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


@pytest.mark.it("The function flatten should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "flatten", None)), "Define a function called flatten in app.py"


@pytest.mark.it("flatten([[1, 2], [3], [], [4, 5, 6]]) should return [1, 2, 3, 4, 5, 6]")
def test_case_1():
    app = load_app()
    result = app.flatten([[1, 2], [3], [], [4, 5, 6]])
    assert_returns(result, [1, 2, 3, 4, 5, 6], "flatten([[1, 2], [3], [], [4, 5, 6]])")


@pytest.mark.it("flatten([[0, 0], [0, 1], [0, 2]]) should return [0, 0, 0, 1, 0, 2]")
def test_case_2():
    app = load_app()
    result = app.flatten([[0, 0], [0, 1], [0, 2]])
    assert_returns(result, [0, 0, 0, 1, 0, 2], "flatten([[0, 0], [0, 1], [0, 2]])")


@pytest.mark.it("flatten([]) should return []")
def test_case_3():
    app = load_app()
    result = app.flatten([])
    assert_returns(result, [], "flatten([])")
