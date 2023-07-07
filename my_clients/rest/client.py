import aiohttp
import backoff


class Client:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.session = aiohttp.ClientSession()
        return cls._instance

    @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=5)
    async def request(self, method: str, url: str, headers: dict = None, data: dict = None):
        async with self.session.request(method, url, headers=headers, data=data) as response:
            return await response.json()

    async def close(self):
        if self.session is not None and not self.session.closed:
            await self.session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
