import time
import uuid
from lib.global_constants import *
from model.job_channel_model import JobChannelModel
import os
from model.job_model import JobModel
from dateutil import parser

from datetime import datetime


class JobChannelMethods:
    unknown = "unknown"
    job_channel_id = "unknown"
    job_channel: JobChannelModel
    global_config: dict
    post: {}

    # post analyzed values
    created = "created"
    removed = "removed"
    updated = "updated"
    ignored = "ignored"
    errored = "errored"
    not_job_post = "not_job_post"
    total_analyzed = "total_analyzed"

    errored_msg = []
    not_job_post_msg = []

    def __init__(self):
        # initializing firebase admin
        self.firebase_crud = firebase_crud
        self.telegram_channel = telegram_channel
        self.assign_job_channel_data()
        self.assign_global_config_data()

    def assign_global_config_data(self):
        self.global_config = self.firebase_crud.get_global_config()

    # assigns JobChannel data from firebase
    def assign_job_channel_data(self):
        job_channel_json = self.firebase_crud.get_job_channel(shop_id=self.job_channel_id)
        self.job_channel = JobChannelModel.to_model(job_channel_json=job_channel_json)

    # returns true if the message is a "product post" type post, false other wise
    def is_post_job(self, message: str):
        pass

    # checks if the product is out of stock
    def is_job_closed(self, message: str):
        pass

    def extract_job_title(self, message: str):
        pass

    def extract_job_category(self, message: str):
        categories = self.global_config["categories"]
        for category in categories:
            tags = category["tags"]
            category["match"] = 0
            for tag in tags:
                if tag in message.lower():
                    category["match"] += 1

        candidate_category = categories[0]
        for category in categories:
            if category["match"] >= candidate_category["match"]:
                candidate_category = category

        return candidate_category["name"]

    def extract_job_contract_type(self, message: str):
        pass

    def extract_job_salary(self, message: str):
        pass

    def extract_job_available_positions(self, message: str):
        pass

    def extract_job_tag(self, message: str):
        job_tags = []
        job_category_name = self.extract_job_category(message=message)
        categories = self.global_config["categories"]
        selected_category = {}
        for category in categories:
            if category["name"] is job_category_name:
                selected_category = category

        for tag in selected_category["tags"]:
            if tag in message.lower().replace("_", " ").replace("-", " "):
                job_tags.append(tag)

        return job_tags

    def extract_job_description(self, message: str):
        pass

    def extract_job_apply_via(self, message: str):
        pass

    def extract_job_apply_link(self, post):
        job_link = self.job_channel.link
        post_link = f'{job_link}/{str(post.id)}'
        return post_link

    def extract_job_company(self, message: str):
        pass

    def extract_job_channel(self, message: str):
        pass

    def extract_job_status_approved(self, message: str):
        pass

    def extract_job_status_deleted(self, message: str):
        pass

    # extracts the  product from the message,
    # note returned product data does not have image reference and Id
    def extract_job(self, post, job_id: str):
        message = post.message
        post_id = post.id
        posted_date = str(parser.parse(str(post.date)).isoformat())
        channel_id = post.peer_id.channel_id
        job = JobModel(
            id=job_id,
            telegram_channel_id=channel_id,
            telegram_post_id=post_id,
            title=self.extract_job_title(message=message),
            category=self.extract_job_category(message=message),
            status="closed" if self.is_job_closed(message=message) is True else "opened",
            contract_type=self.extract_job_contract_type(message=message),
            salary=self.extract_job_salary(message=message),
            available_positions=self.extract_job_available_positions(message=message),
            tags=self.extract_job_tag(message=message),
            description=self.extract_job_description(message=message),
            apply_via=self.extract_job_apply_via(message=message),
            apply_link=self.extract_job_apply_link(post),
            company=self.extract_job_company(message=message),
            job_channel=self.extract_job_channel(message=message),
            approved=self.extract_job_status_approved(message=message),
            deleted=self.extract_job_status_deleted(message=message),
            raw_post=message,
            first_modified=posted_date,
            last_modified=posted_date,
        )

        return job

    # sync products to firebase
    def sync_jobs(self):
        report = {
            JobChannelMethods.created: 0,
            JobChannelMethods.updated: 0,
            JobChannelMethods.removed: 0,
            JobChannelMethods.ignored: 0,
            JobChannelMethods.errored: 0,
            JobChannelMethods.not_job_post: 0,
            JobChannelMethods.total_analyzed: 0,
        }
        posts = self.telegram_channel.get_posts(shop_telegram_channel=self.job_channel.link)
        for post in posts:
            # wait for 100 milli seconds before initiating the next call
            time.sleep(0.1)
            sync_type = self.sync_job(post)
            report[sync_type] += 1
        report[JobChannelMethods.total_analyzed] = report[JobChannelMethods.created] + report[JobChannelMethods.removed] + report[
            JobChannelMethods.updated] + report[
                                                       JobChannelMethods.ignored] + report[JobChannelMethods.errored] + report[
                                                       JobChannelMethods.not_job_post]

        now_date_time = str(datetime.now().ctime())

        str_report = "{}\n{}\n\nj_created   -> {}\nj_updated  -> {}\nj_removed -> {}\nj_ignored   -> {}\nj_errored   -> " \
                     "{}\nnot_job_post   -> {}\nj_analyzed -> {}\n\n{} \n\n ------ errors begin ------ {} " \
                     "------ errors end ------ \n\n ------ not created begin ------ {} ------ not created end ------".format(
            self.job_channel.name,
            35 * "-", report[
                JobChannelMethods.created],
            report[
                JobChannelMethods.updated],
            report[
                JobChannelMethods.removed],
            report[
                JobChannelMethods.ignored],
            report[
                JobChannelMethods.errored],
            report[
                JobChannelMethods.not_job_post],
            report[
                JobChannelMethods.total_analyzed],
            now_date_time,
            "\n".join(self.errored_msg)[:1000],
            "\n".join(self.not_job_post_msg)[:1000]
        )

        self.errored_msg.clear()
        self.not_job_post_msg.clear()

        # telegram_bot.notify_sync_bot(str_report)
        return report

    def sync_job(self, post):
        self.post = post
        # 1. check if post is type "post job", and it is not a reply post
        if post is not None and post.message is not None:
            if self.is_post_job(post.message) and (post.reply_to is None):
                # product id is concatenated from the telegram channel id and the post id

                job_id = str(post.peer_id.channel_id) + "_" + str(post.id)

                if self.is_job_closed(message=post.message):  # job is closed, deleting job
                    self.firebase_crud.delete_job(job_id=job_id)
                    return JobChannelMethods.removed
                else:
                    result = self.firebase_crud.get_job(job_id=job_id)

                    # job does not exist inside firebase
                    if len(result) == 0:  # creating job
                        job = self.extract_job(post=post, job_id=job_id)
                        self.firebase_crud.create_job(job=job)
                        return JobChannelMethods.created
                    else:
                        # todo : update job here
                        # compare previous message with the new one and if there is a change reflect
                        return JobChannelMethods.updated
            else:

                # self.create_not_job_post_record(description=post.message)
                if len(self.not_job_post_msg) < 10 and str(post.message) not in self.not_job_post_msg:
                    message = str("no post message found " if post.message is None else post.message)
                    self.not_job_post_msg.append(message)
                return JobChannelMethods.not_job_post
        else:
            if len(self.not_job_post_msg) < 10 and str(post.message) not in self.not_job_post_msg:
                message = str("no post message found " if post.message is None else post.message)
                self.not_job_post_msg.append(message)

            return JobChannelMethods.not_job_post
