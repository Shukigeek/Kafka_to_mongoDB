import os
from mongo_dal import Connection



class CRUD:
    def __init__(self):
        self.conn = Connection()
        self.client = self.conn.connect()
        if self.client is None:
            raise Exception(
                "Cannot connect to MongoDB. Check MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASSWORD, MONGO_DB"
            )

        self.db = self.client[self.conn.db]
        self.collection = self.db[os.getenv("MONGO_COLLECTION", "soldier_details")]

    def create(self):

        self.collection.insert_many({})


    def read(self, ID=None, first_name=None):
        filter_query = {}
        if ID is not None:
            filter_query["ID"] = ID
        elif first_name is not None:
            filter_query["first_name"] = first_name

        cursor = list(self.collection.find(filter_query, {"_id": 0}))
        if not cursor:
            return [{"error": "No matching record found"}]
        return cursor

