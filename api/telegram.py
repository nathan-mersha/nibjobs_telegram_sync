import configparser

from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.sync import TelegramClient


class TelegramChannel:
    # Get history request constants
    OFFSET_DATE = None
    OFFSET_ID = 0
    MAX_ID = 0
    MIN_ID = 0
    ADD_OFFSET = 0
    HASH = 0
    LIMIT = 30 # todo : change to 100

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
        messages = []
        if not self.client.is_connected():
            self.connect_client()
        try:
            posts = self.client(GetHistoryRequest(
                peer=shop_telegram_channel,
                limit=self.LIMIT,
                offset_date=self.OFFSET_DATE,
                offset_id=self.OFFSET_ID,
                max_id=self.MAX_ID,
                min_id=self.MIN_ID,
                add_offset=0,
                hash=self.HASH)
            )
            messages = posts.messages + messages
        except Exception as e:
            print(e)
        print(f"messages length : {len(messages)}")
        return messages

    # def get_posts(self, shop_telegram_channel: str):
    #
    #     limit = 30
    #     messages = []
    #     index = 0
    #     while index * 30 <= limit:
    #         if not self.client.is_connected():
    #             self.connect_client()
    #         try:
    #             posts = self.client(GetHistoryRequest(
    #                 peer=shop_telegram_channel,
    #                 limit=self.LIMIT,
    #                 offset_date=self.OFFSET_DATE,
    #                 offset_id=self.OFFSET_ID,
    #                 max_id=self.MAX_ID,
    #                 min_id=self.MIN_ID,
    #                 add_offset=0,
    #                 hash=self.HASH)
    #             )
    #             messages = posts.messages + messages
    #             index += 1
    #         except Exception as e:
    #             print(e)
    #
    #     print(f"Posts length : {len(messages)}")
    #     return messages

    def download_media(self, post):
        try:
            print(post.media.photo) # dont delete this print message
            cached_media_path = self.client.download_media(post.media, self.config['Telegram']['image_cache_path'])
        except Exception as e:
            cached_media_path = "None"

        return cached_media_path
