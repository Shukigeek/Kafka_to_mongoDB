from datetime import datetime
from core.consumer import Consumer
from core.mongo_WR import WriteRead


class MongoManger:
    def __init__(self,collection):
        self.mongo = WriteRead(collection)
    def write(self,collection):
        consumer = Consumer(collection).get_all_messages()
        for msg in consumer[0][collection]:
            self.mongo.create(str(datetime.now()),msg)
        return {"inserted": len(consumer), "collection": collection}
    def read_last(self):
        return self.mongo.read_last()
    def read_all(self):
        return self.mongo.read_all_data()






