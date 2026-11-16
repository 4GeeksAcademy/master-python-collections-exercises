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


@pytest.mark.it("The function word_frequency should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "word_frequency", None)), "Define a function called word_frequency in app.py"


@pytest.mark.it("word_frequency('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.') should return {'2': 2, '3.': 1, '3?': 1, 'New': 1, 'Python': 5, 'Read': 1, 'and': 1, 'between': 1, 'choosing': 1, 'or': 2, 'to': 1}")
def test_case_1():
    app = load_app()
    result = app.word_frequency('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')
    assert_returns(result, {'2': 2, '3.': 1, '3?': 1, 'New': 1, 'Python': 5, 'Read': 1, 'and': 1, 'between': 1, 'choosing': 1, 'or': 2, 'to': 1}, "word_frequency('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')")


@pytest.mark.it("word_frequency('b a b') should return {'a': 1, 'b': 2}")
def test_case_2():
    app = load_app()
    result = app.word_frequency('b a b')
    assert_returns(result, {'a': 1, 'b': 2}, "word_frequency('b a b')")


@pytest.mark.it("The keys of the dictionary should be in alphabetical order")
def test_keys_sorted():
    app = load_app()
    result = app.word_frequency("zeta beta alpha beta")
    assert result is not None, "word_frequency returned None. Did you forget the return statement?"
    assert list(result) == ["alpha", "beta", "zeta"], f"The keys should be sorted, but they are {list(result)}"
