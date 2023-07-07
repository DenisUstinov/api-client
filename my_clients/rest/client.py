import logging
import backoff
import aiohttp

from my_clients import RequestError
from my_clients import setup_logger


class Client:
    def __init__(self) -> None:
        self.session = aiohttp.ClientSession()
        self.logger = setup_logger(__name__, 'errors.log')

    @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=5)
    async def request(self, method: str, url: str, headers: dict = None, data: dict = None):
        try:
            async with self.session.request(method, url, headers=headers, data=data) as response:
                return await response.text()
        except aiohttp.ClientError as e:
            self.logger.exception('Error fetching URL')
            raise RequestError('Error fetching URL', url=url, method=method, request_body=data) from e

    async def close(self):
        await self.session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
