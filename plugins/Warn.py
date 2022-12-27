# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
◈ Perintah Tersedia

•`{i}warn <reply to user> <reason>`
    Memberi Peringatan.

•`{i}resetwarn <reply to user>`
    Untuk mengatur ulang Semua Peringatan.

•`{i}warns <reply to user>`
   Untuk Mendapatkan Daftar Peringatan dari pengguna.

•`{i}setwarn <warn count> | <ban/mute/kick>`
   Tetapkan Angka dalam jumlah peringatan untuk peringatan
   Setelah memberi tanda " | ", beri tindakan seperti larangan/bisu/tendang
   Tendangan Default 3-nya
   Example : `setwarn 5 | mute`

"""

from Kazu.dB.warn_db import add_warn, reset_warn, warns

from . import eor, get_string, inline_mention, udB, kazu_cmd


@kazu_cmd(
    pattern="warn( (.*)|$)",
    manager=True,
    groups_only=True,
    admins_only=True,
)
async def warn(e):
    kazu_bot = e.client
    reply = await e.get_reply_message()
    if len(e.text) > 5 and " " not in e.text[5]:
        return
    if reply:
        user = reply.sender_id
        reason = e.text[5:] if e.pattern_match.group(1).strip() else "unknown"
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await kazu_bot.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await e.eor("Balas ke Pengguna", time=5)
        try:
            reason = e.text.split(maxsplit=2)[-1]
        except BaseException:
            reason = "unknown"
    count, r = warns(e.chat_id, user)
    r = f"{r}|$|{reason}" if r else reason
    try:
        x = udB.get_key("SETWARN")
        number, action = int(x.split()[0]), x.split()[1]
    except BaseException:
        number, action = 3, "kick"
    if ("ban" or "kick" or "mute") not in action:
        action = "kick"
    if count + 1 >= number:
        if "ban" in action:
            try:
                await kazu_bot.edit_permissions(e.chat_id, user, view_messages=False)
            except BaseException:
                return await e.eor("`Ada yang salah.`", time=5)
        elif "kick" in action:
            try:
                await kazu_bot.kick_participant(e.chat_id, user)
            except BaseException:
                return await e.eor("`Ada yang salah.`", time=5)
        elif "mute" in action:
            try:
                await kazu_bot.edit_permissions(
                    e.chat_id, user, until_date=None, send_messages=False
                )
            except BaseException:
                return await e.eor("`Ada yang salah.`", time=5)
        add_warn(e.chat_id, user, count + 1, r)
        c, r = warns(e.chat_id, user)
        ok = await kazu_bot.get_entity(user)
        user = inline_mention(ok)
        r = r.split("|$|")
        text = f"Pengguna {user} Mendapat {action} Karena {count+1} Peringatan.\n\n"
        for x in range(c):
            text += f"•**{x+1}.** {r[x]}\n"
        await e.eor(text)
        return reset_warn(e.chat_id, ok.id)
    add_warn(e.chat_id, user, count + 1, r)
    ok = await kazu_bot.get_entity(user)
    user = inline_mention(ok)
    await eor(
        e,
        f"**PERINGATAN :** {count+1}/{number}\n**Ke :**{user}\n**Hati-hati !!!**\n\n**Alasan** : {reason}",
    )


@kazu_cmd(
    pattern="resetwarn( (.*)|$)",
    manager=True,
    groups_only=True,
    admins_only=True,
)
async def rwarn(e):
    reply = await e.get_reply_message()
    if reply:
        user = reply.sender_id
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await e.client.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await e.eor("Balas ke pengguna")
    reset_warn(e.chat_id, user)
    ok = await e.client.get_entity(user)
    user = inline_mention(ok)
    await e.eor(f"Dihapus Semua Peringatan dari {user}.")


@kazu_cmd(
    pattern="warns( (.*)|$)",
    manager=True,
    groups_only=True,
    admins_only=True,
)
async def twarns(e):
    reply = await e.get_reply_message()
    if reply:
        user = reply.from_id.user_id
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await e.client.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await e.eor("Balas ke Pengguna", time=5)
    c, r = warns(e.chat_id, user)
    if c and r:
        ok = await e.client.get_entity(user)
        user = inline_mention(ok)
        r = r.split("|$|")
        text = f"Pengguna {user} Mendapat {c} Peringatan.\n\n"
        for x in range(c):
            text += f"•**{x+1}.** {r[x]}\n"
        await e.eor(text)
    else:
        await e.eor("`Tidak ada Peringatan`")


@kazu_cmd(pattern="setwarn( (.*)|$)", manager=True)
async def warnset(e):
    ok = e.pattern_match.group(1).strip()
    if not ok:
        return await e.eor("stuff")
    if "|" in ok:
        try:
            number, action = int(ok.split()[0]), ok.split()[1]
        except BaseException:
            return await e.eor(get_string("schdl_2"), time=5)
        if ("ban" or "kick" or "mute") not in action:
            return await e.eor("`Hanya opsi mute / ban / kick yang didukung`", time=5)
        udB.set_key("SETWARN", f"{number} {action}")
        await e.eor(f"Selesai Jumlah Peringatan Anda sekarang {number} dan Tindakan adalah {action}")
    else:
        await e.eor(get_string("schdl_2"), time=5)
