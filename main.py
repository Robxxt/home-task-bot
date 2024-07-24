from dotenv import load_dotenv
from telegram import Bot
import os
import asyncio

load_dotenv()

bot_token = os.environ.get("BOT_TOKEN")
chat_id = os.environ.get("CHANNEL_ID")

async def main():
	bot = Bot(token=bot_token)
	message = "Fuck you motherfuckers! I'm the mothefucker bot"
	await bot.send_message(chat_id=chat_id, text=message)

if __name__ == "__main__":
	asyncio.run(main())