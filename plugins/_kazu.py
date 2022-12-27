# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, kazu_cmd, eor, get_string

REPOMSG = """
◈ **ᴋᴀᴢᴜ ᴜʙᴏᴛ​** ◈\n
◈ Repo - [Click Here](https://github.com/ionmusic/Kazu-Ubot)
◈ Addons - [Click Here](https://github.com/ionmusic/addons)
◈ Support - @kazusupportgrp
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/ionmusic/Kazu-Ubot"),
        Button.url("Addons", "https://github.com/ionmusic/Addons"),
    ],
    [Button.url("Support Group", "t.me/kazusupportgrp")],
]

KAZUSTRING = """🎇 **Thanks for Deploying ᴋᴀᴢᴜ ᴜʙᴏᴛ!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@kazu_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@kazu_cmd(pattern="kazu$")
async def useAyra(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        KAZUSTRING,
        file="https://telegra.ph/file/e2f568b76280fadc8ee54.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
