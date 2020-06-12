from abc import ABC, abstractmethod
import os
import cv2
import time


class SolvedCaptcha:
    """
    A class interface for representing solved Captchas.
    """

    def __init__(self, image, text, answer=None, out_dir=None):
        """
        :param image: Unprocessed Captcha image
        :param text: The text contained in the captcha image. (eg: 12+3=)
        :param answer: The solved captcha's answer (eg: 15). In the 'jumbled text' captchas this is the same as 'text'.
        :param out_dir: Where to write captchas to upon notify_correct() or notify_incorrect()
        """
        self.image = image
        self.text = text
        self.answer = answer
        self.out_dir = out_dir

    def notify_correct(self):
        """
        Writes the Captcha's image to self.correct_dir
        This should be called in the case a captcha is solved correctly.
        Captchas should be solved with a unique filename indicating what the captcha says.
        Eg: YYYYMMDD-HHMMSS_qwerty.png
        """
        try:
            correct_dir = os.path.join(self.out_dir, 'correct')
            os.makedirs(correct_dir, exist_ok=True)
            filename = '{}_{}.png'.format(time.strftime("%Y%m%d-%H%M%S"), self.text)
            cv2.imwrite(os.path.join(correct_dir, filename), self.image)
        except TypeError:
            raise NotADirectoryError('notify_incorrect() was called on SolvedCaptcha when no out_dir was given.')

    def notify_incorrect(self):
        """
        Writes the Captcha's image to self.incorrect_dir
        This should be called in the case a captcha is solved incorrectly.
        Captchas should be solved with a unique filename. Eg: YYYYMMDD-HHMMSS.png
        """
        try:
            incorrect_dir = os.path.join(self.out_dir, 'incorrect')
            os.makedirs(incorrect_dir, exist_ok=True)
            filename = '{}.png'.format(time.strftime("%Y%m%d-%H%M%S"))
            cv2.imwrite(os.path.join(incorrect_dir, filename), self.image)
        except TypeError:
            raise NotADirectoryError('notify_incorrect() was called on SolvedCaptcha when no out_dir was given.')



class CaptchaSolverInterface(ABC):
    """
    A formal Class interface to use when creating Captcha Solvers for different Captcha types.
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        # Ensure subclasses conform to the interface.
        return (hasattr(subclass, 'solve_captcha') and
                callable(subclass.solve_captcha) and
                hasattr(subclass, '__preprocess_captcha__') and
                callable(subclass.__preprocess_captcha__) or
                NotImplemented)


    @abstractmethod
    def solve_captcha(self, captcha_image) -> SolvedCaptcha:
        """
        Solve the Captcha and return the answer as a SolvedCaptcha object.
        :param captcha_image: Buffer containing the captcha image
        :return: SolvedCaptcha object
        """
        raise NotImplementedError


    @abstractmethod
    def __preprocess_captcha__(self, captcha_in):
        """
        Preprocess the raw captcha image.
        This might involve computer vision techniques such as thresholding using libraries like OpenCV or PIL.
        What this function does is highly dependent on the type of captcha you are trying to solve.

        :param captcha_in: Captcha to preprocess
        :return: Preprocessed captcha
        """
        raise NotImplementedError
