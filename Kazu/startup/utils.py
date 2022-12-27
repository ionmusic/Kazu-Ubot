# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

from importlib import util
from sys import modules

# for addons


def load_addons(plugin_name):
    base_name = plugin_name.split("/")[-1].split("\\")[-1].replace(".py", "")
    if base_name.startswith("__"):
        return
    from .. import HNDLR, LOGS, asst, udB, kazu_bot
    from .._misc import _supporter as xxx
    from Kazu import fns
    from .._misc._assistant import asst_cmd, callback, in_pattern
    from .._misc._decorators import kazu_cmd
    from .._misc._supporter import Config, admin_cmd, sudo_cmd
    from .._misc._wrappers import eod, eor
    from ..configs import Var
    from ..dB._core import HELP

    name = plugin_name.replace("/", ".").replace("\\", ".").replace(".py","")
    spec = util.spec_from_file_location(name, plugin_name)
    mod = util.module_from_spec(spec)
    mod.LOG_CHANNEL = udB.get_key("LOG_CHANNEL")
    mod.udB = udB
    mod.asst = asst
    mod.tgbot = asst
    mod.kazu_bot = kazu_bot
    mod.ub = kazu_bot
    mod.bot = kazu_bot
    mod.kazu = kazu_bot
    mod.borg = kazu_bot
    mod.telebot = kazu_bot
    mod.jarvis = kazu_bot
    mod.friday = kazu_bot
    mod.eod = eod
    mod.edit_delete = eod
    mod.LOGS = LOGS
    mod.in_pattern = in_pattern
    mod.hndlr = HNDLR
    mod.handler = HNDLR
    mod.HNDLR = HNDLR
    mod.CMD_HNDLR = HNDLR
    mod.Config = Config
    mod.Var = Var
    mod.eor = eor
    mod.edit_or_reply = eor
    mod.asst_cmd = asst_cmd
    mod.kazu_cmd = kazu_cmd
    mod.on_cmd = kazu_cmd
    mod.callback = callback
    mod.Redis = udB.get_key
    mod.admin_cmd = admin_cmd
    mod.sudo_cmd = sudo_cmd
    mod.HELP = HELP.get("Addons", {})
    mod.CMD_HELP = HELP.get("Addons", {})
    modules["ub"] = xxx
    modules["var"] = xxx
    modules["support"] = xxx
    modules["userbot"] = xxx
    modules["telebot"] = xxx
    modules["fridaybot"] = xxx
    modules["uniborg.util"] = xxx
    modules["telebot.utils"] = xxx
    modules["userbot.utils"] = xxx
    modules["userbot.events"] = xxx
    modules["userbot.config"] = xxx
    modules["fridaybot.utils"] = xxx
    modules["fridaybot.Config"] = xxx
    modules["userbot.uniborgConfig"] = xxx
    modules["Kazu.functions"] = fns
    spec.loader.exec_module(mod)
    modules[name] = mod
    doc = modules[name].__doc__.format(i=HNDLR) if modules[name].__doc__ else ""
    if "Addons" in HELP.keys():
        update_cmd = HELP["Addons"]
        try:
            update_cmd.update({base_name: doc})
        except BaseException:
            pass
    else:
        try:
            HELP.update({"Addons": {base_name: doc}})
        except BaseException as em:
            pass
