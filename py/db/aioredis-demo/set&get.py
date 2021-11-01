import asyncio
import aioredis


async def main():
    redis = await aioredis.from_url('redis://127.0.0.1:6379/0')
    await redis.set("my-key", "value")
    value = await redis.get("my-key")
    print(value)

asyncio.run(main())
