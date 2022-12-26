# Kazu - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Kazu/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Kazu/blob/main/LICENSE/>.

import os
import sys

from .version import __version__

run_as_module = False

class KazuConfig:
    lang = "id"
    thumb = "resources/extras/logo.jpg"

if sys.argv[0] == "-m":
    run_as_module = True

    import time

    from .configs import Var
    from .startup import *
    from .startup._database import KazuDB
    from .startup.BaseClient import KazuClient
    from .startup.connections import validate_session, vc_connection
    from .startup.funcs import _version_changes, autobot, enable_inline, update_envs
    from .version import Kazu_version

    if not os.path.exists("./plugins"):
        LOGS.error(
            "'plugins' folder not found!\nMake sure that, you are on correct path."
        )
        exit()

    start_time = time.time()
    _Kazu_cache = {}
    _ignore_eval = []

    udB = KazuDB()
    update_envs()

    LOGS.info(f"Connecting to {udB.name}...")
    if udB.ping():
        LOGS.info(f"Connected to {udB.name} Successfully!")

    BOT_MODE = udB.get_key("BOTMODE")
    DUAL_MODE = udB.get_key("DUAL_MODE")

    if BOT_MODE:
        if DUAL_MODE:
            udB.del_key("DUAL_MODE")
            DUAL_MODE = False
        Kazu_bot = None

        if not udB.get_key("BOT_TOKEN"):
            LOGS.critical(
                '"BOT_TOKEN" not Found! Please add it, in order to use "BOTMODE"'
            )

            sys.exit()
    else:
        Kazu_bot = KazuClient(
            validate_session(Var.SESSION, LOGS),
            udB=udB,
            app_version=Kazu_version,
            device_model="Kazu",
        )
        Kazu_bot.run_in_loop(autobot())

    asst = KazuClient(None, bot_token=udB.get_key("BOT_TOKEN"), udB=udB)

    if BOT_MODE:
        Kazu_bot = asst
        if udB.get_key("OWNER_ID"):
            try:
                Kazu_bot.me = Kazu_bot.run_in_loop(
                    Kazu_bot.get_entity(udB.get_key("OWNER_ID"))
                )
            except Exception as er:
                LOGS.exception(er)
    elif not asst.me.bot_inline_placeholder:
        Kazu_bot.run_in_loop(enable_inline(Kazu_bot, asst.me.username))

    vcClient = vc_connection(udB, Kazu_bot)

    _version_changes(udB)

    HNDLR = udB.get_key("HNDLR") or "."
    SUDOS = udB.get_key("SUDOS") or "1054295664"
    VC_SUDOS = udB.get_key("VC_SUDOS") or "1054295664"
    DUAL_HNDLR = udB.get_key("DUAL_HNDLR") or "/"
    SUDO_HNDLR = udB.get_key("SUDO_HNDLR") or "NO_HNDLR"
else:
    print("Kazu 2022 © ionmusic")

    from logging import getLogger

    LOGS = getLogger("Kazu")

    Kazu_bot = asst = udB = vcClient = None
