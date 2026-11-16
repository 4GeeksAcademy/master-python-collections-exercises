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


@pytest.mark.it("The function to_uppercase should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "to_uppercase", None)), "Define a function called to_uppercase in app.py"


@pytest.mark.it("to_uppercase('Hello world, practice makes perfect') should return 'HELLO WORLD, PRACTICE MAKES PERFECT'")
def test_case_1():
    app = load_app()
    result = app.to_uppercase('Hello world, practice makes perfect')
    assert_returns(result, 'HELLO WORLD, PRACTICE MAKES PERFECT', "to_uppercase('Hello world, practice makes perfect')")


@pytest.mark.it("to_uppercase('python 3.12') should return 'PYTHON 3.12'")
def test_case_2():
    app = load_app()
    result = app.to_uppercase('python 3.12')
    assert_returns(result, 'PYTHON 3.12', "to_uppercase('python 3.12')")


@pytest.mark.it("to_uppercase('') should return ''")
def test_case_3():
    app = load_app()
    result = app.to_uppercase('')
    assert_returns(result, '', "to_uppercase('')")
