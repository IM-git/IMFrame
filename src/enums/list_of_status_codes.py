from enum import Enum


class StatusCodes(Enum):
    """List of common HTTP status codes"""
    CONTINUE = 100
    OK = 200
    MULTIPLE_CHOICES = 300
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
