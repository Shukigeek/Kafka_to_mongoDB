from pub_sub.consumer import Consumer


def consume_interesting():
    consumer = Consumer("interesting")
    consumer.print_messages()
    return consumer



