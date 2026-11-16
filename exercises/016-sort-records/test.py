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


@pytest.mark.it("The function sort_records should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "sort_records", None)), "Define a function called sort_records in app.py"


@pytest.mark.it("sort_records(['Tom,19,80', 'John,20,90', 'Jony,17,91', 'Jony,17,93', 'Jason,21,85']) should return [('Jason', '21', '85'), ('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Tom', '19', '80')]")
def test_case_1():
    app = load_app()
    result = app.sort_records(['Tom,19,80', 'John,20,90', 'Jony,17,91', 'Jony,17,93', 'Jason,21,85'])
    assert_returns(result, [('Jason', '21', '85'), ('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Tom', '19', '80')], "sort_records(['Tom,19,80', 'John,20,90', 'Jony,17,91', 'Jony,17,93', 'Jason,21,85'])")


@pytest.mark.it("sort_records(['Ana,30,70', 'Ana,25,99', 'Ana,25,50']) should return [('Ana', '25', '50'), ('Ana', '25', '99'), ('Ana', '30', '70')]")
def test_case_2():
    app = load_app()
    result = app.sort_records(['Ana,30,70', 'Ana,25,99', 'Ana,25,50'])
    assert_returns(result, [('Ana', '25', '50'), ('Ana', '25', '99'), ('Ana', '30', '70')], "sort_records(['Ana,30,70', 'Ana,25,99', 'Ana,25,50'])")
