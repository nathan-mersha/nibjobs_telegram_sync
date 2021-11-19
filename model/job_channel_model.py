from pydantic import BaseModel
from typing import Optional


class JobChannelModel(BaseModel):
    id: str
    channel_id: str
    name: str
    rank: Optional[int] = 1
    description: str
    logo: str
    link: str
    first_modified: str
    last_modified: str

    @staticmethod
    def to_model(job_channel_json):
        return JobChannelModel(
            id=job_channel_json["id"],
            channel_id=job_channel_json["channelId"],
            name=job_channel_json["name"],
            rank=job_channel_json["rank"],
            description=job_channel_json["description"],
            logo=job_channel_json["logo"],
            link=job_channel_json["link"],
            first_modified=job_channel_json["firstModified"],
            last_modified=job_channel_json["lastModified"]
        )

    def to_json(self):
        load = {
            "id": self.id,
            "channelId": self.channel_id,
            "name": self.name,
            "rank": self.rank,
            "description": self.description,
            "logo": self.logo,
            "link": self.link,
            "firstModified": self.first_modified,
            "lastModified": self.last_modified
        }

        return load
