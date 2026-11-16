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


@pytest.mark.it("The function count_upper_and_lower should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "count_upper_and_lower", None)), "Define a function called count_upper_and_lower in app.py"


@pytest.mark.it("count_upper_and_lower('Hello world!') should return {'uppercase': 1, 'lowercase': 9}")
def test_case_1():
    app = load_app()
    result = app.count_upper_and_lower('Hello world!')
    assert_returns(result, {'uppercase': 1, 'lowercase': 9}, "count_upper_and_lower('Hello world!')")


@pytest.mark.it("count_upper_and_lower('HTML and CSS') should return {'uppercase': 7, 'lowercase': 3}")
def test_case_2():
    app = load_app()
    result = app.count_upper_and_lower('HTML and CSS')
    assert_returns(result, {'uppercase': 7, 'lowercase': 3}, "count_upper_and_lower('HTML and CSS')")


@pytest.mark.it("count_upper_and_lower('123') should return {'uppercase': 0, 'lowercase': 0}")
def test_case_3():
    app = load_app()
    result = app.count_upper_and_lower('123')
    assert_returns(result, {'uppercase': 0, 'lowercase': 0}, "count_upper_and_lower('123')")
