import asyncio
import websockets
import json
from datetime import datetime

# Configuración del servidor WebSocket
PORT = 8765
IP = "localhost"

def timestamp():
    """Genera una marca de tiempo con microsegundos."""
    return datetime.now().strftime("[%H:%M:%S.%f]")

async def test_client():
    uri = f"ws://{IP}:{PORT}"

    async with websockets.connect(uri) as websocket:
        print(f"{timestamp()} Conectado al servidor WebSocket")

        # Mensaje de suscripción al evento del jugador
        subscribe_message_health = {
            "type": "PlayerEvent",
            "action": "subscribe",
            "event": "PlayerHealthChangeEvent",
            "playerUUID": "ab406b11-d454-462f-927d-f5b41573cd43"
        }

        subscribe_message_position = {
            "type": "PlayerEvent",
            "action": "subscribe",
            "event": "PlayerPositionChangeEvent",
            "playerUUID": "ab406b11-d454-462f-927d-f5b41573cd43"
        }

        await websocket.send(json.dumps(subscribe_message_health))
        print(f"{timestamp()} CLIENTE ->\n{json.dumps(subscribe_message_health, indent=2)}")

        await websocket.send(json.dumps(subscribe_message_position))
        print(f"{timestamp()} CLIENTE ->\n{json.dumps(subscribe_message_position, indent=2)}")

        try:
            # Escuchar mensajes entrantes del servidor
            async for message in websocket:
                print(f"{timestamp()} SERVIDOR -> {json.dumps(message, indent=2)}")
        except websockets.ConnectionClosed:
            print(f"{timestamp()} [Conexión cerrada]")

if __name__ == "__main__":
    asyncio.run(test_client())
