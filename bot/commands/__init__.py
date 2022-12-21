__all__ = ["register_user_commands", "bot_commands"]

from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.filters import Command
from aiogram import F

from bot.commands.start import start
from bot.commands.help import help_commands


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help_commands, Command(commands=["help"]))
    router.message.register(start, F.text == "Старт")
