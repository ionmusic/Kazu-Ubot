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



@register(incoming=True, from_users=DEVLIST, pattern=r"^Cping$")
async def _(xping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    message = "**㋡ 𝙺𝙰𝚉𝚄 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ㋡**\n\n㋡ **ᴘɪɴɢᴇʀ :** `{} ms`\n㋡ **ᴜᴘᴛɪᴍᴇ :** `{}`\n㋡ **ᴏᴡɴᴇʀ :** `{}`\n㋡ **ɪᴅ :** `{}`"
    await ping.reply(message.format(duration, uptime, user.first_name, user.id)
                     )
