#!/usr/bin/env python3
"""
Module encrypt password
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a randomly generated salt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted, hashed password as a byte string.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates whether a provided password matches the given hashed password.

    Args:
        hashed_password (bytes): The hashed password to check against.
        password (str): The plaintext password to verify.

    Returns:
        bool: True if the password matches the hashed password,
        False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
