def check_strength(password):
    """
    Check if a password is strong based on length.

    Args:
        password (str): Password string to evaluate.

    Returns:
        bool: True if password length >= 8, else False.
    """
    return len(password) >= 8