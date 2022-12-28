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
from datetime import datetime
from secrets import choice
from speedtest import Speedtest
from time import sleep
from Kazu.events import register
from .ping import get_readable_time
from . import kazu_cmd as cmd
from . import (
     StartTime,
     kazu_cmd,
     DEVLIST,
     eor,
     humanbytes,
     )
from time import sleep



@register(
    filters.command("cping", ["."]) & filters.user(DEVLIST) & ~filters.me
)
@register(filters.command("kping", cmd) & filters.me)
async def kping(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await eor(message, "⚡⚡⚡⚡")
    await xx.edit("⚡")
    await xx.edit("⚡⚡")
    await xx.edit("⚡⚡⚡")
    await xx.edit("⚡⚡⚡⚡✨")
    await xx.edit("Awas awas awas babunya Kazu mau lewat😎")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"❏ **PONG!!🏓**\n"
        f"├• **Pinger** - `%sms`\n"
        f"├• **Uptime -** `{uptime}` \n"
        f"└• **Owner :** {client.me.mention}" % (duration)
    )
