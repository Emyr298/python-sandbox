import asyncio
import websockets

async def handle_code(websocket, path):
    code = await websocket.recv()
    print("Received code:", code)

start_server = websockets.serve(handle_code, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()