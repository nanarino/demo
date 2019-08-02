import asyncio
from redis import asyncio as aioredis


async def main():
    redis = aioredis.from_url('redis://127.0.0.1:6379/0')
    await redis.set("my-key", "value")
    value: bytes = await redis.get("my-key")
    print(value)

asyncio.run(main())
