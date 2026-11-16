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


@pytest.mark.it("The function merge_inventories should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "merge_inventories", None)), "Define a function called merge_inventories in app.py"


@pytest.mark.it("merge_inventories({'apple': 5, 'pear': 2}, {'apple': 3, 'kiwi': 7}) should return {'apple': 8, 'pear': 2, 'kiwi': 7}")
def test_case_1():
    app = load_app()
    result = app.merge_inventories({'apple': 5, 'pear': 2}, {'apple': 3, 'kiwi': 7})
    assert_returns(result, {'apple': 8, 'pear': 2, 'kiwi': 7}, "merge_inventories({'apple': 5, 'pear': 2}, {'apple': 3, 'kiwi': 7})")


@pytest.mark.it("merge_inventories({}, {'milk': 1}) should return {'milk': 1}")
def test_case_2():
    app = load_app()
    result = app.merge_inventories({}, {'milk': 1})
    assert_returns(result, {'milk': 1}, "merge_inventories({}, {'milk': 1})")


@pytest.mark.it("merge_inventories({'egg': 12}, {}) should return {'egg': 12}")
def test_case_3():
    app = load_app()
    result = app.merge_inventories({'egg': 12}, {})
    assert_returns(result, {'egg': 12}, "merge_inventories({'egg': 12}, {})")


@pytest.mark.it("merge_inventories should not modify the original dictionaries")
def test_does_not_mutate():
    app = load_app()
    store_a = {"apple": 5, "pear": 2}
    store_b = {"apple": 3, "kiwi": 7}
    app.merge_inventories(store_a, store_b)
    assert store_a == {"apple": 5, "pear": 2}, "store_a was modified. Work on a copy instead."
    assert store_b == {"apple": 3, "kiwi": 7}, "store_b was modified. Work on a copy instead."
