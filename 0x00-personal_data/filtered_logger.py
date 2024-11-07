#!/usr/bin/env python3
"""
Module filtered_logger

This module provides a function to obfuscate specified fields in
log messages using regular expressions.
"""

import logging
from typing import List
from re import sub


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message by
    replacing their values with a redaction string.

    Args:
        fields (List[str]): representing the fields to obfuscate.
        redaction (str): The string to replace the field values with.
        message (str): The log line in which fields need to be obfuscated.
        separator (str): The separator used to split fields in the log line.

    Returns:
        str: The obfuscated log message with specified
        fields replaced by the redaction string.
    """
    pattern = '|'.join([f'{field}=[^\\{separator}]*' for field in fields])
    return sub(pattern, lambda x: f"{x.group().split('=')[0]}={redaction}",
               message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class for filtering log messages """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize RedactingFormatter with fields to be obfuscated.

        Args:
            fields (List[str]): List of field names
            to be obfuscated in log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, filtering sensitive fields.

        Args:
            record (logging.LogRecord): The log record to format and filter.

        Returns:
            str: The formatted and filtered log message.
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super().format(record)
