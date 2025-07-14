import asyncio
import websockets
import json

PORT = 8765
IP = "localhost"

async def test_client():
    uri = f"ws://{IP}:{PORT}"

    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server")

        subscribe_message = {
            "type": "PlayerEvent",
            "action": "subscribe",
            "event": "PlayerHealthChangeEvent",
            "playerUUID": "ab406b11-d454-462f-927d-f5b41573cd43"
        }

        await websocket.send(json.dumps(subscribe_message))
        print(f"CLIENT -> {json.dumps(subscribe_message, indent=2)}")

        try:
            async for message in websocket:
                print(f"SERVER -> {message}")
        except websockets.ConnectionClosed:
            print("[Connection closed]")

if __name__ == "__main__":
    asyncio.run(test_client())
