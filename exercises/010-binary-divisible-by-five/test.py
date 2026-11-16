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


@pytest.mark.it("The function binary_divisible_by_five should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "binary_divisible_by_five", None)), "Define a function called binary_divisible_by_five in app.py"


@pytest.mark.it("binary_divisible_by_five('0100,0011,1010,1001') should return ['1010']")
def test_case_1():
    app = load_app()
    result = app.binary_divisible_by_five('0100,0011,1010,1001')
    assert_returns(result, ['1010'], "binary_divisible_by_five('0100,0011,1010,1001')")


@pytest.mark.it("binary_divisible_by_five('0101,1111,0000,0110') should return ['0101', '1111', '0000']")
def test_case_2():
    app = load_app()
    result = app.binary_divisible_by_five('0101,1111,0000,0110')
    assert_returns(result, ['0101', '1111', '0000'], "binary_divisible_by_five('0101,1111,0000,0110')")


@pytest.mark.it("binary_divisible_by_five('0001,0010') should return []")
def test_case_3():
    app = load_app()
    result = app.binary_divisible_by_five('0001,0010')
    assert_returns(result, [], "binary_divisible_by_five('0001,0010')")
