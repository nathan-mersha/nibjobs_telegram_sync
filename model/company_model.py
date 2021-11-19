from pydantic import BaseModel
from typing import Optional


class CompanyModel(BaseModel):
    id: Optional[str] = "unAvailable"
    name: Optional[str] = "unAvailable"
    rank: Optional[int] = 1
    category: Optional[str] = "unAvailable"
    primary_phone: Optional[str] = "unAvailable"
    secondary_phone: Optional[str] = "unAvailable"
    email: Optional[str] = "unAvailable"
    verified: Optional[bool] = False
    website: Optional[str] = "unAvailable"
    physical_address: Optional[str] = "unAvailable"
    no_of_employees: Optional[int] = "unAvailable"
    description: Optional[str] = "unAvailable"
    logo: Optional[str] = "unAvailable"
    first_modified: Optional[str] = "2020-06-10T11:25:42.000Z"
    last_modified: Optional[str] = "2020-06-10T11:25:42.000Z"

    @staticmethod
    def to_model(job_channel_json):
        return CompanyModel(
            id=job_channel_json["id"],
            name=job_channel_json["name"],
            rank=job_channel_json["rank"],
            category=job_channel_json["category"],
            primary_phone=job_channel_json["primaryPhone"],
            secondary_phone=job_channel_json["secondaryPhone"],
            email=job_channel_json["email"],
            verified=job_channel_json["verified"],
            website=job_channel_json["website"],
            physical_address=job_channel_json["physicalAddress"],
            no_of_employees=job_channel_json["noOfEmployees"],
            description=job_channel_json["description"],
            logo=job_channel_json["logo"],
            first_modified=job_channel_json["firstModified"],
            last_modified=job_channel_json["lastModified"]
        )

    def to_json(self):
        load = {
            "id": self.id,
            "name": self.name,
            "rank": self.rank,
            "category": self.category,
            "primaryPhone": self.primary_phone,
            "secondaryPhone": self.secondary_phone,
            "email": self.email,
            "verified": self.verified,
            "website": self.website,
            "physicalAddress": self.physical_address,
            "noOfEmployees": self.no_of_employees,
            "description": self.description,
            "logo": self.logo,
            "firstModified": self.first_modified,
            "lastModified": self.last_modified
        }

        return load
