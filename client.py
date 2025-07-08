import asyncio
import websockets

async def test_client():
    uri = "ws://localhost:8080"  # Change the port if different

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
