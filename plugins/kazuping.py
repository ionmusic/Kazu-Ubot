# Kazu - Ubot
# Copyright (C) 2022-2023 @TeamKazu
#
# This file is a part of < https://github.com/ionmusic/Kazu-Ubot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/ionmusic/Kazu-Ubot/blob/main/LICENSE/>.
#
# FROM Kazu-Ubot <https://github.com/ionmusic/Kazu-Ubot >
# t.mekazusupportgrp

# ========================ร========================
#            Jangan Hapus Credit Ngentod
# ========================ร========================

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
    "**Hadir Bang** ๐",
    "**Mmuaahh** ๐",
    "**Hadir dong** ๐",
    "**Hadir ganteng** ๐ฅต",
    "**Hadir bro** ๐",
    "**Hadir kak maap telat** ๐ฅบ",
]

kazucakep = [
    "**๐๐ฎ๐ Kazu ๐๐๐ฃ๐ฉ๐๐ฃ๐ ๐ฝ๐๐ฃ๐๐๐ฉ** ๐",
    "**๐๐๐ฃ๐ฉ๐๐ฃ๐๐ฃ๐ฎ๐ ๐๐๐  ๐ผ๐๐ ๐๐๐ฌ๐๐ฃ** ๐",
    "**๐๐๐ข๐ช ๐๐๐ฃ๐ฉ๐๐ฃ๐๐ฃ๐ฎ๐ ๐ผ๐ ๐ช ๐๐๐ฃ Zu** ๐",
    "**๐๐ฎ๐๐ ๐๐๐๐ ๐๐๐ ๐จ๐๐๐ฃ๐** ๐",
    "**๐๐๐ข๐ช ๐๐๐ข๐๐ฉ ๐๐๐ฅ๐ ๐ฝ๐ค๐ค๐ฃ๐** ๐",
]

@kazu_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    message = "**ใก ๐บ๐ฐ๐๐ ๐๐๐ด๐๐ฑ๐พ๐ ใก**\n\nใก **แดษชษดษขแดส :** `{} ms`\nใก **แดแดแดษชแดแด :** `{}`\nใก **แดแดกษดแดส :** `{}`\nใก **ษชแด :** `{}`"
    await ping.reply(message.format(duration, uptime, user.first_name, user.id)
                     )

# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK ๐ก
# JANGAN DI HAPUS GOBLOK ๐ก LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA ๐ฅด GUA TANDAIN LU AKUN TELENYA ๐ก

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


# ========================ร========================
#            Jangan Hapus Credit Ngentod
# ========================ร========================
