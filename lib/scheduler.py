import datetime

from lib.global_constants import telegram_bot

from lib.job_channels.EthionlineJobs import EthoOnlineJobs
from lib.job_channels.ethio_job_vacancy import EthioJobVacancy
from lib.job_channels.ethiopian_vacancy import EthiopianVacancy
from lib.job_channels.freelance_ethiopia import FreeLanceEthiopia
from lib.job_channels.hahujobs import HaHuJobs
from lib.job_channels.jobs_in_ethiopia import JobInEthiopia
from lib.job_channels.ngo_job_vacancy import NgoJobVacancy
from lib.job_channels.post_vacancy import PostVacancy
from lib.job_channels.siraapp import SiraApp


class ShopScheduler:
    # todo : add job_channels here
    companies_sync_list = [
        FreeLanceEthiopia(),
        SiraApp(),
        HaHuJobs(),
        EthoOnlineJobs(),
        EthiopianVacancy(),
        EthioJobVacancy(),
        PostVacancy(),
        NgoJobVacancy(),
        JobInEthiopia(),
    ]

    @staticmethod
    def sync_job_channels():
        begin = datetime.datetime.now()
    
        for shop in ShopScheduler.companies_sync_list:
            shop.sync_jobs()
            
        end = datetime.datetime.now()
        diff = end - begin
        telegram_bot.notify_sync_bot("Completed NibJobs Sync, Begin approval. Took {} sec".format(diff.seconds))

