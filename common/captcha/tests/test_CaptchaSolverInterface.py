import pytest
import cv2
import os
from common.captcha.CaptchaSolverInterface import CaptchaSolverInterface, SolvedCaptcha


@pytest.fixture(scope='module')
def testdatadir(request):
    # Get a py.path.local, which is a bit friendlier to work with.
    return request.fspath.join('..')


class TestCaptchaSolverInterface:

    def test_interface_not_implemented(self):
        # Creates a CaptchaSolverInterface subclass where functions in the interface have not been implemented.

        # Should fail because __preprocess_captcha__ is not implemented
        class TestCaptchaClass(CaptchaSolverInterface):
            def solve_captcha(self, captcha_image):
                pass

        # Should fail because solve_captcha is not implemented
        class TestCaptchaClass2(CaptchaSolverInterface):
            def __preprocess_captcha__(self, captcha_in):
                pass

        # Should fail because no functions are implemented
        class TestCaptchaClass3(CaptchaSolverInterface):
            pass

        try:
            TestCaptchaClass()
            pytest.fail('CaptchaSolverInterface does not enforce implementation of __preprocess_captcha__() method.')
        except TypeError:
            pass

        try:
            TestCaptchaClass2()
            pytest.fail('CaptchaSolverInterface does not enforce implementation of solve_captcha() method.')
        except TypeError:
            pass

        try:
            TestCaptchaClass3()
            pytest.fail('CaptchaSolverInterface does not enforce implementation of any interface methods.')
        except TypeError:
            pass

    def test_interface_implemented(self):
        # Ensures when all interface methods are implemented instantiation works as expected.
        class TestCaptchaClass(CaptchaSolverInterface):
            def solve_captcha(self, captcha_image) -> SolvedCaptcha:
                pass

            def __preprocess_captcha__(self, captcha_in):
                pass

        TestCaptchaClass()


class TestSolvedCaptchaObject:

    def test_init(self, testdatadir):
        captcha_data = cv2.imread(testdatadir.join('test_BenchmarkAdditionSolver_valid.png').strpath)
        test1 = SolvedCaptcha(captcha_data, 'test', '123', r'C:\Example')

        assert (test1.image == captcha_data).all()
        assert test1.text == 'test'
        assert test1.answer == '123'
        assert test1.out_dir == r'C:\Example'

        test2 = SolvedCaptcha(captcha_data, 'test', out_dir=r'C:\Example')
        assert (test2.image == captcha_data).all()
        assert test2.text == 'test'
        assert test2.answer is None
        assert test2.out_dir == r'C:\Example'

        test3 = SolvedCaptcha(captcha_data, 'test', '123')
        assert (test3.image == captcha_data).all()
        assert test3.text == 'test'
        assert test3.answer == '123'
        assert test3.out_dir is None

    def test_notify_correct(self, tmpdir, testdatadir):
        td = tmpdir.mkdir('captcha')
        captcha_data = cv2.imread(testdatadir.join('test_BenchmarkAdditionSolver_valid.png').strpath)
        test1 = SolvedCaptcha(captcha_data, 'test', '123', td)
        test1.notify_correct()

        assert os.path.exists(td.join('correct'))
        assert len([f for f in os.listdir(td.join('correct')) if f.endswith('test.png')]) == 1

    def test_notify_incorrect(self, tmpdir, testdatadir):
        td = tmpdir.mkdir('captcha')
        captcha_data = cv2.imread(testdatadir.join('test_BenchmarkAdditionSolver_invalid.png').strpath)
        test1 = SolvedCaptcha(captcha_data, 'test', '123', td)
        test1.notify_incorrect()

        assert os.path.exists(td.join('incorrect'))
        assert len([f for f in os.listdir(td.join('incorrect')) if f.endswith('.png')]) == 1

    def test_notify_correct_no_path(self, testdatadir):
        # Tests marking a captcha as correct if no out_dir was given.
        captcha_data = cv2.imread(testdatadir.join('test_BenchmarkAdditionSolver_valid.png').strpath)
        test1 = SolvedCaptcha(captcha_data, 'test', '123')
        try:
            test1.notify_correct()
            pytest.fail(
                'notify_correct() does not raise NotADirectoryError when out_dir is not specified at instantiation.')
        except NotADirectoryError:
            pass

    def test_notify_incorrect_no_path(self, testdatadir):
        # Tests marking a captcha as incorrect if no out_dir was given.
        captcha_data = cv2.imread(testdatadir.join('test_BenchmarkAdditionSolver_invalid.png').strpath)
        test1 = SolvedCaptcha(captcha_data, 'test', '123')
        try:
            test1.notify_incorrect()
            pytest.fail(
                'notify_incorrect() does not raise NotADirectoryError when out_dir is not specified at instantiation.')
        except NotADirectoryError:
            pass
