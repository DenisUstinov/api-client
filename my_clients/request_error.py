from typing import Any


class RequestError(Exception):
    """Exception raised for request errors.

    Attributes:
        message (str): The error message.
        url (str): The URL that caused the error.
        method (str): The request method.
        request_body (Any): The request body.
    """

    def __init__(self, message: str, url: str = None, method: str = None, request_body: Any = None):
        super().__init__(message)
        self.url = url
        self.method = method
        self.request_body = request_body
