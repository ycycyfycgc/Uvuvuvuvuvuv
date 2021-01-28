from telethon.errors import FloodWaitError
from telethon import TelegramClient,functions
from datetime import datetime
import pytz
import aiocron
import asyncio

api_id = "2175226"
api_hash="9ca53b1316986d8974f5d53c87a46933"

client=TelegramClient("session name", api_id, api_hash)

@aiocron.crontab('*/1 * * * *')
async def clock():
	ir=pytz.timezone("Asia/Tehran")
	time=datetime.now(ir).strftime("%H⏐%M :)")
	font1="1234567890"
	font2="➊➋➌➍➎➏➐➑➒⓿"
	await client(functions.account.UpdateProfileRequest(last_name=time.translate(time.maketrans(font1,font2))))

client.start()
clock.start()
client.run_until_disconnected()
asyncio.get_event_loop().run_forever()
