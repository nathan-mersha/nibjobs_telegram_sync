import os
from fastapi import FastAPI
from api.typesense_api import TypeSenseAPI
from lib.system_info import SystemInfo

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./cred/nib-job-finder-firebase-adminsdk-9y8l0-aca148cd64.json"
os.environ["mode"] = "test"

app = FastAPI()
ts = TypeSenseAPI()
sys_info = SystemInfo()


@app.get("/server/system_info")
def get_system_info():
    return sys_info.get_info()


@app.post("/server/ts/index/job")
def index_product(job: dict):
    return ts.index_job(job)

@app.get("/server/ts/search/{document}/{fields}/{query}")
def search(document: str, fields: str, query: str):
    return ts.search_data(document=document, fields=fields, query=query)






