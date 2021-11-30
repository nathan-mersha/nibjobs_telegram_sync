from lib.job_channel import JobChannelMethods
from model.company_model import CompanyModel
import re


class SiraApp(JobChannelMethods):
    job_channel_id = "ZwfexgBZaKeZ38jJ8Eth"

    # returns true if the message is a "product post" type post, false other wise
    def is_post_job(self, message: str):
        return "Education Level".lower() in message.lower()

    # checks if the product is out of stock
    def is_job_closed(self, message: str):
        return "- closed -" in message.lower()

    def extract_job_title(self, message: str):
        # matches = re.findall('job title: .*', message.lower())
        return message.partition('\n')[0].strip()

    def extract_job_contract_type(self, message: str):
        matches = re.findall('type  : .*', message.lower())
        if len(matches) == 0:
            return "unAvailable"
        return matches[0].replace("type", "").replace(":", "").strip()

    def extract_job_salary(self, message: str):
        salary = "unAvailable"
        matches = re.findall('salary - .*', message.lower())
        if len(matches) > 0:
            salary = matches[0].replace("salary -", "").strip()

        if "unpaid" in message.lower() or "un paid" in message.lower():
            salary = "unpaid"

        if "salary negotiable" in message.lower():
            salary = "negotiable"

        return salary

    def extract_job_available_positions(self, message: str):
        return 1

    def extract_job_description(self, message: str):
        reg = re.compile('.*?description:(.*)', re.DOTALL)
        matches = reg.findall(message.lower())
        return matches[0]\
            .replace("description:", "")\
            .replace("from: @freelance_ethio", "")\
            .replace("#business_services", "")\
            .replace("#creative_design", "")\
            .replace("#other", "")\
            .replace("#software", "")\
            .strip()

    def extract_job_apply_via(self, message: str):
        return "telegram"

    def extract_job_apply_link(self, message: str):
        return self.post.reply_markup.rows[0].buttons[0].url

    def extract_job_company(self, message: str):
        name = "unAvailable"
        matches = re.findall('company: .*', message.lower())

        if len(matches) > 0:
            name = matches[0].replace("company:", "").strip()

        verified = "verified" in message.lower()
        return CompanyModel(name=name, verified=verified)

    def extract_job_channel(self, message: str):
        return self.job_channel

    def extract_job_status_approved(self, message: str):
        return True

    def extract_job_status_deleted(self, message: str):
        return False


