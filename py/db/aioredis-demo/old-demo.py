import asyncio
import aioredis


async def main():
    """Cannot run in python311: https://github.com/dioptra-io/iris/issues/145"""
    redis = await aioredis.from_url('redis://127.0.0.1:6379/0')
    await redis.set("my-key", "value")
    value: bytes = await redis.get("my-key")
    print(value)

asyncio.run(main())
