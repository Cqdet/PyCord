import websockets
import json
import asyncio
from threading import Timer


def set_interval(func, time):
    Timer(time, func).run()


class WebsocketManager:
    async def init_ws(self, token: str):
        async with websockets.connect('wss://gateway.discord.gg/?v=6&encoding=json') as websocket:
            

wsm = WebsocketManager()
init = wsm.init_ws('')
asyncio.get_event_loop().run_until_complete(init)
asyncio.get_event_loop().run_forever()


