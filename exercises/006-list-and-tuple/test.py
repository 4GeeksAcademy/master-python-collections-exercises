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


@pytest.mark.it("The function list_and_tuple should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "list_and_tuple", None)), "Define a function called list_and_tuple in app.py"


@pytest.mark.it("list_and_tuple(34, 67, 55) should return (['34', '67', '55'], ('34', '67', '55'))")
def test_case_1():
    app = load_app()
    result = app.list_and_tuple(34, 67, 55)
    assert_returns(result, (['34', '67', '55'], ('34', '67', '55')), "list_and_tuple(34, 67, 55)")


@pytest.mark.it("list_and_tuple(34, 67, 55, 33, 12, 98) should return (['34', '67', '55', '33', '12', '98'], ('34', '67', '55', '33', '12', '98'))")
def test_case_2():
    app = load_app()
    result = app.list_and_tuple(34, 67, 55, 33, 12, 98)
    assert_returns(result, (['34', '67', '55', '33', '12', '98'], ('34', '67', '55', '33', '12', '98')), "list_and_tuple(34, 67, 55, 33, 12, 98)")


@pytest.mark.it("list_and_tuple(7) should return (['7'], ('7',))")
def test_case_3():
    app = load_app()
    result = app.list_and_tuple(7)
    assert_returns(result, (['7'], ('7',)), "list_and_tuple(7)")
