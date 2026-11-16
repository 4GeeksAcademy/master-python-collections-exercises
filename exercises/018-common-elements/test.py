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


@pytest.mark.it("The function common_elements should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "common_elements", None)), "Define a function called common_elements in app.py"


@pytest.mark.it("common_elements([5, 1, 3, 3, 8], [3, 8, 9, 5]) should return [3, 5, 8]")
def test_case_1():
    app = load_app()
    result = app.common_elements([5, 1, 3, 3, 8], [3, 8, 9, 5])
    assert_returns(result, [3, 5, 8], "common_elements([5, 1, 3, 3, 8], [3, 8, 9, 5])")


@pytest.mark.it("common_elements(['python', 'java'], ['go', 'rust']) should return []")
def test_case_2():
    app = load_app()
    result = app.common_elements(['python', 'java'], ['go', 'rust'])
    assert_returns(result, [], "common_elements(['python', 'java'], ['go', 'rust'])")


@pytest.mark.it("common_elements(['b', 'a', 'c'], ['c', 'a', 'a']) should return ['a', 'c']")
def test_case_3():
    app = load_app()
    result = app.common_elements(['b', 'a', 'c'], ['c', 'a', 'a'])
    assert_returns(result, ['a', 'c'], "common_elements(['b', 'a', 'c'], ['c', 'a', 'a'])")
