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


@pytest.mark.it("The function remove_duplicate_words should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "remove_duplicate_words", None)), "Define a function called remove_duplicate_words in app.py"


@pytest.mark.it("remove_duplicate_words('hello world and practice makes perfect and hello world again') should return 'again and hello makes perfect practice world'")
def test_case_1():
    app = load_app()
    result = app.remove_duplicate_words('hello world and practice makes perfect and hello world again')
    assert_returns(result, 'again and hello makes perfect practice world', "remove_duplicate_words('hello world and practice makes perfect and hello world again')")


@pytest.mark.it("remove_duplicate_words('b a b a c') should return 'a b c'")
def test_case_2():
    app = load_app()
    result = app.remove_duplicate_words('b a b a c')
    assert_returns(result, 'a b c', "remove_duplicate_words('b a b a c')")
