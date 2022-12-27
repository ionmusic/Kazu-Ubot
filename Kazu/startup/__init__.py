# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

import os
import platform
import sys
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger

from .. import run_as_module

if run_as_module:
    from ..configs import Var
else:
    Var = None


def where_hosted():
    if os.getenv("DYNO"):
        return "heroku"
    if os.getenv("RAILWAY_STATIC_URL"):
        return "railway"
    if os.getenv("OKTETO_TOKEN"):
        return "okteto"
    if os.getenv("KUBERNETES_PORT"):
        return "qovery | kubernetes"
    if os.getenv("RUNNER_USER") or os.getenv("HOSTNAME"):
        return "github actions"
    if os.getenv("ANDROID_ROOT"):
        return "termux"
    if os.getenv("FLY_APP_NAME"):
        return "fly.io"
    return "local"


if run_as_module:
    from telethon import __version__
    from telethon.tl.alltlobjects import LAYER

    from ..version import __version__ as __kazu__
    from ..version import kazu_version

    file = f"kazu{sys.argv[6]}.log" if len(sys.argv) > 6 else "kazu.log"

    if os.path.exists(file):
        os.remove(file)

    HOSTED_ON = where_hosted()
    LOGS = getLogger("KazuLogs")
    TelethonLogger = getLogger("Telethon")
    TelethonLogger.setLevel(INFO)

    _, v, __ = platform.python_version_tuple()

    if int(v) < 10:
        from ._extra import _fix_logging

        _fix_logging(FileHandler)

    if HOSTED_ON == "local":
        from ._extra import _ask_input

        _ask_input()

    _LOG_FORMAT = "%(asctime)s | %(name)s [%(levelname)s] : %(message)s"
    basicConfig(
        format=_LOG_FORMAT,
        level=INFO,
        datefmt="%m/%d/%Y, %H:%M:%S",
        handlers=[FileHandler(file), StreamHandler()],
    )
    try:

        import coloredlogs

        coloredlogs.install(level=None, logger=LOGS, fmt=_LOG_FORMAT)
    except ImportError:
        pass

    LOGS.info(
        """
                    -----------------------------------
                            Starting Deployment
                    -----------------------------------
    """
    )

    LOGS.info(f"Python version - {platform.python_version()}")
    LOGS.info(f"py-Kazu Version - {__kazu__}")
    LOGS.info(f"Telethon Version - {__version__} [Layer: {LAYER}]")
    LOGS.info(f"Kazu Version - {kazu_version} [{HOSTED_ON}]")

    try:
        from safety.tools import *
    except ImportError:
        LOGS.error("'safety' package not found!")
