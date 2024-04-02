import asyncio
import logging
import sys

from django.core.management.base import BaseCommand

from apps.bot.bot.main import start_bot


class Command(BaseCommand):
    help = 'Just a command for launching a Telegram bot.'

    def handle(self, *args, **kwargs):
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(start_bot())