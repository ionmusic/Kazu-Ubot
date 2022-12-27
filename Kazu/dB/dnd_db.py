# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.


from .. import udB


def get_dnd_chats():
    return udB.get_key("DND_CHATS") or []


def add_dnd(chat_id):
    x = get_dnd_chats()
    x.append(int(chat_id))
    return udB.set_key("DND_CHATS", x)


def del_dnd(chat_id):
    x = get_dnd_chats()
    x.remove(int(chat_id))
    return udB.set_key("DND_CHATS", x)


def chat_in_dnd(chat_id):
    return int(chat_id) in get_dnd_chats()
