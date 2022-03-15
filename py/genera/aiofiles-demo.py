# -*- encoding:utf-8 -*-
'''
with open('./README.md',"rb") as f:
    print(f.read())
'''
import asyncio, aiofiles
async def main():
    async with aiofiles.open('./README.md', mode='rb') as f:
        contents = await f.read()
        print(contents)

asyncio.run(main())