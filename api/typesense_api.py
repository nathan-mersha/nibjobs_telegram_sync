import typesense
from typesense.exceptions import ObjectAlreadyExists


class TypeSenseAPI:

    def __init__(self):

        self.client = typesense.Client({
            'api_key': 'GpffZbKsgNu2UrhfR3NQpfoMTMUAZSWRPMUZNjglX2i7U90r',
            'nodes': [{
                'host': '178.62.83.84',
                'port': '8108',
                'protocol': 'http'
            }],
            'connection_timeout_seconds': 2
        })

        try:
            self.client.collections.create({
                "name": "product",
                "fields": [
                    {"name": "name", "type": "string"},
                    {"name": "category", "type": "string"},
                    {"name": "subCategory", "type": "string"},
                    {"name": "tag", "type": "string"},
                    {"name": "authorOrManufacturer", "type": "string"},

                ],
            })
        except Exception as e:
            print(e)

        try:
            self.client.collections.create({
                "name": "shop",
                "fields": [
                    {"name": "name", "type": "string"},
                    {"name": "description", "type": "string"},
                ],
            })
        except Exception as e:
            print(e)

    def index_product(self, product: dict):
        try:
            return self.client.collections["product"].documents.create(product)
        except ObjectAlreadyExists as e:
            return self.client.collections['product'].documents.update(product)

    def index_shop(self, shop: dict):
        try:
            return self.client.collections['shop'].documents.create(shop)
        except ObjectAlreadyExists as e:
            return self.client.collections['shop'].documents.update(shop)

    def search_data(self, document: str, fields: str, query: str):
        search_parameters = {
            'q': query,
            'query_by': fields.split(","),
        }
        return self.client.collections[document].documents.search(search_parameters)
