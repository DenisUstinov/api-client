import logging

import backoff
import websockets
import websockets.exceptions

from typing import Dict, Any, Callable, Coroutine


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


class Client:
    """WebSocket client class.

    Attributes:
        response_handler (Callable[[dict], Coroutine]): The coroutine function to handle responses.
        logger (logging.Logger): The logger instance for error logging.
        file_handler (logging.FileHandler): The file handler for error log file.
    """

    def __init__(self, response_handler: Callable[[dict], Coroutine]) -> None:
        """Initialize the WebSocket client.

        Args:
            response_handler (Callable[[dict], Coroutine]): The coroutine function to handle responses.
        """
        self.response_handler = response_handler
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.ERROR)
        self.file_handler = logging.FileHandler('errors.log')
        self.file_handler.setLevel(logging.ERROR)
        self.logger.addHandler(self.file_handler)

    @backoff.on_exception(backoff.expo, websockets.exceptions.WebSocketException, max_tries=5)
    async def subscribe_and_listen(self, data: Dict[str, Any]) -> None:
        """Subscribe to a WebSocket and listen for messages.

        Args:
            data (Dict[str, Any]): The data containing the URL and optional initial messages.
        """
        try:
            url = data.get('url')
            if url is None:
                raise RequestError('URL is missing')

            async with websockets.connect(url) as websocket:
                init_messages = data.get('init_messages', [])
                for message in init_messages:
                    await websocket.send(message)

                while True:
                    message = await websocket.recv()
                    await self.response_handler(message)
        except websockets.WebSocketException as e:
            self.logger.exception('Error fetching URL')
            raise RequestError('Error fetching URL', url=url, method=None, request_body=data) from e
