from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import json
import time

class Producer:
    def __init__(self):
        while True:
            try:
                self.producer = KafkaProducer(
                    bootstrap_servers=['localhost:9092'],
                    value_serializer=lambda x: json.dumps(x).encode('utf-8')
                )
                print("Connected to Kafka!")
                break
            except NoBrokersAvailable:
                print("Kafka broker not ready yet, waiting...")
                time.sleep(2)

    def publish_message(self, topic, message):
        self.producer.send(topic, message)
        self.producer.flush()


