import os
from fastapi import FastAPI
from api.typesense_api import TypeSenseAPI
from lib.system_info import SystemInfo

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./cred/nib-job-finder-firebase-adminsdk-9y8l0-aca148cd64.json"
os.environ["mode"] = "test"

app = FastAPI()
ts = TypeSenseAPI()
sys_info = SystemInfo()


@app.post("/server/ts/index/product")
def index_product(product: dict):
    return ts.index_product(product)


@app.post("/server/ts/index/shop")
def index_product(shop: dict):
    return ts.index_shop(shop)


@app.get("/server/ts/search/{document}/{fields}/{query}")
def search(document: str, fields: str, query: str):
    return ts.search_data(document=document, fields=fields, query=query)


@app.get("/server/sync/shop/{shop_id}")
def sync_shop_by_id(shop_id: str):
    return {"message": "Successfully synced {}".format(shop_id)}
