# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

"""
◈ Perintah Tersedia

• `{i} convert` <gif/img/stiker/webm>

• `{i} doc <filename.ext>`
     Balas pesan teks untuk menyimpannya dalam file.

• `{i} open`
     Balas file untuk mengungkapkan teksnya.

• `{i} rename <nama file dengan ekstensi>`
     Ubah nama file

• `{i} thumbnail <Balas ke file gambar/thumbnail>`
     Unggah file Anda dengan thumbnail khusus Anda
"""

import os
import time

from . import LOGS

try:
    import cv2
except ImportError:
    cv2 = None

try:
    from PIL import Image
except ImportError:
    LOGS.info(f"{__file__}: PIL  not Installed.")
    Image = None

from telegraph import upload_file as uf

from . import (
    KazuConfig,
    kazu_cmd,
    bash,
    con,
    downloader,
    get_paste,
    get_string,
    udB,
    uploader,
)

opn = []


@kazu_cmd(
    pattern="thumbnail$",
)
async def _(e):
    r = await e.get_reply_message()
    if r.photo:
        dl = await r.download_media()
    elif r.document and r.document.thumbs:
        dl = await r.download_media(thumb=-1)
    else:
        return await e.eor("`Balas ke Foto atau media dengan thumb...`")
    variable = uf(dl)
    os.remove(dl)
    nn = f"https://graph.org{variable[0]}"
    udB.set_key("CUSTOM_THUMBNAIL", str(nn))
    await bash(f"wget {nn} -O resources/extras/logo.jpg")
    await e.eor(get_string("cvt_6").format(nn), link_preview=False)


@kazu_cmd(
    pattern="rename( (.*)|$)",
)
async def imak(event):
    reply = await event.get_reply_message()
    t = time.time()
    if not reply:
        return await event.eor(get_string("cvt_1"))
    inp = event.pattern_match.group(1).strip()
    if not inp:
        return await event.eor(get_string("cvt_2"))
    xx = await event.eor(get_string("com_1"))
    if reply.media:
        if hasattr(reply.media, "document"):
            file = reply.media.document
            image = await downloader(
                reply.file.name or str(time.time()),
                reply.media.document,
                xx,
                t,
                get_string("com_5"),
            )

            file = image.name
        else:
            file = await event.client.download_media(reply.media)
    if os.path.exists(inp):
        os.remove(inp)
    await bash(f'mv """{file}""" """{inp}"""')
    if not os.path.exists(inp) or os.path.exists(inp) and not os.path.getsize(inp):
        os.rename(file, inp)
    k = time.time()
    xxx = await uploader(inp, inp, k, xx, get_string("com_6"))
    await event.reply(
        f"`{xxx.name}`",
        file=xxx,
        force_document=True,
        thumb=KazuConfig.thumb,
    )
    os.remove(inp)
    await xx.delete()


conv_keys = {
    "img": "png",
    "sticker": "webp",
    "webp": "webp",
    "image": "png",
    "webm": "webm",
    "gif": "gif",
    "json": "json",
    "tgs": "tgs",
}


@kazu_cmd(
    pattern="convert( (.*)|$)",
)
async def uconverter(event):
    xx = await event.eor(get_string("com_1"))
    a = await event.get_reply_message()
    if a is None:
        return await event.eor("`Balas ke Foto atau media dengan thumb...`")
    input_ = event.pattern_match.group(1).strip()
    b = await a.download_media("resources/downloads/")
    if not b and (a.document and a.document.thumbs):
        b = await a.download_media(thumb=-1)
    if not b:
        return await xx.edit(get_string("cvt_3"))
    try:
        convert = conv_keys[input_]
    except KeyError:
        return await xx.edit(get_string("sts_3").format("gif/img/sticker/webm"))
    file = await con.convert(b, outname="ayra", convert_to=convert)
    if file:
        await event.client.send_file(
            event.chat_id, file, reply_to=event.reply_to_msg_id or event.id
        )
        os.remove(file)
    await xx.delete()


@kazu_cmd(
    pattern="doc( (.*)|$)",
)
async def _(event):
    input_str = event.pattern_match.group(1).strip()
    if not (input_str and event.is_reply):
        return await event.eor(get_string("cvt_1"), time=5)
    xx = await event.eor(get_string("com_1"))
    a = await event.get_reply_message()
    if not a.message:
        return await xx.edit(get_string("ex_1"))
    with open(input_str, "w") as b:
        b.write(str(a.message))
    await xx.edit(f"**Pengepakan ke dalam** `{input_str}`")
    await event.reply(file=input_str, thumb=KazuConfig.thumb)
    await xx.delete()
    os.remove(input_str)


@kazu_cmd(
    pattern="open( (.*)|$)",
)
async def _(event):
    a = await event.get_reply_message()
    b = event.pattern_match.group(1).strip()
    if not ((a and a.media) or (b and os.path.exists(b))):
        return await event.eor(get_string("cvt_7"), time=5)
    xx = await event.eor(get_string("com_1"))
    rem = None
    if not b:
        b = await a.download_media()
        rem = True
    try:
        with open(b) as c:
            d = c.read()
    except UnicodeDecodeError:
        return await xx.eor(get_string("cvt_8"), time=5)
    try:
        await xx.edit(f"```{d}```")
    except BaseException:
        what, key = await get_paste(d)
        await xx.edit(
            f"**PESAN MELEBIHI BATAS TELEGRAM**\n\\Jadi Ditempelkan Di [SPACEBIN](https://spaceb.in/{key})"
        )
    if rem:
        os.remove(b)
