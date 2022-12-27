# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
◈ Perintah Tersedia

• `{i} startvc`
    Mulai Panggilan Grup dalam grup.

• `{i} stopvc`
    Hentikan Panggilan Grup dalam grup.

• `{i} vctitle <title>`
    Ubah judul Panggilan grup.

• `{i} vcinvite`
    Undang semua anggota grup di Group Call.
    (Anda harus bergabung)
    
• `{i} joinvc` <chat id/username grup>
   Bergabunglah dengan obrolan suara.

• `{i} leavevc` <chat id/username grup>
   Tinggalkan obrolan suara.

"""

import asyncio

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from . import kazu_cmd, vc_asst, owner_and_sudos, get_string, udB, inline_mention, add_to_queue, mediainfo, file_download, LOGS, is_url_ok, bash, download, Player, VC_QUEUE, list_queue, CLIENTS,VIDEO_ON, vid_download, dl_playlist


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@kazu_cmd(
    pattern="stopvc$",
    admins_only=True,
    groups_only=True,
)
async def _(e):
    try:
        await e.client(stopvc(await get_call(e)))
        await e.eor(get_string("vct_4"))
    except Exception as ex:
        await e.eor(f"`{ex}`")


@kazu_cmd(
    pattern="vcinvite$",
    groups_only=True,
)
async def _(e):
    ok = await e.eor(get_string("vct_3"))
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await ok.edit(get_string("vct_5").format(z))


@kazu_cmd(
    pattern="startvc$",
    admins_only=True,
    groups_only=True,
)
async def _(e):
    try:
        await e.client(startvc(e.chat_id))
        await e.eor(get_string("vct_1"))
    except Exception as ex:
        await e.eor(f"`{ex}`")


@kazu_cmd(
    pattern="vctitle(?: |$)(.*)",
    admins_only=True,
    groups_only=True,
)
async def _(e):
    title = e.pattern_match.group(1).strip()
    if not title:
        return await e.eor(get_string("vct_6"), time=5)
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await e.eor(get_string("vct_2").format(title))
    except Exception as ex:
        await e.eor(f"`{ex}`")
        
        
@vc_asst("joinvc")
async def join_(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("vcbot_2").format(str(e)))
    else:
        chat = event.chat_id
    aySongs = Player(chat, event)
    await asyncio.sleep(1)
    await aySongs.group_call.set_pause(False)
    await asyncio.sleep(1)
    await aySongs.group_call.set_pause(True)
    if not aySongs.group_call.is_connected:
        await aySongs.vc_joiner()


@vc_asst("(end|leavevc)")
async def leaver(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("vcbot_2").format(str(e)))
    else:
        chat = event.chat_id
    aySongs = Player(chat)
    await aySongs.group_call.stop()
    if CLIENTS.get(chat):
        del CLIENTS[chat]
    if VIDEO_ON.get(chat):
        del VIDEO_ON[chat]
    await event.eor(get_string("vcbot_1"))
