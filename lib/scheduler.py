from lib.global_constants import telegram_bot
from lib.job_channels.freelance_ethiopia import FreeLanceEthiopia
import traceback
import datetime

from lib.job_channels.hahujobs import HaHuJobs
from lib.job_channels.siraapp import SiraApp


class ShopScheduler:
    # todo : add job_channels here
    companies_sync_list = [
        FreeLanceEthiopia(),
        SiraApp(),
        HaHuJobs(),
    ]

    @staticmethod
    def sync_job_channels():
        begin = datetime.datetime.now()
        telegram_bot.notify_sync_bot("starting sync script")

        # iterating through the above defined shop lists to sync product
        for shop in ShopScheduler.companies_sync_list:
            shop.sync_jobs()
            # try:
            #     shop.sync_jobs()
            # except Exception as e:
            #     print(e)
            #     telegram_bot.notify_sync_bot(
            #         "----- Error On Sync {} ------ \n Something Went wrong while syncing : \n {} \n ----- Error End ------".format("a",
            #                                                                                                                     str(traceback.format_exc())))
        end = datetime.datetime.now()
        diff = end - begin
        telegram_bot.notify_sync_bot("completed sync script took {} sec".format(diff.seconds))

    @staticmethod
    def sync_shop(shop_id: str):
        begin = datetime.datetime.now()
        telegram_bot.notify_sync_bot("starting sync script")

        # iterating through the above defined shop lists to sync product

        for shop in ShopScheduler.companies_sync_list:
            if shop.shop_id == shop_id:
                shop.sync_products()
                return

        end = datetime.datetime.now()
        diff = end - begin
        telegram_bot.notify_sync_bot("completed sync script took {} sec".format(diff.seconds))
