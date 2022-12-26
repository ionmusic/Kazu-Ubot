# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
◈ Perintah Tersedia

• `{i}tagall`
    Tandai 100 Anggota Obrolan Teratas.

• `{i}tagadmins`
    Tandai Admin obrolan itu.

• `{i}tagowner`
    Tandai Pemilik obrolan itu

• `{i}tagbots`
    Tandai Bot dari obrolan itu.

• `{i}tagrec`
    Tandai Anggota Aktif baru-baru ini.

• `{i}tagon`
    Tandai Anggota online (berfungsi hanya jika privasi tidak aktif).

• `{i}tagoff`
    Tandai Anggota Offline (berfungsi hanya jika privasi tidak aktif).
"""

from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.tl.types import ChannelParticipantCreator as owner
from telethon.tl.types import UserStatusOffline as off
from telethon.tl.types import UserStatusOnline as onn
from telethon.tl.types import UserStatusRecently as rec

from . import inline_mention, kazu_cmd


@kazu_cmd(
    pattern="tag(on|off|all|bots|rec|admins|owner)( (.*)|$)",
    groups_only=True,
)
async def _(e):
    okk = e.text
    lll = e.pattern_match.group(2)
    o = 0
    nn = 0
    rece = 0
    xx = f"{lll}" if lll else ""
    lili = await e.client.get_participants(e.chat_id, limit=99)
    for bb in lili:
        x = bb.status
        y = bb.participant
        if isinstance(x, onn):
            o += 1
            if "on" in okk:
                xx += f"\n{inline_mention(bb)}"
        elif isinstance(x, off):
            nn += 1
            if "off" in okk and not bb.bot and not bb.deleted:
                xx += f"\n{inline_mention(bb)}"
        elif isinstance(x, rec):
            rece += 1
            if "rec" in okk and not bb.bot and not bb.deleted:
                xx += f"\n{inline_mention(bb)}"
        if isinstance(y, owner):
            xx += f"\n◈{inline_mention(bb)}"
        if isinstance(y, admin) and "admin" in okk and not bb.deleted:
            xx += f"\n{inline_mention(bb)}"
        if "all" in okk and not bb.bot and not bb.deleted:
            xx += f"\n{inline_mention(bb)}"
        if "bot" in okk and bb.bot:
            xx += f"\n{inline_mention(bb)}"
    await e.eor(xx)
