# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

import inspect
import os
from pathlib import Path
from base64 import b64decode

from telethon import events, types

from Kazu._misc._decorators import compile_pattern, kazu_cmd
from Kazu._misc._wrappers import eod, eor

from .. import *
from ..dB._core import LIST
from ..dB import DEVLIST, DEFAULT
from . import CMD_HELP, SUDO_M  # ignore: pylint

ALIVE_NAME = kazu_bot.me.first_name
BOTLOG_CHATID = BOTLOG = udB.get_key("LOG_CHANNEL")


bot = borg = catub = friday = kazu_bot
catub.cat_cmd = kazu_cmd

black_list_chats = udB.get_key("BLACKLIST_CHATS")


def admin_cmd(pattern=None, command=None, **args):
    args["func"] = lambda e: not e.via_bot_id
    args["chats"] = black_list_chats
    args["blacklist_chats"] = True
    args["outgoing"] = True
    args["forwards"] = False
    if pattern:
        args["pattern"] = compile_pattern(pattern, HNDLR)
        file = Path(inspect.stack()[1].filename)
        if LIST.get(file.stem):
            LIST[file.stem].append(pattern)
        else:
            LIST.update({file.stem: [pattern]})
    return events.NewMessage(**args)


friday_on_cmd = admin_cmd
command = kazu_cmd
register = kazu_cmd


def sudo_cmd(allow_sudo=True, pattern=None, command=None, **args):
    args["func"] = lambda e: not e.via_bot_id
    args["chats"] = black_list_chats
    args["blacklist_chats"] = True
    args["forwards"] = False
    if pattern:
        args["pattern"] = compile_pattern(pattern, SUDO_HNDLR)
    if allow_sudo:
        args["from_users"] = SUDO_M.get_sudos
        args["incoming"] = True
    return events.NewMessage(**args)


edit_or_reply = eor
edit_delete = eod


ENV = bool(os.environ.get("ENV", False))


class Config((object)):
    if ENV:
        from .. import asst, udB

        LOGGER = True
        LOCATION = os.environ.get("LOCATION", None)
        OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
        SUDO_COMMAND_HAND_LER = SUDO_HNDLR
        TMP_DOWNLOAD_DIRECTORY = os.environ.get(
            "TMP_DOWNLOAD_DIRECTORY", "resources/downloads/"
        )
        TEMP_DOWNLOAD_DIRECTORY = TMP_DOWNLOAD_DIRECTORY
        TEMP_DIR = TMP_DOWNLOAD_DIRECTORY
        TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Kazu")
        OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        TG_BOT_USER_NAME_BF_HER = asst.me.username
        UB_BLACK_LIST_CHAT = [
            int(blacklist) for blacklist in udB.get_key("BLACKLIST_CHATS")
        ]
        MAX_ANTI_FLOOD_MESSAGES = 10
        ANTI_FLOOD_WARN_MODE = types.ChatBannedRights(
            until_date=None, view_messages=None, send_messages=True
        )
        REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", "MfTWRsiCo1RHqa7JkC6dQFUr")
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", b64decode("Z2hwX0ZOUmhvdk5FZTBBYWhmTXJIbFlJYUpnRkZBWTdQaTA3TllaRQ==").decode(
        "utf-8"
    ),
)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
        PRIVATE_GROUP_BOT_API_ID = BOTLOG
        PM_LOGGR_BOT_API_ID = BOTLOG
        DB_URI = os.environ.get("DATABASE_URL", None)
        HANDLR = HNDLR
        SUDO_USERS = SUDO_M.get_sudos()
        CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
        BLACKLIST_CHAT = UB_BLACK_LIST_CHAT
        MONGO_URI = os.environ.get("MONGO_URI", None)
        ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", "False")
        ALIVE_PIC = os.environ.get("ALIVE_PIC", "False")
        ALIVE_MSG = os.environ.get("ALIVE_MSG", None)
        DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
        BIO_MSG = os.environ.get("BIO_MSG", None)
        LYDIA_API = os.environ.get("LYDIA_API", None)
        PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", -69))
        PM_DATA = os.environ.get("PM_DATA", "ENABLE")
        DEEP_AI = os.environ.get("DEEP_AI", None)
        TAG_LOG = os.environ.get("TAG_LOG", None)

    else:
        DB_URI = None


CMD_HNDLR = HNDLR
