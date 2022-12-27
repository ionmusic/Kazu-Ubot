# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
◈ Perintah Tersedia

• `{i}gban <reply user/ username>`

• `{i}ungban`
    Ban/Unban Globally.

• `{i}gstat <reply to user/userid/username>`
   apakahPeriksa pengguna GBanned.

• `{i}listgban` : List all GBanned users.

• `{i}gmute` | `{i}ungmute` <reply user/ username>
    Mute/UnMute Globally.

• `{i}gkick <reply/username>` `Globally Kick User`

• `{i}gcast <text/reply>` `Globally Send msg in all grps`

• `{i}gadmincast <text/reply>` `Globally broadcast in your admin chats`

• `{i}gucast <text/reply>` `Globally send msg in all pm users`

• `{i}gblacklist <chat id/username/nothing (for current chat)`
   Tambahkan obrolan ke daftar hitam dan abaikan siaran global.
   
• `{i}ungblacklist` `Remove the chat from blacklist.`

• `{i}gpromote <reply to user> <channel/group/all> <rank>`
    promosikan pengguna secara global di mana Anda adalah admin

• `{i}gdemote` - `demote user globally`
"""
import asyncio
import os

from telethon.errors.rpcerrorlist import ChatAdminRequiredError, FloodWaitError
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import ChatAdminRights, User

from Kazu.dB import DEVLIST
from Kazu.dB.gban_mute_db import (
    gban,
    gmute,
    is_gbanned,
    is_gmuted,
    list_gbanned,
    ungban,
    ungmute,
)
from Kazu.dB.gcast_blacklist_db import (
    add_gblacklist,
    is_gblacklisted,
    rem_gblacklist,
)
from Kazu.fns.tools import create_tl_btn, format_btn, get_msg_button

from . import (
    HNDLR,
    LOGS,
    NOSPAM_CHAT,
    OWNER_NAME,
    eod,
    eor,
    get_string,
    inline_mention,
    kazu_bot,
    kazu_cmd,
)
from ._inline import something

_gpromote_rights = ChatAdminRights(
    add_admins=False,
    invite_users=True,
    change_info=False,
    ban_users=True,
    delete_messages=True,
    pin_messages=True,
)

_gdemote_rights = ChatAdminRights(
    add_admins=False,
    invite_users=False,
    change_info=False,
    ban_users=False,
    delete_messages=False,
    pin_messages=False,
)


@kazu_cmd(pattern="gpromote( (.*)|$)", fullsudo=True)
async def _(e):
    x = e.pattern_match.group(1).strip()
    kazu_bot = e.client
    if not x:
        return await e.eor(get_string("schdl_2"), time=5)
    user = await e.get_reply_message()
    if user:
        ev = await e.eor("`Mempromosikan Pengguna yang Dibalas Secara Global`")
        ok = e.text.split()
        key = "all"
        if len(ok) > 1 and (("group" in ok[1]) or ("channel" in ok[1])):
            key = ok[1]
        rank = ok[2] if len(ok) > 2 else "AdMin"
        c = 0
        user.id = user.peer_id.user_id if e.is_private else user.from_id.user_id
        async for x in e.client.iter_dialogs():
            if (
                "group" in key.lower()
                and x.is_group
                or "group" not in key.lower()
                and "channel" in key.lower()
                and x.is_channel
            ):
                try:
                    await e.client(
                        EditAdminRequest(
                            x.id,
                            user.id,
                            _gpromote_rights,
                            rank,
                        ),
                    )
                    c += 1
                except BaseException:
                    pass
            elif (
                ("group" not in key.lower() or x.is_group)
                and (
                    "group" in key.lower()
                    or "channel" not in key.lower()
                    or x.is_channel
                )
                and (
                    "group" in key.lower()
                    or "channel" in key.lower()
                    or x.is_group
                    or x.is_channel
                )
            ):
                try:
                    await e.client(
                        EditAdminRequest(
                            x.id,
                            user.id,
                            _gpromote_rights,
                            rank,
                        ),
                    )
                    c += 1
                except Exception as er:
                    LOGS.info(er)
        await eor(ev, f"Mempromosikan Pengguna yang Dibalas secara Total : {c} {key} chats")
    else:
        k = e.text.split()
        if not k[1]:
            return await eor(
                e, "`Berikan nama pengguna/id seseorang atau balas ke pengguna.", time=5
            )
        user = k[1]
        if user.isdigit():
            user = int(user)
        try:
            name = await e.client.get_entity(user)
        except BaseException:
            return await e.eor(f"`Tidak Ada Pengguna Ditemukan Terkait {user}`", time=5)
        ev = await e.eor(f"`Mempromosikan {name.first_name} globally.`")
        key = "all"
        if len(k) > 2 and (("group" in k[2]) or ("channel" in k[2])):
            key = k[2]
        rank = k[3] if len(k) > 3 else "AdMin"
        c = 0
        async for x in e.client.iter_dialogs():
            if (
                "group" in key.lower()
                and x.is_group
                or "group" not in key.lower()
                and "channel" in key.lower()
                and x.is_channel
                or "group" not in key.lower()
                and "channel" not in key.lower()
                and (x.is_group or x.is_channel)
            ):
                try:
                    await kazu_bot(
                        EditAdminRequest(
                            x.id,
                            user,
                            _gpromote_rights,
                            rank,
                        ),
                    )
                    c += 1
                except BaseException:
                    pass
        await eor(ev, f"Dipromosikan {name.first_name} secara keseluruhan : {c} {key} obrolan.")


@kazu_cmd(pattern="gdemote( (.*)|$)", fullsudo=True)
async def _(e):
    x = e.pattern_match.group(1).strip()
    kazu_bot = e.client
    if not x:
        return await e.eor(get_string("schdl_2"), time=5)
    user = await e.get_reply_message()
    if user:
        user.id = user.peer_id.user_id if e.is_private else user.from_id.user_id
        ev = await e.eor("`Demoting Balasan Pengguna Secara Global`")
        ok = e.text.split()
        key = "all"
        if len(ok) > 1 and (("group" in ok[1]) or ("channel" in ok[1])):
            key = ok[1]
        rank = "Not AdMin"
        c = 0
        async for x in e.client.iter_dialogs():
            if (
                "group" in key.lower()
                and x.is_group
                or "group" not in key.lower()
                and "channel" in key.lower()
                and x.is_channel
                or "group" not in key.lower()
                and "channel" not in key.lower()
                and (x.is_group or x.is_channel)
            ):
                try:
                    await kazu_bot(
                        EditAdminRequest(
                            x.id,
                            user.id,
                            _gdemote_rights,
                            rank,
                        ),
                    )
                    c += 1
                except BaseException:
                    pass
        await eor(ev, f"Diturunkan Total Pengguna yang Dibalas : {c} {key} chats")
    else:
        k = e.text.split()
        if not k[1]:
            return await eor(
                e, "`Berikan nama pengguna/id seseorang atau balas ke pengguna.", time=5
            )
        user = k[1]
        if user.isdigit():
            user = int(user)
        try:
            name = await kazu_bot.get_entity(user)
        except BaseException:
            return await e.eor(f"`Tidak Ada Pengguna Ditemukan Terkait {user}`", time=5)
        ev = await e.eor(f"`Demoting {name.first_name} globally.`")
        key = "all"
        if len(k) > 2 and (("group" in k[2]) or ("channel" in k[2])):
            key = k[2]
        rank = "Not AdMin"
        c = 0
        async for x in kazu_bot.iter_dialogs():
            if (
                "group" in key.lower()
                and x.is_group
                or "group" not in key.lower()
                and "channel" in key.lower()
                and x.is_channel
                or "group" not in key.lower()
                and "channel" not in key.lower()
                and (x.is_group or x.is_channel)
            ):
                try:
                    await kazu_bot(
                        EditAdminRequest(
                            x.id,
                            user,
                            _gdemote_rights,
                            rank,
                        ),
                    )
                    c += 1
                except BaseException:
                    pass
        await eor(ev, f"Demoted {name.first_name} in Total : {c} {key} chats.")


@kazu_cmd(pattern="ungban( (.*)|$)", fullsudo=True)
async def _(e):
    xx = await e.eor("`UnGbanning...`")
    match = e.pattern_match.group(1).strip()
    peer = None
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif match:
        try:
            userid = int(match)
        except ValueError:
            userid = match
        try:
            userid = (await e.client.get_entity(userid)).id
        except Exception as er:
            return await xx.edit(f"Gagal mendapatkan Pengguna...\nError: {er}")
    elif e.is_private:
        userid = e.chat_id
    else:
        return await xx.eor("`Balas beberapa pesan atau tambahkan id mereka.`", time=5)
    if not is_gbanned(userid):
        return await xx.edit("`Pengguna/Saluran tidak di-Gban...`")
    try:
        if not peer:
            peer = await e.client.get_entity(userid)
        name = inline_mention(peer)
    except BaseException:
        userid = int(userid)
        name = str(userid)
    chats = 0
    if e.client._dialogs:
        dialog = e.client._dialogs
    else:
        dialog = await e.client.get_dialogs()
        e.client._dialogs.extend(dialog)
    for ggban in dialog:
        if ggban.is_group or ggban.is_channel:
            try:
                await e.client.edit_permissions(ggban.id, userid, view_messages=True)
                chats += 1
            except FloodWaitError as fw:
                LOGS.info(
                    f"[FLOOD_WAIT_ERROR] : on Ungban\nSleeping for {fw.seconds+10}"
                )
                await asyncio.sleep(fw.seconds + 10)
                try:
                    await e.client.edit_permissions(
                        ggban.id, userid, view_messages=True
                    )
                    chats += 1
                except BaseException as er:
                    LOGS.exception(er)
            except (ChatAdminRequiredError, ValueError):
                pass
            except BaseException as er:
                LOGS.exception(er)
    ungban(userid)
    if isinstance(peer, User):
        await e.client(UnblockRequest(userid))
    await xx.edit(
        f"`Ungbaned` {name} in {chats} `chats.\nRemoved from gbanwatch.`",
    )


@kazu_cmd(pattern="gban( (.*)|$)", fullsudo=True)
async def _(e):
    xx = await e.eor("`Gbanning...`")
    reason = ""
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
        try:
            reason = e.text.split(" ", maxsplit=1)[1]
        except IndexError:
            pass
    elif e.pattern_match.group(1).strip():
        usr = e.text.split(maxsplit=2)[1]
        try:
            userid = await e.client.parse_id(usr)
        except ValueError:
            userid = usr
        try:
            reason = e.text.split(maxsplit=2)[2]
        except IndexError:
            pass
    elif e.is_private:
        userid = e.chat_id
        try:
            reason = e.text.split(" ", maxsplit=1)[1]
        except IndexError:
            pass
    else:
        return await xx.eor("`Balas beberapa pesan atau tambahkan id mereka.`", time=5)
    user = None
    try:
        user = await e.client.get_entity(userid)
        name = inline_mention(user)
    except BaseException:
        userid = int(userid)
        name = str(userid)
    chats = 0
    if userid == kazu_bot.uid:
        return await xx.eor("`Aku tidak bisa membohongi diriku sendiri.`", time=3)
    elif userid in DEVLIST:
        return await xx.eor("`Saya tidak dapat melakukan gban pada Pengembang saya.`", time=3)
    elif is_gbanned(userid):
        return await eod(
            xx,
            "`Pengguna sudah di-gban dan ditambahkan ke gbanwatch.`",
            time=4,
        )
    if e.client._dialogs:
        dialog = e.client._dialogs
    else:
        dialog = await e.client.get_dialogs()
        e.client._dialogs.extend(dialog)
    for ggban in dialog:
        if ggban.is_group or ggban.is_channel:
            try:
                await e.client.edit_permissions(ggban.id, userid, view_messages=False)
                chats += 1
            except FloodWaitError as fw:
                LOGS.info(
                    f"[FLOOD_WAIT_ERROR] : on GBAN Command\nSleeping for {fw.seconds+10}"
                )
                await asyncio.sleep(fw.seconds + 10)
                try:
                    await e.client.edit_permissions(
                        ggban.id, userid, view_messages=False
                    )
                    chats += 1
                except BaseException as er:
                    LOGS.exception(er)
            except (ChatAdminRequiredError, ValueError):
                pass
            except BaseException as er:
                LOGS.exception(er)
    gban(userid, reason)
    if isinstance(user, User):
        await e.client(BlockRequest(userid))
    gb_msg = f"**#Gbanned** {name} `in {chats} chats and added to gbanwatch!`"
    if reason:
        gb_msg += f"\n**Reason** : {reason}"
    await xx.edit(gb_msg)


@kazu_cmd(pattern="g(admin|)cast( (.*)|$)", fullsudo=False)
async def gcast(event):
    text, btn, reply = "", None, None
    if xx := event.pattern_match.group(2):
        msg, btn = get_msg_button(event.text.split(maxsplit=1)[1])
    elif event.is_reply:
        reply = await event.get_reply_message()
        msg = reply.text
        if reply.buttons:
            btn = format_btn(reply.buttons)
        else:
            msg, btn = get_msg_button(msg)
    else:
        return await eor(
            event, "`Berikan beberapa teks ke Globally Broadcast atau balas pesan..`"
        )

    kk = await event.eor("`Sebentar Kalo Limit Jangan Salahin Gua...`")
    er = 0
    done = 0
    err = ""
    if event.client._dialogs:
        dialog = event.client._dialogs
    else:
        dialog = await event.client.get_dialogs()
        event.client._dialogs.extend(dialog)
    for x in dialog:
        if x.is_group:
            chat = x.entity.id
            if (
                not is_gblacklisted(chat)
                and int(f"-100{str(chat)}") not in NOSPAM_CHAT
                and (
                    (
                        event.text[2:7] != "admin"
                        or (x.entity.admin_rights or x.entity.creator)
                    )
                )
            ):
                try:
                    if btn:
                        bt = create_tl_btn(btn)
                        await something(
                            event,
                            msg,
                            reply.media if reply else None,
                            bt,
                            chat=chat,
                            reply=False,
                        )
                    else:
                        await event.client.send_message(
                            chat, msg, file=reply.media if reply else None
                        )
                    done += 1
                except FloodWaitError as fw:
                    await asyncio.sleep(fw.seconds + 10)
                    try:
                        if btn:
                            bt = create_tl_btn(btn)
                            await something(
                                event,
                                msg,
                                reply.media if reply else None,
                                bt,
                                chat=chat,
                                reply=False,
                            )
                        else:
                            await event.client.send_message(
                                chat, msg, file=reply.media if reply else None
                            )
                        done += 1
                    except Exception as rr:
                        err += f"• {rr}\n"
                        er += 1
                except BaseException as h:
                    err += f"• {str(h)}" + "\n"
                    er += 1
    text += f"Berhasil di {done} obrolan, kesalahan {er} obrolan(s)"
    if err != "":
        open("gcast-error.log", "w+").write(err)
        text += f"\Anda dapat melakukan `{HNDLR}kazu gcast-error.log` untuk mengetahui laporan kesalahan."
    await kk.edit(text)


@kazu_cmd(pattern="gucast( (.*)|$)", fullsudo=True)
async def gucast(event):
    msg, btn, reply = "", None, None
    if xx := event.pattern_match.group(1).strip():
        msg, btn = get_msg_button(event.text.split(maxsplit=1)[1])
    elif event.is_reply:
        reply = await event.get_reply_message()
        msg = reply.text
        if reply.buttons:
            btn = format_btn(reply.buttons)
        else:
            msg, btn = get_msg_button(msg)
    else:
        return await eor(
            event, "`Berikan beberapa teks ke Globally Broadcast atau balas pesan..`"
        )
    kk = await event.eor("`Sebentar Kalo Limit Jangan Salahin Gua...`")
    er = 0
    done = 0
    if event.client._dialogs:
        dialog = event.client._dialogs
    else:
        dialog = await event.client.get_dialogs()
        event.client._dialogs.extend(dialog)
    for x in dialog:
        if x.is_user and not x.entity.bot:
            chat = x.id
            if not is_gblacklisted(chat):
                try:
                    if btn:
                        bt = create_tl_btn(btn)
                        await something(
                            event,
                            msg,
                            reply.media if reply else None,
                            bt,
                            chat=chat,
                            reply=False,
                        )
                    else:
                        await event.client.send_message(
                            chat, msg, file=reply.media if reply else None
                        )
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(f"Berhasil di {done} obrolan, kesalahan {er} obrolan(s)")


@kazu_cmd(pattern="gkick( (.*)|$)", fullsudo=True)
async def gkick(e):
    xx = await e.eor("`Gkicking...`")
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1).strip():
        userid = await e.client.parse_id(e.pattern_match.group(1).strip())
    elif e.is_private:
        userid = e.chat_id
    else:
        return await xx.edit("`Balas beberapa pesan atau tambahkan id mereka.`", time=5)
    name = (await e.client.get_entity(userid)).first_name
    chats = 0
    if userid == kazu_bot.uid:
        return await xx.eor("`I can't gkick myself.`", time=3)
    if userid in DEVLIST:
        return await xx.eor("`I can't gkick my Developers.`", time=3)
    if e.client._dialogs:
        dialog = e.client._dialogs
    else:
        dialog = await e.client.get_dialogs()
        e.client._dialogs.extend(dialog)
    for gkick in dialog:
        if gkick.is_group or gkick.is_channel:
            try:
                await e.client.kick_participant(gkick.id, userid)
                chats += 1
            except BaseException:
                pass
    await xx.edit(f"`Gkicked` [{name}](tg://user?id={userid}) `in {chats} chats.`")


@kazu_cmd(pattern="gmute( (.*)|$)", fullsudo=True)
async def _(e):
    xx = await e.eor("`Gmuting...`")
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1).strip():
        userid = await e.client.parse_id(e.pattern_match.group(1).strip())
    elif e.is_private:
        userid = e.chat_id
    else:
        return await xx.eor("`Balas beberapa pesan atau tambahkan id mereka.`", tome=5, time=5)
    name = await e.client.get_entity(userid)
    chats = 0
    if userid == kazu_bot.uid:
        return await xx.eor("`I can't gmute myself.`", time=3)
    if userid in DEVLIST:
        return await xx.eor("`I can't gmute my Developers.`", time=3)
    if is_gmuted(userid):
        return await xx.eor("`User is already gmuted.`", time=4)
    if e.client._dialogs:
        dialog = e.client._dialogs
    else:
        dialog = await e.client.get_dialogs()
        e.client._dialogs.extend(dialog)
    for onmute in dialog:
        if onmute.is_group:
            try:
                await e.client.edit_permissions(onmute.id, userid, send_messages=False)
                chats += 1
            except BaseException:
                pass
    gmute(userid)
    await xx.edit(f"`Gmuted` {inline_mention(name)} `in {chats} chats.`")


@kazu_cmd(pattern="ungmute( (.*)|$)", fullsudo=True)
async def _(e):
    xx = await e.eor("`UnGmuting...`")
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1).strip():
        userid = await e.client.parse_id(e.pattern_match.group(1).strip())
    elif e.is_private:
        userid = e.chat_id
    else:
        return await xx.eor("`Balas beberapa pesan atau tambahkan id mereka.`", time=5)
    name = (await e.client.get_entity(userid)).first_name
    chats = 0
    if not is_gmuted(userid):
        return await xx.eor("`User is not gmuted.`", time=3)
    if e.client._dialogs:
        dialog = e.client._dialogs
    else:
        dialog = await e.client.get_dialogs()
        e.client._dialogs.extend(dialog)
    for hurr in dialog:
        if hurr.is_group:
            try:
                await e.client.edit_permissions(hurr.id, userid, send_messages=True)
                chats += 1
            except BaseException:
                pass
    ungmute(userid)
    await xx.edit(f"`Ungmuted` {inline_mention(name)} `in {chats} chats.`")


@kazu_cmd(
    pattern="listgban$",
)
async def list_gengbanned(event):
    users = list_gbanned()
    x = await event.eor(get_string("com_1"))
    msg = ""
    if not users:
        return await x.edit("`You haven't GBanned anyone!`")
    for i in users:
        try:
            name = await event.client.get_entity(int(i))
        except BaseException:
            name = i
        msg += f"<strong>User</strong>: {inline_mention(name, html=True)}\n"
        reason = users[i]
        msg += f"<strong>Reason</strong>: {reason}\n\n" if reason is not None else "\n"
    gbanned_users = f"<strong>List of users GBanned by {OWNER_NAME}</strong>:\n\n{msg}"
    if len(gbanned_users) > 4096:
        with open("gbanned.txt", "w") as f:
            f.write(
                gbanned_users.replace("<strong>", "")
                .replace("</strong>", "")
                .replace("<a href=tg://user?id=", "")
                .replace("</a>", "")
            )
        await x.reply(
            file="gbanned.txt",
            message=f"List of users GBanned by {inline_mention(kazu_bot.me)}",
        )
        os.remove("gbanned.txt")
        await x.delete()
    else:
        await x.edit(gbanned_users, parse_mode="html")


@kazu_cmd(
    pattern="gstat( (.*)|$)",
)
async def gstat_(e):
    xx = await e.eor(get_string("com_1"))
    if e.is_private:
        userid = (await e.get_chat()).id
    elif e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1).strip():
        try:
            userid = await e.client.parse_id(e.pattern_match.group(1).strip())
        except Exception as err:
            return await xx.eor(f"{err}", time=10)
    else:
        return await xx.eor("`Balas beberapa pesan atau tambahkan id mereka.`", time=5)
    name = (await e.client.get_entity(userid)).first_name
    msg = f"**{name} is "
    is_banned = is_gbanned(userid)
    reason = list_gbanned().get(userid)
    if is_banned:
        msg += "Globally Banned"
        msg += f" with reason** `{reason}`" if reason else ".**"
    else:
        msg += "not Globally Banned.**"
    await xx.edit(msg)


@kazu_cmd(pattern="gblacklist$")
async def blacklist_(event):
    await gblacker(event, "add")


@kazu_cmd(pattern="ungblacklist$")
async def ungblacker(event):
    await gblacker(event, "remove")


async def gblacker(event, type_):
    try:
        chat_id = int(event.text.split(maxsplit=1)[1])
        try:
            chat_id = (await event.client.get_entity(chat_id)).id
        except Exception as e:
            return await event.eor(f"**ERROR**\n`{str(e)}`")
    except IndexError:
        chat_id = event.chat_id
    if type_ == "add":
        add_gblacklist(chat_id)
    elif type_ == "remove":
        rem_gblacklist(chat_id)
    await event.eor(f"Global Broadcasts: \n{type_}ed {chat_id}")
