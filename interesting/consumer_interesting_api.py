from fastapi import FastAPI
from core.manage_mongo import MongoManger
import uvicorn

app = FastAPI()

consumer = MongoManger("interesting")

@app.get("/consume")
def consume():
    consumer.write("interesting")
    return {"status":"ok","consume":"interesting"}

@app.get("/data")
def get_last_data(read = "all"):
    if read == "all":
        return consumer.read_all()
    return consumer.read_last()

if __name__ == '__main__':
    uvicorn.run("consumer_interesting_api:core", host="127.0.0.1", port=8001, reload=True)