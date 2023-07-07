import backoff
import aiohttp


class Client:
    def __init__(self) -> None:
        self.session = aiohttp.ClientSession()

    @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=5)
    async def request(self, method: str, url: str, headers: dict = None, data: dict = None):
        async with self.session.request(method, url, headers=headers, data=data) as response:
            return await response.text()

    async def close(self):
        await self.session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
