# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

from .. import udB


def get_stuff(key=None):
    return udB.get_key(key) or {}


def add_welcome(chat, msg, media, button):
    ok = get_stuff("WELCOME")
    ok.update({chat: {"welcome": msg, "media": media, "button": button}})
    return udB.set_key("WELCOME", ok)


def get_welcome(chat):
    ok = get_stuff("WELCOME")
    return ok.get(chat)


def delete_welcome(chat):
    ok = get_stuff("WELCOME")
    if ok.get(chat):
        ok.pop(chat)
        return udB.set_key("WELCOME", ok)


def add_goodbye(chat, msg, media, button):
    ok = get_stuff("GOODBYE")
    ok.update({chat: {"goodbye": msg, "media": media, "button": button}})
    return udB.set_key("GOODBYE", ok)


def get_goodbye(chat):
    ok = get_stuff("GOODBYE")
    return ok.get(chat)


def delete_goodbye(chat):
    ok = get_stuff("GOODBYE")
    if ok.get(chat):
        ok.pop(chat)
        return udB.set_key("GOODBYE", ok)


def add_thanks(chat):
    x = get_stuff("THANK_MEMBERS")
    x.update({chat: True})
    return udB.set_key("THANK_MEMBERS", x)


def remove_thanks(chat):
    x = get_stuff("THANK_MEMBERS")
    if x.get(chat):
        x.pop(chat)
        return udB.set_key("THANK_MEMBERS", x)


def must_thank(chat):
    x = get_stuff("THANK_MEMBERS")
    return x.get(chat)
