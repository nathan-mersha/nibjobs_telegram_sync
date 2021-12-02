from lib.job_channel import JobChannelMethods
from model.company_model import CompanyModel
import re


class EthioDailyVacancy(JobChannelMethods):
    job_channel_id = "dGFrypUuBpEpAibnVqnt"

    # returns true if the message is a "product post" type post, false other wise
    def is_post_job(self, message: str):
        return "How to Apply".lower() in message.lower() or "ደሞዝ".lower() in message.lower()

    # checks if the product is out of stock
    def is_job_closed(self, message: str):
        return "- closed -" in message.lower()

    def deEmojify(self, message: str):
        return message.encode('ascii', 'ignore').decode('ascii')

    def extract_job_title(self, message: str):
        message=self.deEmojify(message)
        return message.partition('\n')[0].strip()

    def extract_job_contract_type(self, message: str):
        message=self.deEmojify(message)
        matches = re.findall('job type: .*', message.lower())
        if len(matches) == 0:
            return "unAvailable"
        return matches[0].replace("job type:", "").strip()

    def extract_job_salary(self, message: str):
        message=self.deEmojify(message)
        salary = "unAvailable"
        matches = re.findall('salary: .*', message.lower())
        if len(matches) > 0:
            salary = matches[0].replace("salary", "").strip()

        if "unpaid" in message.lower() or "un paid" in message.lower():
            salary = "unpaid"

        if "salary: negotiable" in message.lower():
            salary = "negotiable"

        return salary

    def extract_job_available_positions(self, message: str):
        return 1

    def extract_job_description(self, message: str):
        message=self.deEmojify(message)
        return message.lower() \
            .replace("https://ethiopage.com/jobs", "") \
            .replace("ሌሎች የስራ ማስታወቂያዎችን ዌብሳይቱ ላይ ማግኘት ትችላላችሁ", "") \
            .replace("ሌሎች ስራ መረጃዎችን ለማግኘት ይህንን ሊንክ ይጫኑት", "") \
            .replace("https://t.me/joinchat/AAAAAErPpgYpd5Yl8CBg8g", "") \
            .replace("#other", "") \
            .replace("#software", "") \
            .strip()

    def extract_job_apply_via(self, message: str):
        return "link"

    def extract_job_apply_link(self, message: str):
        return self.post.reply_markup.rows[0].buttons[0].url

    def extract_job_company(self, message: str):
        message = self.deEmojify(message)
        return CompanyModel(name=message.partition('\n')[1].strip().replace("#",""), verified=False)

    def extract_job_channel(self, message: str):
        return self.job_channel

    def extract_job_status_approved(self, message: str):
        return False

    def extract_job_status_deleted(self, message: str):
        return False
