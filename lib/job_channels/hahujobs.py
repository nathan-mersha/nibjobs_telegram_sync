from lib.job_channel import JobChannelMethods
from model.company_model import CompanyModel
import re


class HaHuJobs(JobChannelMethods):
    job_channel_id = "x13fDIe5FucLpezt0GDk"

    # returns true if the message is a "product post" type post, false other wise
    def is_post_job(self, message: str):
        return "How To Apply".lower() in message.lower()

    # checks if the product is out of stock
    def is_job_closed(self, message: str):
        return "- closed -" in message.lower()

    def extract_job_title(self, message: str):
        return message.partition('\n')[0].strip()

    def extract_job_contract_type(self, message: str):
        matches = re.findall('job type: .*', message.lower())
        if len(matches) == 0:
            return "unAvailable"
        return matches[0].replace("job type:", "").strip()

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
        return message.lower()\
            .replace("@hahujobs @hahujobs_bot", "")\
            .replace("@hahujobs", "")\
            .replace("@hahujobs_bot", "")\
            .replace("#creative_design", "")\
            .replace("#other", "")\
            .replace("#software", "")\
            .strip()

    def extract_job_apply_via(self, message: str):
        return "link"

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
        return False

    def extract_job_status_deleted(self, message: str):
        return False

