# Copyright (C) 2019 The Raphielscape Company LLC.

#

# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot module for managing events. One of the main components of the userkazu_bot."""

import inspect
import re
import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from pathlib import Path
from time import gmtime, strftime
from traceback import format_exc

from telethon import events

from Kazu import kazu_bot
from Kazu._misc._supporter import CMD_HNDLR, CMD_HELP
from Kazu.dB import DEFAULT, DEVLIST


def babu_cmd(pattern=None, command=None, **args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    args.get("allow_sudo", False)
    if pattern is not None:
        if pattern.startswith(r"\#"):
            args["pattern"] = re.compile(pattern)
        elif pattern.startswith(r"^"):
            args["pattern"] = re.compile(pattern)
            cmd = pattern.replace("$", "").replace("^", "").replace("\\", "")
            try:
                CMD_HELP[file_test].append(cmd)
            except BaseException:
                CMD_HELP.update({file_test: [cmd]})
        else:
            if len(CMD_HNDLR) == 2:
                catreg = "^" + CMD_HNDLR
                reg = CMD_HNDLR[1]
            elif len(CMD_HNDLR) == 1:
                catreg = "^\\" + CMD_HNDLR
                reg = CMD_HNDLR
            args["pattern"] = re.compile(catreg + pattern)
            if command is not None:
                cmd = reg + command
            else:
                cmd = (
                    (reg + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                CMD_HELP[file_test].append(cmd)
            except BaseException:
                CMD_HELP.update({file_test: [cmd]})

    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        del args["allow_edited_updates"]

    return events.NewMessage(**args)


def command(**args):
    args["func"] = lambda e: e.via_bot_id is None

    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    pattern = args.get("pattern")
    allow_edited_updates = args.get("allow_edited_updates", False)
    args["incoming"] = args.get("incoming", False)
    args["outgoing"] = True
    if bool(args["incoming"]):
        args["outgoing"] = False

    try:
        if pattern is not None and not pattern.startswith("(?i)"):
            args["pattern"] = "(?i)" + pattern
    except BaseException:
        pass

    reg = re.compile("(.*)")
    if pattern is not None:
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except BaseException:
                pass
            try:
                CMD_HELP[file_test].append(cmd)
            except BaseException:
                CMD_HELP.update({file_test: [cmd]})
        except BaseException:
            pass

    def decorator(func):
        async def wrapper(check):
            if check.edit_date and check.is_channel and not check.is_group:
                return

        if allow_edited_updates:
            kazu_bot.add_event_handler(func, events.MessageEdited(**args))
        kazu_bot.add_event_handler(func, events.NewMessage(**args))

    return decorator


def devs_cmd(**args):
    pattern = args.get("pattern")
    disable_edited = args.get("disable_edited", False)
    ignore_unsafe = args.get("ignore_unsafe", False)
    unsafe_pattern = r"^[^/!#@\$A-Za-z]"
    args.get("groups_only", False)
    disable_errors = args.get("disable_errors", False)
    insecure = args.get("insecure", False)
    args.get("sudo", False)
    args.get("own", False)

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    if "disable_edited" in args:
        del args["disable_edited"]

    if "sudo" in args:
        del args["sudo"]
        args["incoming"] = True
        args["from_users"] = DEVLIST

    if "ignore_unsafe" in args:
        del args["ignore_unsafe"]

    if "groups_only" in args:
        del args["groups_only"]

    if "disable_errors" in args:
        del args["disable_errors"]

    if "own" in args:
        del args["own"]
        args["incoming"] = True
        args["from_users"] = DEFAULT

    if "insecure" in args:
        del args["insecure"]

    if pattern and not ignore_unsafe:
        args["pattern"] = pattern.replace("^.", unsafe_pattern, 1)

    def decorator(func):
        async def wrapper(check):
            if check.edit_date and check.is_channel and not check.is_group:
                # Messages sent in channels can be edited by other users.
                # Ignore edits that take place in channels.
                return

            if check.via_bot_id and not insecure and check.out:
                return

            try:
                await func(check)

            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException:
                # Check if we have to disable it.
                # If not silence the log spam on the console,
                # with a dumb except.

                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    text = "**✘ KAZU-UBOT ERROR REPORT ✘**\n\n"
                    link = "[Group Support](https://t.me/kazusupportgrp)"
                    text += "Jika mau, Anda bisa melaporkan error ini, "
                    text += f"Cukup forward saja pesan ini ke {link}.\n\n"

                    ftext = "========== DISCLAIMER =========="
                    ftext += "\nFile ini HANYA diupload di sini,"
                    ftext += "\nkami hanya mencatat fakta error dan tanggal,"
                    ftext += "\nkami menghormati privasi Anda."
                    ftext += "\nJika mau, Anda bisa melaporkan error ini,"
                    ftext += "\ncukup forward saja pesan ini ke @kazusupportgrp"
                    ftext += "\n================================\n\n"
                    ftext += "--------BEGIN USERBOT TRACEBACK LOG--------\n"
                    ftext += "\nTanggal : " + date
                    ftext += "\nChat ID : " + str(check.chat_id)
                    ftext += "\nUser ID : " + str(check.sender_id)
                    ftext += "\n\nEvent Trigger:\n"
                    ftext += str(check.text)
                    ftext += "\n\nTraceback info:\n"
                    ftext += str(format_exc())
                    ftext += "\n\nError text:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"

                    command = 'git log --pretty=format:"%an: %s" -10'

                    ftext += "\n\n\n10 commits Terakhir:\n"

                    process = await asyncsubshell(
                        command, stdout=asyncsub.PIPE, stderr=asyncsub.PIPE
                    )
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) + str(stderr.decode().strip())

                    ftext += result

                    with open("error.log", "w+") as file:
                        file.write(ftext)

        if kazu_bot:
            if not disable_edited:
                kazu_bot.add_event_handler(wrapper, events.MessageEdited(**args))
            kazu_bot.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper

    return decorator
