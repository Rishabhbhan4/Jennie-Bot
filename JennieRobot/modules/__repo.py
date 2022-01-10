import os
from pyrogram import Client, filters
from pyrogram.types import *

from JennieRobot.conf import get_str_key
from JennieRobot import pbot

REPO_TEXT = "**A Powerful [BOT](https://telegra.ph/Rishabh-Bhan-12-06) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [Rishabh](t.me/Rishu_05) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @LisaSupportChat «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("⚡ ʀᴇᴘᴏꜱɪᴛᴏʀʏ🔥", url=f"https://github.com/Rishabhbhan4/Jennie-Bot"),
        InlineKeyboardButton(" ᴊᴏɪɴ 💫", url=f"https://t.me/RishabhHelpBot"),
      ],[
        InlineKeyboardButton("Jennie Owner ❣️", url="https://t.me/Rishu_05"),
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ⚡", url="https://t.me/lisaSupportChat"),
      ],[
        InlineKeyboardButton("⚡ ᴜᴘᴅᴀᴛᴇꜱ ☑️", url="https://t.me/RishabhHelpBot"),
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ ➡️", url="https://t.me/Rishu_05"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
