
def validate_student(name, email):
    """Validate student name and email."""
    if not name or not name.strip():
        return False

    if not email or "@" not in email:
        return False

    if "." not in email.split("@")[-1]:
        return False

    return True


def test_student_validation():
    assert validate_student("Divya", "divya@example.com")
    assert not validate_student("", "divya@example.com")
    assert not validate_student("Divya", "invalid-email")
    print("All student validation tests passed!")


if __name__ == "__main__":
    test_student_validation()
