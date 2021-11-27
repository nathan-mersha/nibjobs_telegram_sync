import configparser

from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.sync import TelegramClient


class GetTelegramChannel:
    # Get history request constants

    def __init__(self):
        # Reading Configs
        self.config = configparser.ConfigParser()
        self.connect_client()

    def connect_client(self):
        self.config.read("./cred/config.ini")

        # Setting configuration values
        api_id = int(self.config['Telegram']['api_id'])
        api_hash = str(self.config['Telegram']['api_hash'])
        api_hash = str(api_hash)
        username = self.config['Telegram']['username']

        self.client = TelegramClient(username, api_id, api_hash)
        self.client.start()

    def get_posts(self, shop_telegram_channel: str):
        if not self.client.is_connected():
            self.connect_client()
        try:
            posts = self.client(GetHistoryRequest(
                peer=shop_telegram_channel,
                limit=1,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0)
            )
            print(posts)
            print(posts.messages[0].reply_markup.rows[0].buttons[0].url)
            # print(posts.messages[0])
            return posts

        except Exception as e:
            print(e)


getChannel = GetTelegramChannel()
getChannel.get_posts(shop_telegram_channel = "https://t.me/freelance_ethio")
