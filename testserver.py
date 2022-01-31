import asyncio
import websockets


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


async def handler(websocket):
    await authentication_handler(websocket)

    await asyncio.gather(
        consumer_handler(websocket),
        producer_handler(websocket),
    )


async def authentication_handler(websocket):
    token = await websocket.recv()
    user = get_user(token)
    if user is None:
        await websocket.close(1011, "authentication failed")
        return


async def consumer_handler(websocket):
    async for message in websocket:
        # read message type.
        # if system message:
        # server does action with user data

        # if text message:
        # get destination stream of message, and publish it to that stream
        pass # coroutine msg handler


async def producer_handler(websocket):
    while True:
        # for every stream the user of this websocket is subbed to, send them msg
        message = "" # coroutine msg handler
        await websocket.send(message)


def get_user(token):
    # TODO: implement auth (separate file?)
    return 0


async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())
