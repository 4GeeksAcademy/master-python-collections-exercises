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


@pytest.mark.it("The function square_odd_numbers should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "square_odd_numbers", None)), "Define a function called square_odd_numbers in app.py"


@pytest.mark.it("square_odd_numbers('1,2,3,4,5,6,7,8,9') should return [1, 9, 25, 49, 81]")
def test_case_1():
    app = load_app()
    result = app.square_odd_numbers('1,2,3,4,5,6,7,8,9')
    assert_returns(result, [1, 9, 25, 49, 81], "square_odd_numbers('1,2,3,4,5,6,7,8,9')")


@pytest.mark.it("square_odd_numbers('10,11,12') should return [121]")
def test_case_2():
    app = load_app()
    result = app.square_odd_numbers('10,11,12')
    assert_returns(result, [121], "square_odd_numbers('10,11,12')")


@pytest.mark.it("square_odd_numbers('2,4,6') should return []")
def test_case_3():
    app = load_app()
    result = app.square_odd_numbers('2,4,6')
    assert_returns(result, [], "square_odd_numbers('2,4,6')")
