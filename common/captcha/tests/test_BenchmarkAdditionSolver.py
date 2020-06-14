import pytest
from common.captcha.benchmark.BenchmarkAdditionSolver import CaptchaSolver
import os
import cv2


@pytest.fixture(scope='module')
def testdatadir(request):
    # Get a py.path.local, which is a bit friendlier to work with.
    return request.fspath.join('..')


class TestBenchmarkAdditionSolver:

    def test_folder_creation(self, tmpdir, testdatadir):
        td = tmpdir.mkdir('captcha')
        captcha_solver = CaptchaSolver(out_dir=td)
        test_captcha = cv2.imread(testdatadir.join('test_BenchmarkAdditionSolver_valid.png').strpath)

        solved_captcha = captcha_solver.solve_captcha(test_captcha)
        solved_captcha.save_captcha(correct=True)
        solved_captcha.save_captcha(correct=False)

        # Check the relevant incorrect/correct folders were created.
        assert os.path.exists(td.join('incorrect'))
        assert os.path.exists(td.join('correct'))

    def test_ocr(self, tmpdir, testdatadir):
        # Do OCR on easy image to ensure it's working
        td = tmpdir.mkdir('captcha')
        captcha_solver = CaptchaSolver(out_dir=td)

        test_img1 = cv2.imread(testdatadir.join('test_BenchmarkAdditionSolver_valid.png').strpath)
        test_img2 = cv2.imread(testdatadir.join('test_BenchmarkAdditionSolver_invalid.png').strpath)
        captcha_text1 = captcha_solver.read_captcha(test_img1)
        captcha_text2 = captcha_solver.read_captcha(test_img2)

        assert captcha_text1 == '123'
        assert captcha_text2 == '12'

    def test_first_second_separation(self, tmpdir, testdatadir):
        # Tests correct separation of first_number (first 2 digits) and second_number (last digit)
        td = tmpdir.mkdir('captcha')
        captcha_solver = CaptchaSolver(out_dir=td)

        test_img = cv2.imread(testdatadir.join('test_BenchmarkAdditionSolver_valid.png').strpath)
        solved_captcha = captcha_solver.solve_captcha(test_img)

        assert solved_captcha.text == '12+3='
        assert solved_captcha.answer == 15

    def test_first_second_separation_invalid(self, tmpdir, testdatadir):
        # Tests the case where only 2 out of 3 digits are read by OCR. Should return a SolvedCaptcha with blank text and answer.
        td = tmpdir.mkdir('captcha')
        captcha_solver = CaptchaSolver(out_dir=td)

        test_img = cv2.imread(testdatadir.join('test_BenchmarkAdditionSolver_invalid.png').strpath)
        solved_captcha = captcha_solver.solve_captcha(test_img)

        assert solved_captcha.text == ''
        assert solved_captcha.answer == ''


    def test_captcha_fail_save(self, tmpdir, testdatadir):
        td = tmpdir.mkdir('captcha')
        captcha_solver = CaptchaSolver(out_dir=td)
        test_img = cv2.imread(testdatadir.join('test_BenchmarkAdditionSolver_valid.png').strpath)

        solved_captcha = captcha_solver.solve_captcha(test_img)
        solved_captcha.save_captcha(correct=False)
        assert len(os.listdir(td.join('incorrect'))) == 1

    def test_captcha_success_save(self, tmpdir, testdatadir):
        td = tmpdir.mkdir('captcha')
        captcha_solver = CaptchaSolver(out_dir=td)
        test_img = cv2.imread(testdatadir.join('test_BenchmarkAdditionSolver_valid.png').strpath)

        solved_captcha = captcha_solver.solve_captcha(test_img)
        solved_captcha.save_captcha(correct=True)

        print("files in directory:", os.listdir(td.join('correct')))
        assert len([f for f in os.listdir(td.join('correct')) if f.endswith('12+3=.png')]) == 1
