# Ported By @disinikazu & @Riizzvbss
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# ReCode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de


import time
from datetime import datetime

from speedtest import Speedtest

from . import (
     StartTime,
     kazu_cmd,
     DEVLIST,
     eor,
     humanbytes,
     devs_cmd,
     )
from time import sleep


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@kazu_cmd(pattern=r"^pink$", incoming=True, from_users=DEVLIST)
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Cpink$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ping = await eor(ping, "**✧**")
    await ping.edit("**✧✧**")
    await ping.edit("**✧✧✧**")
    await ping.edit("**✧✧✧✧**")
    await ping.edit("**✧✧✧✧✧**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await ping.edit("⚡")
    sleep(3)
    await ping.edit(
        f"**✧ 𝙺𝙰𝚉𝚄 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**\n\n"
        f"✧ **𝙿𝙸𝙽𝙶𝙴𝚁 :** `%sms`\n"
        f"✧ **𝚄𝙿𝚃𝙸𝙼𝙴 :** `{uptime}` \n"
        f"✧ **𝙾𝚆𝙽𝙴𝚁 :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@kazu_cmd(pattern="ping$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xping = await eor(ping, "`Pinging....`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xping.edit(
        f"**PONG!! 🍭**\n**Ping** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


@kazu_cmd(pattern="lping$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Lping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    lping = await eor(ping, "**★ PING ★**")
    await lping.edit("**★★ PING ★★**")
    await lping.edit("**★★★ PING ★★★**")
    await lping.edit("**★★★★ PING ★★★★**")
    await lping.edit("**✦҈͜͡➳ PONG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await lping.edit(
        f"❃ **Ping !!** "
        f"`%sms` \n"
        f"❃ **Uptime -** "
        f"`{uptime}` \n"
        f"**✦҈͜͡➳ Master :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@kazu_cmd(pattern="keping$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Kping$")
async def _(pong):
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kopong = await eor(pong, "**『⍟𝐊𝐎𝐍𝐓𝐎𝐋』**")
    await kopong.edit("**◆◈𝐊𝐀𝐌𝐏𝐀𝐍𝐆◈◆**")
    await kopong.edit("**𝐏𝐄𝐂𝐀𝐇𝐊𝐀𝐍 𝐁𝐈𝐉𝐈 𝐊𝐀𝐔 𝐀𝐒𝐔**")
    await kopong.edit("**☬𝐒𝐈𝐀𝐏 𝐊𝐀𝐌𝐏𝐀𝐍𝐆 𝐌𝐄𝐍𝐔𝐌𝐁𝐔𝐊 𝐀𝐒𝐔☬**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await kopong.edit(
        f"**✲ 𝙺𝙾𝙽𝚃𝙾𝙻 𝙼𝙴𝙻𝙴𝙳𝚄𝙶** "
        f"\n ⫸ 𝙺𝙾𝙽𝚃𝙾𝙻 `%sms` \n"
        f"**✲ 𝙱𝙸𝙹𝙸 𝙿𝙴𝙻𝙴𝚁** "
        f"\n ⫸ 𝙺𝙰𝙼𝙿𝙰𝙽𝙶『[{user.first_name}](tg://user?id={user.id})』 \n" % (duration)
    )


# .keping & kping Coded by Koala


@kazu_cmd(pattern=r"kaz$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Kaz$")
async def _(pong):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kping = await eor(pong, "8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8==✊=D")
    await kping.edit("8=✊==D")
    await kping.edit("8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8==✊=D")
    await kping.edit("8=✊==D")
    await kping.edit("8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8===✊D💦")
    await kping.edit("8====D💦💦")
    await kping.edit("**MINGGIR MINGGIR**")
    await kping.edit("**SEMUANYA MINGGIR KAZU MAU LEWAT.....**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await kping.edit("😎")
    sleep(3)
    await kping.edit(
        f"**𝙺𝙰𝚉𝚄 𝚃𝙰𝙼𝙿𝙰𝙽!! 😎**\n**𝙿𝙸𝙽𝙶** : %sms\n**𝙱𝙾𝚃 𝚄𝙿𝚃𝙸𝙼𝙴** : {uptime}🕛" % (duration)
    )


@kazu_cmd(pattern="speedtest$")
async def _(speed):
    xxnx = await eor(speed, "`Running speed test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@kazu_cmd(pattern="pong$")
async def _(pong):
    start = datetime.now()
    xx = await eor(pong, "`Sepong`")
    await xx.edit("Sepong Sayang.....")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("🥵")
    sleep(3)
    await xx.edit("**𝙿𝙸𝙽𝙶!**\n`%sms`" % (duration))
