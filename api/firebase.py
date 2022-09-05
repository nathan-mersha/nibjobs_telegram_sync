import firebase_admin
from firebase_admin import credentials, firestore
from model.job_model import JobModel


class FirebaseCRUD:
    global_config_id = "VM4rSfVp138U9YPvc69g"

    def __init__(self):
        print("init firebase app.....")
        cred = credentials.Certificate("./cred/nib-job-finder-firebase-adminsdk-9y8l0-aca148cd64.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

        # defining model references of firestore
        self.job_channel_ref = self.db.collection("jobChannel")
        self.global_config_ref = self.db.collection("globalConfig")
        self.job_ref = self.db.collection("job")
        self.job = self.db.collection("job")

    def get_job_channel(self, shop_id: str):
        doc_ref = self.job_channel_ref.document(shop_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            print("no shop found by id : ", shop_id)

    def create_job(self, job: JobModel):
        if len(job.tags) >= 2:
            job.approved = True
        elif job.category=="health & medicine" or job.category=="architecture and engineering" or job.category=="business & administration" or job.category=="education":
            job.approved = True

        self.job_ref.document(job.id).set(job.to_json())

    def get_job(self, job_id: str):
        result = self.db.collection("job").where("id", "==", job_id).get()
        return result

    def get_deleted_job(self, job_id: str):
        result = self.db.collection("deletedJob").where("id", "==", job_id).get()
        return result

    def delete_job(self, job_id: str):
        self.db.collection("job").document(job_id).delete()

    def get_global_config(self):
        config = self.global_config_ref.document(self.global_config_id).get()
        return config.to_dict()

    def update_global_config(self, global_config):
        global_config_doc = self.global_config_ref.document(self.global_config_id)
        return global_config_doc.update(global_config)

