import asyncio
import websockets


def main():
    async def echo(websocket, path):
        async for message in websocket:
            print(message)
            await websocket.send('hello' + message)

    start_server = websockets.serve(
        echo, "0.0.0.0", 8111)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    main()
