# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.


from .. import udB


def get_chats():
    return udB.get_key("FORCESUB") or {}


def add_forcesub(chat_id, chattojoin):
    omk = get_chats()
    omk.update({chat_id: chattojoin})
    return udB.set_key("FORCESUB", omk)


def get_forcesetting(chat_id):
    omk = get_chats()
    if chat_id in omk.keys():
        return omk[chat_id]


def rem_forcesub(chat_id):
    omk = get_chats()
    if chat_id in omk.keys():
        try:
            del omk[chat_id]
            return udB.set_key("FORCESUB", omk)
        except KeyError:
            return False
