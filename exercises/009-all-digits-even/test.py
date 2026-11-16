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


@pytest.mark.it("The function all_digits_even should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "all_digits_even", None)), "Define a function called all_digits_even in app.py"


@pytest.mark.it("all_digits_even(2000, 2030) should return [2000, 2002, 2004, 2006, 2008, 2020, 2022, 2024, 2026, 2028]")
def test_case_1():
    app = load_app()
    result = app.all_digits_even(2000, 2030)
    assert_returns(result, [2000, 2002, 2004, 2006, 2008, 2020, 2022, 2024, 2026, 2028], "all_digits_even(2000, 2030)")


@pytest.mark.it("all_digits_even(1000, 1999) should return []")
def test_case_2():
    app = load_app()
    result = app.all_digits_even(1000, 1999)
    assert_returns(result, [], "all_digits_even(1000, 1999)")


@pytest.mark.it("all_digits_even(1, 10) should return [2, 4, 6, 8]")
def test_case_3():
    app = load_app()
    result = app.all_digits_even(1, 10)
    assert_returns(result, [2, 4, 6, 8], "all_digits_even(1, 10)")
