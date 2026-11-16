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


@pytest.mark.it("The function robot_distance should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "robot_distance", None)), "Define a function called robot_distance in app.py"


@pytest.mark.it("robot_distance(['UP 5', 'DOWN 3', 'LEFT 3', 'RIGHT 2']) should return 2")
def test_case_1():
    app = load_app()
    result = app.robot_distance(['UP 5', 'DOWN 3', 'LEFT 3', 'RIGHT 2'])
    assert_returns(result, 2, "robot_distance(['UP 5', 'DOWN 3', 'LEFT 3', 'RIGHT 2'])")


@pytest.mark.it("robot_distance(['UP 3', 'RIGHT 4']) should return 5")
def test_case_2():
    app = load_app()
    result = app.robot_distance(['UP 3', 'RIGHT 4'])
    assert_returns(result, 5, "robot_distance(['UP 3', 'RIGHT 4'])")


@pytest.mark.it("robot_distance([]) should return 0")
def test_case_3():
    app = load_app()
    result = app.robot_distance([])
    assert_returns(result, 0, "robot_distance([])")
