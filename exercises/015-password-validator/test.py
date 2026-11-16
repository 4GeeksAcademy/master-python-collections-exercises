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


@pytest.mark.it("The function is_valid_password should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "is_valid_password", None)), "Define a function called is_valid_password in app.py"


@pytest.mark.it("is_valid_password('ABd1234@1') should return True")
def test_case_1():
    app = load_app()
    result = app.is_valid_password('ABd1234@1')
    assert_returns(result, True, "is_valid_password('ABd1234@1')")


@pytest.mark.it("is_valid_password('abc123') should return False")
def test_case_2():
    app = load_app()
    result = app.is_valid_password('abc123')
    assert_returns(result, False, "is_valid_password('abc123')")


@pytest.mark.it("is_valid_password('Ab1$') should return False")
def test_case_3():
    app = load_app()
    result = app.is_valid_password('Ab1$')
    assert_returns(result, False, "is_valid_password('Ab1$')")


@pytest.mark.it("is_valid_password('Abcdefgh1234$') should return False")
def test_case_4():
    app = load_app()
    result = app.is_valid_password('Abcdefgh1234$')
    assert_returns(result, False, "is_valid_password('Abcdefgh1234$')")


@pytest.mark.it("is_valid_password('aB3#xy') should return True")
def test_case_5():
    app = load_app()
    result = app.is_valid_password('aB3#xy')
    assert_returns(result, True, "is_valid_password('aB3#xy')")


@pytest.mark.it("is_valid_password('ABCD12#$') should return False")
def test_case_6():
    app = load_app()
    result = app.is_valid_password('ABCD12#$')
    assert_returns(result, False, "is_valid_password('ABCD12#$')")
