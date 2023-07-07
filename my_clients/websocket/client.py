import backoff
import websockets
import websockets.exceptions

from typing import Dict, Any, Callable, Coroutine


class Client:
    def __init__(self, response_handler: Callable[[dict], Coroutine]) -> None:
        self.response_handler = response_handler

    @backoff.on_exception(backoff.expo, websockets.exceptions.WebSocketException, max_tries=5)
    async def subscribe_and_listen(self, data: Dict[str, Any]) -> None:
        url = data.get('url')
        if url is None:
            raise ValueError('url is not provided')

        async with websockets.connect(url) as websocket:
            init_messages = data.get('init_messages')
            if init_messages is None:
                raise ValueError('init_messages is not provided')

            if init_messages:
                for message in init_messages:
                    await websocket.send(message)

                while True:
                    message = await websocket.recv()
                    await self.response_handler(message)
