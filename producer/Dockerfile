FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt


COPY . . 


CMD ["uvicorn", "producer.producer_api:app", "--host", "0.0.0.0", "--port", "8000"]
