def is_valid_email(email):
    if "@" in email and "." in email and email.index("@") < email.rindex("."):
        return True
    return False