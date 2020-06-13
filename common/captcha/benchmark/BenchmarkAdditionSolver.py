import os
import re
import cv2
import numpy as np
import pytesseract.pytesseract as tesseract
from common.captcha.CaptchaSolverInterface import CaptchaSolverInterface, SolvedCaptcha


class CaptchaSolver(CaptchaSolverInterface):
    """
    Class for solving addition Captchas used on Benchmark-based Portals
    These are easy Captchas for these reasons:
        1. They always use addition, so the math operation is always the same.
        2. They always have two digits on the left-side of the addition.
        3. They always have one digit on the right-side of the addition.
        4. The text has no distortion.
        5. Background 'noise' is usually a different colour to the text, so can easily be filtered out in preprocessing.
    """

    def __init__(self, out_dir=None):
        self.out_dir = out_dir or os.path.join(os.getcwd(), 'captcha')

    def solve_captcha(self, captcha_image) -> SolvedCaptcha:
        """
        Solve Captcha and return its value
        :param captcha_image: Selenium screenshot buffer of captcha
        :return: Captcha answer
        """
        # Convert Selenium screenshot buffer to OpenCV CV2 Image
        captcha_image = self.__convert_captcha_img__(captcha_image)

        # Read digits in captcha
        captcha_digits = self.read_captcha(captcha_image)

        if len(captcha_digits) >= 3:
            # Do the sum
            first_number = int(captcha_digits[:2])
            second_number = int(captcha_digits[-1])
            captcha_sum = first_number + second_number
            captcha_text = '{}+{}='.format(first_number, second_number)
            solved = SolvedCaptcha(captcha_image, captcha_text, captcha_sum, self.out_dir)
            return solved
        else:
            # Something went wrong during OCR. Return a blank captcha result.
            return SolvedCaptcha(captcha_image, '', '', self.out_dir)


    def read_captcha(self, captcha_buffer):
        """
        Read the text contained in a captcha
        :param captcha_buffer: Selenium screenshot buffer of captcha
        :return: Text contained in captcha
        """
        processed_captcha = self.__preprocess_captcha__(captcha_buffer)

        # Use Tesseract to perform OCR on processed captcha, using a limited character-set and Page Segmentation Mode 7
        captcha_text = tesseract.image_to_string(processed_captcha, config="-c tessedit_char_whitelist=0123456789+=? --psm 7")
        # Remove any symbols from the text
        captcha_text = re.sub("[^0-9]", "", captcha_text)
        return captcha_text


    def __convert_captcha_img__(self, captcha_buffer):
        """
        :param captcha: Selenium screenshot buffer of a captcha to convert to OpenCV CV2 image.
        :return: Converted Captcha as an OpenCV2 Image
        """
        if isinstance(captcha_buffer, bytes):
            # Load from selenium screenshot_as_png into cv2 format
            captcha_nparr = np.frombuffer(captcha_buffer, np.uint8)
            captcha_img = cv2.imdecode(captcha_nparr, cv2.IMREAD_COLOR)
        elif isinstance(captcha_buffer, np.ndarray):
            # Already CV2 format
            captcha_img = captcha_buffer
        else:
            raise ValueError('Captcha image passed as invalid type:', type(captcha_buffer))

        return captcha_img


    def __preprocess_captcha__(self, captcha_img):
        """
        Background noise can mostly be removed by thresholding HSV values. This is done in preprocessing.
        See https://stackoverflow.com/a/53978868/6008271
        :param self: Captcha to preprocess as a OpenCV CV2 Image.
        :return: Preprocessed captcha as opencv cv2 image
        """
        # Convert captcha image to HSV colour space
        hsv = cv2.cvtColor(captcha_img, cv2.COLOR_BGR2HSV)

        # Mask the image's S and V values to suppress colour in the captcha
        mask = cv2.inRange(hsv, (0, 0, 0), (180, 45, 175))
        cv2.bitwise_and(captcha_img, captcha_img, mask=mask)
        # Invert the image to give white text on a black background
        captcha = cv2.bitwise_not(mask)

        return captcha