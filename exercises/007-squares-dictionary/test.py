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


@pytest.mark.it("The function squares_dictionary should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "squares_dictionary", None)), "Define a function called squares_dictionary in app.py"


@pytest.mark.it("squares_dictionary(5) should return {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}")
def test_case_1():
    app = load_app()
    result = app.squares_dictionary(5)
    assert_returns(result, {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}, "squares_dictionary(5)")


@pytest.mark.it("squares_dictionary(8) should return {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}")
def test_case_2():
    app = load_app()
    result = app.squares_dictionary(8)
    assert_returns(result, {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}, "squares_dictionary(8)")


@pytest.mark.it("squares_dictionary(1) should return {1: 1}")
def test_case_3():
    app = load_app()
    result = app.squares_dictionary(1)
    assert_returns(result, {1: 1}, "squares_dictionary(1)")
