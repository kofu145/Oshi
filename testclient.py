import asyncio
import websockets


async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()

# TODO: state handling
# TODO: wrapper around message sending and receiving
# TODO: Encryption - instead of using text frame for sending, use byte frame of encrypted data

asyncio.run(hello())
