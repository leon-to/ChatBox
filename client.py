import asyncio
import websockets
import json



async def sendMessage(sender):
    async with websockets.connect('ws://localhost:8765') as websocket:
        receiver = input("To whom: ")
        message = input("What message do you wanna say?") 

        data = json.dumps({
            'sender': sender,
            'receiver': receiver,
            'message': message
        })
        
        await websocket.send(data)

        greeting = await websocket.recv()
        # print(f"< {greeting}")


sender = input("What's your name? ")

asyncio.get_event_loop().run_until_complete(sendMessage(sender))