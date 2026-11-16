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


@pytest.mark.it("The function two_dimensional_list should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "two_dimensional_list", None)), "Define a function called two_dimensional_list in app.py"


@pytest.mark.it("two_dimensional_list(3, 5) should return [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]")
def test_case_1():
    app = load_app()
    result = app.two_dimensional_list(3, 5)
    assert_returns(result, [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]], "two_dimensional_list(3, 5)")


@pytest.mark.it("two_dimensional_list(2, 2) should return [[0, 0], [0, 1]]")
def test_case_2():
    app = load_app()
    result = app.two_dimensional_list(2, 2)
    assert_returns(result, [[0, 0], [0, 1]], "two_dimensional_list(2, 2)")


@pytest.mark.it("two_dimensional_list(1, 3) should return [[0, 0, 0]]")
def test_case_3():
    app = load_app()
    result = app.two_dimensional_list(1, 3)
    assert_returns(result, [[0, 0, 0]], "two_dimensional_list(1, 3)")
