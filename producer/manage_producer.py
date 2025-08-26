from data.get_data import Data
from producer.producer_conn import Producer


class ManageProducer:
    def __init__(self):
        self.producer = Producer()
        self.interesting = Data().interesting()
        self.not_interesting = Data().not_interesting()
        self.local1 = 0
        self.local2 = 0
    def produce_data(self):
        interesting_data = self.interesting[self.local1:self.local1+10]
        self.producer.publish_message("interesting", {"interesting": interesting_data})
        not_interesting_data = self.not_interesting[self.local2:self.local2+10]
        self.producer.publish_message("not_interesting", {"not_interesting": not_interesting_data})
        self.local1 = (self.local1 + 10) % len(self.interesting)
        self.local2 = (self.local2 + 10)% len(self.not_interesting)
if __name__ == '__main__':

    m = ManageProducer()
    m.produce_data()


