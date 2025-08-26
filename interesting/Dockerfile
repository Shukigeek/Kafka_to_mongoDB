FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

COPY core ./core
COPY . .



CMD ["uvicorn", "interesting.consumer_interesting_api:app", "--host", "0.0.0.0", "--port", "8001"]
