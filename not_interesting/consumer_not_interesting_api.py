from fastapi import FastAPI
from core.manage_mongo import MongoManger

app = FastAPI()

consumer = MongoManger("not_interesting")

@app.get("/consume")
def consume():
    consumer.write("not_interesting")
    return {"status":"ok","consume":"not interesting"}

@app.get("/data")
def get_last_data(read = "all"):
    if read == "all":
        return consumer.read_all()
    return consumer.read_last()

