from abc import ABC, abstractmethod
import os
import cv2
from datetime import datetime


class SolvedCaptcha:
    """
    A class interface for representing solved Captchas.
    """

    def __init__(self, image, text, answer=None, out_dir=None):
        """
        :param image: Unprocessed Captcha image
        :param text: The text contained in the captcha image. (eg: 12+3=)
        :param answer: The solved captcha's answer (eg: 15). In the 'jumbled text' captchas this is the same as 'text'.
        :param out_dir: Where to write captchas to. Leave as None if captcha saving is not required.
        """
        self.image = image
        self.text = text
        self.answer = answer
        self.out_dir = out_dir

    def save_captcha(self, correct):
        """
        Saves the Captcha image to the correct or incorrect folder.
        Captchas are saved with a unique filename. This indicates what the captcha text is if correct==True.
        Eg: YYYY-MM-DDTHH-MM-SS.MMM_qwerty.png
        :param correct: Whether the captcha was solved correctly (True) or incorrectly (False)
        """
        if self.out_dir:

            if correct:
                save_dir = os.path.join(self.out_dir, 'correct')
                filename = '{}_{}.png'.format(datetime.now().strftime("%Y-%m-%dT%H-%M-%S.%f")[:-3], self.text)
            else:
                save_dir = os.path.join(self.out_dir, 'incorrect')
                filename = '{}.png'.format(datetime.now().strftime("%Y-%m-%dT%H%M%S.%f")[:-3])
            os.makedirs(save_dir, exist_ok=True)
            cv2.imwrite(os.path.join(save_dir, filename), self.image)


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
