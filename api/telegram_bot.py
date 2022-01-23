import configparser
import os
from pathlib import Path
from telegram.ext import *


class TelegramBot:

    def __init__(self):
        self.config = configparser.ConfigParser()
        config_path = Path("./cred/config.ini")
        print(config_path.absolute())
        self.config.read(config_path.absolute())

        bot_token = self.config['Telegram']['bot_token_test'] if os.environ.get("MODE") == "test" else self.config['Telegram']['bot_token']
        self.updater = Updater(bot_token, use_context=True)
        dp = self.updater.dispatcher
        dp.add_handler(CommandHandler("start", self.start_command))
        dp.add_handler(CommandHandler("help", self.help_command))
        dp.add_handler(CommandHandler("sync", self.sync_command))

        self.updater.start_polling(10)

    @staticmethod
    def start_command(update, context):
        update.message.reply_text("you will receive notifications when sync is complete")

    @staticmethod
    def help_command(update, context):
        update.message.reply_text("/start - to start\n /sync - sync job_channels on command \n /help - help commands")

    @staticmethod
    def sync_command(update, context):
        update.message.reply_text("start sync command")

    def notify_sync_bot(self, message: str):
        chat_ids = ["793267544", "496930646", "1714819450"]

        for chat_id in chat_ids:
            self.updater.bot.send_message(chat_id=chat_id, text=message)
