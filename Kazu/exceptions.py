# Kazu - UserBot
# Copyright (C) 2021-2022 ionmusic
#
# This file is a part of < https://github.com/ionmusic/Kazu-Ubot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/ionmusic/Kazu-Ubot/blob/main/LICENSE/>.

"""
Exceptions which can be raised by Kazu Itself.
"""


class KazuError(Exception):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(KazuError):
    ...
