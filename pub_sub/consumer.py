from kafka import KafkaConsumer

import json

class Consumer:
    def __init__(self, topic):
        self.consumer = KafkaConsumer(
            topic,
            group_id= 'my-group',
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            bootstrap_servers=['localhost:9092'],
            consumer_timeout_ms=10000,
            auto_offset_reset='earliest'
        )

    def print_messages(self):
        for message in self.consumer:
            print(f"{message.topic}:{message.partition}:{message.offset}: key={message.key} value={message.value}")

if __name__ == '__main__':
    c = Consumer("not_interesting")
    c.print_messages()
    h = Consumer("interesting")
    h.print_messages()
