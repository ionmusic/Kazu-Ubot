# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

import sys
import os

from decouple import config

try:
    from dotenv import load_dotenv
    
    load_dotenv()
except ImportError:
    pass

if os.environ.get("HEROKU_API"):
    from heroku3 import from_key

    heroku_api = os.environ.get("HEROKU_API")
    heroku_app_name = os.environ.get("HEROKU_APP_NAME")
    heroku_conn = from_key(heroku_api)
    heroku_app = heroku_conn.apps()[heroku_app_name]
    heroku_config = heroku_app.config()

    redis_url = os.environ.get("REDISCLOUD_URL")
    if redis_url and redis_url.startswith("redis://"):
        redis_url = redis_url.replace("redis://", "", 1)
        redis_uri_password, redis_host = redis_url.split("@")
        redis_uri, redis_password = redis_uri_password.split(":")

        heroku_config["REDIS_URI"] = redis_host
        heroku_config["REDIS_PASSWORD"] = redis_password


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default=6, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default=None)
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", default=None)
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=None) or config("REDIS_URL", default=None))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default=None)
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    SUDO = config("SUDO", default=True, cast=bool)
    VC_SESSION = config("VC_SESSION", default=SESSION)
    ADDONS = config("ADDONS", default=True, cast=bool)
    INLINE_PIC = config("INLINE_PIC", default=False, cast=bool)
    VCBOT = config("VCBOT", default=True, cast=bool)
    PMSETTING = config("PMSETTING", default=True, cast=bool)
    PMWARNS = config("PMWARNS", "3")
    DISABLE_PMDEL = config("DISABLE_PMDEL", default=True, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default=None)
