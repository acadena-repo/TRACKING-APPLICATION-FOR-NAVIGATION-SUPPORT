import asyncio
from datetime import datetime
import pandas as pd

HOST = '127.0.0.1'
PORT = 7932
route = pd.read_csv("ROUTE2.csv")
segments = route.shape[0] - 1

tracker = {'count': -1, 'execute': datetime.now()}


async def client_handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    request = None
    addr = writer.get_extra_info("peername")

    # Send initial pose at connection established
    idx = tracker["count"]
    X, Y, alfa = route.iloc[idx].to_dict().values()
    pose = f"{X} {Y} {alfa}"
    writer.write(pose.encode())
    await writer.drain()

    while request := await reader.read(1024):
        text = request.decode()
        print(f"Message from {addr!r}: {text!r}")
        idx = tracker["count"]
        X, Y, alfa = route.iloc[idx].to_dict().values()
        # echo = f"Absolute X:{X} - Y:{Y} - alfa:{alfa}"
        pose = f"{X} {Y} {alfa}"
        if text == "quit\n":
            writer.write(text.encode())
        else:
            writer.write(pose.encode())
        await writer.drain()

        if text == "quit\n":
            break

    print(f"Connection with {addr!r} closed .....")
    writer.close()
    await writer.wait_closed()


async def main():
    loop = asyncio.get_running_loop()

    def rate():
        tracker['count'] += 1
        tracker['execute'] = datetime.now()
        if tracker['count'] > segments:
            tracker['count'] = 0

        loop.call_later(0.125, rate)

    server = await asyncio.start_server(client_handler, HOST, PORT)
    addr = server.sockets[0].getsockname() if server.sockets else "unknown"
    print(f"Serving on {addr}")
    loop.call_soon(rate)

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server shutdown .....")
