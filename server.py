import asyncio
import websockets
import json

async def hello(websocket, path):
    message = await websocket.recv()
    data = json.loads (message)
    sender = data['sender']
    receiver = data['receiver']
    message = data['message']
    
    print(sender, receiver, message)

    greeting = "Hello!"

    await websocket.send(greeting)
    # print(f"> {greeting}")

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()