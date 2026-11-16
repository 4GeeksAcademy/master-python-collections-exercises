import importlib.util
import os

import pytest

APP_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.py")


def load_app():
    """Load the student's app.py as a fresh module."""
    spec = importlib.util.spec_from_file_location("student_app", APP_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_returns(result, expected, call):
    assert result is not None, f"{call} returned None. Did you forget the return statement?"
    assert result == expected, f"{call} should return {expected!r}, but it returned {result!r}"


@pytest.mark.it("The function count_letters_and_digits should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "count_letters_and_digits", None)), "Define a function called count_letters_and_digits in app.py"


@pytest.mark.it("count_letters_and_digits('hello world! 123') should return {'letters': 10, 'digits': 3}")
def test_case_1():
    app = load_app()
    result = app.count_letters_and_digits('hello world! 123')
    assert_returns(result, {'letters': 10, 'digits': 3}, "count_letters_and_digits('hello world! 123')")


@pytest.mark.it("count_letters_and_digits('4Geeks Academy 2026') should return {'letters': 12, 'digits': 5}")
def test_case_2():
    app = load_app()
    result = app.count_letters_and_digits('4Geeks Academy 2026')
    assert_returns(result, {'letters': 12, 'digits': 5}, "count_letters_and_digits('4Geeks Academy 2026')")


@pytest.mark.it("count_letters_and_digits('!!!') should return {'letters': 0, 'digits': 0}")
def test_case_3():
    app = load_app()
    result = app.count_letters_and_digits('!!!')
    assert_returns(result, {'letters': 0, 'digits': 0}, "count_letters_and_digits('!!!')")
