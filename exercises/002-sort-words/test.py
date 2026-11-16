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


@pytest.mark.it("The function sort_words should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "sort_words", None)), "Define a function called sort_words in app.py"


@pytest.mark.it("sort_words('without,hello,bag,world') should return 'bag,hello,without,world'")
def test_case_1():
    app = load_app()
    result = app.sort_words('without,hello,bag,world')
    assert_returns(result, 'bag,hello,without,world', "sort_words('without,hello,bag,world')")


@pytest.mark.it("sort_words('pear,apple,mango') should return 'apple,mango,pear'")
def test_case_2():
    app = load_app()
    result = app.sort_words('pear,apple,mango')
    assert_returns(result, 'apple,mango,pear', "sort_words('pear,apple,mango')")


@pytest.mark.it("sort_words('one') should return 'one'")
def test_case_3():
    app = load_app()
    result = app.sort_words('one')
    assert_returns(result, 'one', "sort_words('one')")
