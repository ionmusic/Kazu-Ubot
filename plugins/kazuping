# Kazu - Ubot
# Copyright (C) 2022-2023 @TeamKazu
#
# This file is a part of < https://github.com/ionmusic/Kazu-Ubot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/ionmusic/Kazu-Ubot/blob/main/LICENSE/>.
#
# FROM Kazu-Ubot <https://github.com/ionmusic/Kazu-Ubot >
# t.mekazusupportgrp

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import time
import random
import speedtest
import asyncio
from pyrogram import Client, filters
from Kazu import *
from pyrogram import Client as KazuClient
from pyrogram.raw import functions
from pyrogram.types import Message
from datetime import datetime

from .ping import get_readable_time

from . import (
        DEVLIST,
        DEFAULT,
        kazu_cmd,
        eor,
        StartTime,
        humanbytes,
        )
from time import sleep



absen = [
    "**Hadir Bang** 😁",
    "**Mmuaahh** 😉",
    "**Hadir dong** 😁",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak maap telat** 🥺",
]

kazucakep = [
    "**𝙄𝙮𝙖 Kazu 𝙂𝙖𝙣𝙩𝙚𝙣𝙜 𝘽𝙖𝙣𝙜𝙚𝙩** 😍",
    "**𝙂𝙖𝙣𝙩𝙚𝙣𝙜𝙣𝙮𝙖 𝙂𝙖𝙠 𝘼𝙙𝙖 𝙇𝙖𝙬𝙖𝙣** 😚",
    "**𝙆𝙖𝙢𝙪 𝙂𝙖𝙣𝙩𝙚𝙣𝙜𝙣𝙮𝙖 𝘼𝙠𝙪 𝙆𝙖𝙣 Zu** 😍",
    "**𝙄𝙮𝙖𝙖 𝙜𝙖𝙙𝙖 𝙖𝙙𝙖 𝙨𝙖𝙞𝙣𝙜** 😎",
    "**𝙆𝙖𝙢𝙪 𝙅𝙖𝙢𝙚𝙩 𝙏𝙖𝙥𝙞 𝘽𝙤𝙤𝙣𝙜** 😚",
]

@kazu_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    message = "**㋡ 𝙺𝙰𝚉𝚄 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ㋡**\n\n㋡ **ᴘɪɴɢᴇʀ :** `{} ms`\n㋡ **ᴜᴘᴛɪᴍᴇ :** `{}`\n㋡ **ᴏᴡɴᴇʀ :** `{}`\n㋡ **ɪᴅ :** `{}`"
    await ping.reply(message.format(duration, uptime, user.first_name, user.id)
                     )

# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
# JANGAN DI HAPUS GOBLOK 😡 LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡

# Absen by : mrismanaziz <https://github.com/mrismanaziz/man-userbot>

@kazu_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Absen$")
async def kazuabsen(ganteng):
    await ganteng.reply(choice(absen))

@KazuClient.on_message(filters.command("absen", ["."]) & filters.user(DEVLIST) & ~filters.me)
async def absen(client: Client, message: Message):
    await message.reply_text(random.choice(kopi))

@kazu_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Aku ganteng kan$")
async def kazu(ganteng):
    await ganteng.reply(choice(kazucakep))


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================
