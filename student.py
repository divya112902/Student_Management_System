
def validate_student(name, email):
    """Validate student name and email."""
    if not name or not name.strip():
        return False

    if not email or "@" not in email:
        return False

    if "." not in email.split("@")[-1]:
        return False

    return True


def validate_student_email(email):
    """Validate a student's email address."""
    if not email or "@" not in email:
        return False

    username, domain = email.split("@", 1)

    if not username or not domain:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


def test_student_validation():
    assert validate_student("Divya", "divya@example.com")
    assert not validate_student("", "divya@example.com")
    assert not validate_student("Divya", "invalid-email")


def test_student_email_validation():
    assert validate_student_email("divya@example.com")
    assert not validate_student_email("invalid-email")
    assert not validate_student_email("@example.com")
    assert not validate_student_email("divya@")
    print("All student validation tests passed!")


if __name__ == "__main__":
    test_student_validation()
    test_student_email_validation()
