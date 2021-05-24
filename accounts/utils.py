import six

USERNAME_MAX_LENGTH = 32
DISPLAY_NAME_MAX_LENGTH = 65

def validate_username(username):
    if not isinstance(username, six.string_types):
        return False

    if len(username) > USERNAME_MAX_LENGTH:
        return False

    if not username.isalnum():
        return False

    if not username.lower().startswith("cpe"):
        return False

    return True


def validate_display_name(display_name):
    if not isinstance(display_name, six.string_types):
        return False

    if len(display_name) > DISPLAY_NAME_MAX_LENGTH:
        return False

    if not display_name.replace(' ', '').isalnum():
        return False

    return True