import asyncio
import websockets

PORT = 8765
IP = "localhost"

async def test_client():
    uri = f"ws://{IP}:{PORT}"

    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server")

        # Send a test message
        await websocket.send("Hello server!")

        # Listen for incoming messages
        try:
            async for message in websocket:
                print(f"Received message: {message}")
        except websockets.ConnectionClosed:
            print("Connection closed")

if __name__ == "__main__":
    asyncio.run(test_client())
