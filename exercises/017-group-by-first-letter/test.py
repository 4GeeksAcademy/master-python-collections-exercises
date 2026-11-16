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


@pytest.mark.it("The function group_by_first_letter should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "group_by_first_letter", None)), "Define a function called group_by_first_letter in app.py"


@pytest.mark.it("group_by_first_letter(['apple', 'banana', 'avocado', 'blueberry', 'cherry']) should return {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}")
def test_case_1():
    app = load_app()
    result = app.group_by_first_letter(['apple', 'banana', 'avocado', 'blueberry', 'cherry'])
    assert_returns(result, {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}, "group_by_first_letter(['apple', 'banana', 'avocado', 'blueberry', 'cherry'])")


@pytest.mark.it("group_by_first_letter(['zoo']) should return {'z': ['zoo']}")
def test_case_2():
    app = load_app()
    result = app.group_by_first_letter(['zoo'])
    assert_returns(result, {'z': ['zoo']}, "group_by_first_letter(['zoo'])")


@pytest.mark.it("group_by_first_letter([]) should return {}")
def test_case_3():
    app = load_app()
    result = app.group_by_first_letter([])
    assert_returns(result, {}, "group_by_first_letter([])")
