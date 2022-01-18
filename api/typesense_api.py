import typesense
from typesense.exceptions import ObjectAlreadyExists


class TypeSenseAPI:

    def __init__(self):

        self.client = typesense.Client({
            'api_key': 'gSBSha05QBxPQwDLGIr8G8A7S8ZLIWbZQcgpykyQASNRK8Ns',
            'nodes': [{
                'host': '46.101.84.178',
                'port': '8108',
                'protocol': 'http'
            }],
            'connection_timeout_seconds': 2
        })

        try:
            self.client.collections.create({
                "name": "job",
                "fields": [
                    {"name": "title", "type": "string"},
                ],
            })
        except Exception as e:
            print(e)


    def index_job(self, product: dict):
        try:
            return self.client.collections["job"].documents.create(product)
        except ObjectAlreadyExists as e:
            return self.client.collections['job'].documents.update(product)


    def search_data(self, document: str, fields: str, query: str):
        search_parameters = {
            'q': query,
            'query_by': fields.split(","),
        }
        return self.client.collections[document].documents.search(search_parameters)
