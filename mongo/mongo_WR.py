from mongo.mongo_dal import Connection

class WriteRead:
    def __init__(self,collection):
        self.conn = Connection()
        self.client = self.conn.connect()
        if self.client is None:
            raise Exception(
                "Cannot connect to MongoDB."
            )

        self.db = self.client[self.conn.db]
        self.collection = self.db[collection]

    def create(self,time,data):
        self.collection.insert_one({"timestamp":time,"data":data})
    def read_last(self):
        cursor = list(self.collection.find({}, {"timestamp": 1,"data":1, "_id": 0}).sort("timestamp", -1).limit(10))

        if not cursor:
            return [{"error": "No data found"}]
        return cursor
    def read_all_data(self):
        cursor = list(self.collection.find({}, {"_id": 0}))

        if not cursor:
            return [{"error": "No data found"}]
        return cursor

