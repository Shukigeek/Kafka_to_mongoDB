from pub_sub.consumer import Consumer

def consume_not_interesting():
    consumer = Consumer("not_interesting")
    consumer.print_messages()
    return consumer