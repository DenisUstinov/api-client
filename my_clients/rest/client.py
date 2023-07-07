import logging
import backoff
import aiohttp


class RequestError(Exception):
    def __init__(self, message, url=None, method=None, request_body=None):
        super().__init__(message)
        self.url = url
        self.method = method
        self.request_body = request_body


class Client:
    def __init__(self) -> None:
        self.session = aiohttp.ClientSession()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.ERROR)
        self.file_handler = logging.FileHandler('errors.log')
        self.file_handler.setLevel(logging.ERROR)
        self.logger.addHandler(self.file_handler)

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
