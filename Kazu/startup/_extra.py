# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

# https://bugs.python.org/issue26789
# 'open' not defined has been fixed in Python3.10
# for other older versions, something need to be done.


def _fix_logging(handler):
    handler._builtin_open = open

    def _new_open(self):
        open_func = self._builtin_open
        return open_func(self.baseFilename, self.mode)

    setattr(handler, "_open", _new_open)


def _ask_input():
    # Ask for Input even on Vps and other platforms.
    def new_input(*args, **kwargs):
        raise EOFError("args=" + str(args) + ", kwargs=" + str(kwargs))

    __builtins__["input"] = new_input
