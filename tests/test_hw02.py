import os
import sys
import pytest

# Ensure we can import main.py from the homework folder.
# Put the homework folder first on sys.path so it takes precedence
# and remove any previously-imported top-level `main` to avoid
# importing a different project's `main.py` from a cached module.
project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# If a different `main` module was already imported (from another
# project), remove it so Python will import the correct one below.
if "main" in sys.modules:
    del sys.modules["main"]

from main import build_roster


@pytest.mark.parametrize(
    "registrations, expected",
    [
        (
            [("s1", "CS101"), ("s2", "CS101")],
            {"CS101": ["s1", "s2"]},
        ),
        (
            [("s1", "CS101"), ("s1", "MATH200")],
            {"CS101": ["s1"], "MATH200": ["s1"]},
        ),
        (
            [("s2", "ENG10")],
            {"ENG10": ["s2"]},
        ),
        (
            [],
            {},
        ),
    ],
)
def test_normal_cases(registrations, expected):
    assert build_roster(registrations) == expected


@pytest.mark.parametrize(
    "registrations, expected",
    [
        (
            [("s1", "CS101"), ("s1", "CS101")],
            {"CS101": ["s1"]},
        ),
        (
            [("s1", "CS101"), ("s2", "CS101"), ("s2", "CS101")],
            {"CS101": ["s1", "s2"]},
        ),
        (
            [("s1", "CS101"), ("s1", "cs101")],
            {"CS101": ["s1"], "cs101": ["s1"]},
        ),
    ],
)
def test_edge_cases_duplicates_and_case(registrations, expected):
    assert build_roster(registrations) == expected


@pytest.mark.parametrize(
    "registrations, expected_courses, expected_total_students",
    [
        (
            [("s" + str(i), "CS101") for i in range(10)],
            {"CS101"},
            10,
        ),
        (
            [("s" + str(i), "C" + str(i % 3)) for i in range(30)],
            {"C0", "C1", "C2"},
            30,
        ),
        (
            [("s" + str(i % 5), "C" + str(i % 4)) for i in range(40)],
            {"C0", "C1", "C2", "C3"},
            5,  # only 5 unique students total
        ),
    ],
)
def test_larger_and_mixed_inputs(registrations, expected_courses, expected_total_students):
    roster = build_roster(registrations)
    assert set(roster.keys()) == expected_courses
    # Count unique students across all courses
    all_students = set()
    for students in roster.values():
        assert students == sorted(students)
        all_students.update(students)
    assert len(all_students) == expected_total_students
