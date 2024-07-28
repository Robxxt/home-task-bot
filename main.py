from dotenv import load_dotenv
from telegram import Bot
import os
import asyncio
import time
import sys

load_dotenv()

bewohners = ["Rt", "Fx", "Ado", "Hy"]

bot_token = os.environ.get("BOT_TOKEN")
chat_id = os.environ.get("CHANNEL_ID")

async def main():
	global bewohners
	bot = Bot(token=bot_token)
	counter = 0
	while counter < sys.maxsize:
		counter += 1
		message = f"Mothefucker {bewohners[counter % 4]} throw the trash!"
		two_days = 3600 * 24 * 2
		time.sleep(two_days)
		await bot.send_message(chat_id=chat_id, text=message)

if __name__ == "__main__":
	asyncio.run(main())
	