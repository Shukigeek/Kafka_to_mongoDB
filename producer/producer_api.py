from fastapi import FastAPI
from producer.manage_producer import ManageProducer
import uvicorn

app = FastAPI()


@app.get("/produce")
def produce():
    ManageProducer().produce_data()
    return {"status": "ok", "topic": "produce data"}



if __name__ == '__main__':
    uvicorn.run("producer_api:app", host="127.0.0.1", port=8000, reload=True)