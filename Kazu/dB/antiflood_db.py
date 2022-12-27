# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.


from .. import udB


def get_flood():
    return udB.get_key("ANTIFLOOD") or {}


def set_flood(chat_id, limit):
    omk = get_flood()
    omk.update({chat_id: limit})
    return udB.set_key("ANTIFLOOD", omk)


def get_flood_limit(chat_id):
    omk = get_flood()
    if chat_id in omk.keys():
        return omk[chat_id]


def rem_flood(chat_id):
    omk = get_flood()
    if chat_id in omk.keys():
        del omk[chat_id]
        return udB.set_key("ANTIFLOOD", omk)
