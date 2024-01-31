#!/usr/bin/env python

import asyncio
from websockets.server import serve

async def hello(websocket):
    async for name in websocket:
        message = f"Hello, {name}"
        await websocket.send(message)

async def main():
    async with serve(hello, "localhost", 80):
        await asyncio.Future()  # run forever

asyncio.run(main())