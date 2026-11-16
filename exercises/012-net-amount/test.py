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


@pytest.mark.it("The function net_amount should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "net_amount", None)), "Define a function called net_amount in app.py"


@pytest.mark.it("net_amount('D 300 D 300 W 200 D 100') should return 500")
def test_case_1():
    app = load_app()
    result = app.net_amount('D 300 D 300 W 200 D 100')
    assert_returns(result, 500, "net_amount('D 300 D 300 W 200 D 100')")


@pytest.mark.it("net_amount('W 50') should return -50")
def test_case_2():
    app = load_app()
    result = app.net_amount('W 50')
    assert_returns(result, -50, "net_amount('W 50')")


@pytest.mark.it("net_amount('') should return 0")
def test_case_3():
    app = load_app()
    result = app.net_amount('')
    assert_returns(result, 0, "net_amount('')")
