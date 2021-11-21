from pydantic import BaseModel
from model.company_model import CompanyModel
from model.job_channel_model import JobChannelModel
from typing import Optional


class JobModel(BaseModel):
    id: str
    title: str
    category: str  # job category like, accountant, software developer
    status: Optional[str] = "closed" # job status - closed, opened
    contract_type: Optional[str] = "unAvailable" # full time, contractual, part time and so on
    salary: Optional[str] = "unAvailable"
    available_positions: Optional[int] = 1
    tags: Optional[list] = []
    description: str
    apply_via: str  # telegram, phone number, email, link
    apply_link: str  # the value of apply via, for example if apply_via is phone number -> apply_link will be phone number
    company: CompanyModel
    job_channel: JobChannelModel
    approved: bool
    deleted: bool
    raw_post: Optional[str] = "unAvailable"
    first_modified: str
    last_modified: str

    @staticmethod
    def to_model(job_channel_json):
        return JobModel(
            id=job_channel_json["id"],
            title=job_channel_json["title"],
            category=job_channel_json["category"],
            status=job_channel_json["status"],
            contract_type=job_channel_json["contractType"],
            salary=job_channel_json["salary"],
            available_positions=job_channel_json["availablePositions"],
            tags=job_channel_json["tags"],
            description=job_channel_json["description"],
            apply_via=job_channel_json["applyVia"],
            apply_link=job_channel_json["applyLink"],
            company=CompanyModel.to_model(job_channel_json["company"]),
            job_channel=CompanyModel.to_model(job_channel_json["jobChannel"]),
            approved=job_channel_json["approved"],
            deleted=job_channel_json["deleted"],
            raw_post=job_channel_json["rawPost"],
            first_modified=job_channel_json["firstModified"],
            last_modified=job_channel_json["lastModified"]
        )

    def to_json(self):
        load = {
            "id": self.id,
            "title": self.title,
            "category": self.category,
            "status": self.status,
            "contractType": self.contract_type,
            "salary": self.salary,
            "availablePositions": self.available_positions,
            "tags": self.tags,
            "description": self.description,
            "applyVia": self.apply_via,
            "applyLink": self.apply_link,
            "company": self.company.to_json(),
            "jobChannel": self.job_channel.to_json(),
            "approved": self.approved,
            "deleted": self.deleted,
            "rawPost": self.raw_post,
            "firstModified": self.first_modified,
            "lastModified": self.last_modified
        }

        return load
