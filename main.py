

def build_roster(registrations):
    """
    Given a list of (student_id, course_id) pairs, build a course roster.

    The result should be a dictionary where:
      - each key is a course id (string)
      - each value is a sorted list of unique student ids (strings)
        enrolled in that course

    Duplicate registrations for the same (student_id, course_id) pair
    should appear only once in the output.
    """

    # Build a mapping course_id -> set of unique student_ids
    rosters = {}
    for student_id, course_id in registrations:
        if course_id not in rosters:
            rosters[course_id] = set()
        rosters[course_id].add(student_id)

    # Convert sets to sorted lists
    for course_id in list(rosters.keys()):
        rosters[course_id] = sorted(rosters[course_id])

    return rosters


if __name__ == "__main__":
    # Optional manual test
    sample = [
        ("s1", "CS101"),
        ("s2", "CS101"),
        ("s1", "MATH200"),
        ("s1", "CS101"),
    ]
    print(build_roster(sample))
