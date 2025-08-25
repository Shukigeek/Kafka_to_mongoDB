from data.get_data import Data
from pub_sub.producer import Producer


class ManageProducer:
    def __init__(self):
        self.producer = Producer()
        self.interesting = Data().interesting()
        self.not_interesting = Data().not_interesting()
        self.local = 0
    def produce_data(self):
        interesting_data = self.interesting[self.local:self.local+10]
        self.producer.publish_message("interesting", {"interesting": interesting_data})
        not_interesting_data = self.not_interesting[self.local:self.local+10]
        self.producer.publish_message("not_interesting", {"not_interesting": not_interesting_data})
        self.local += 10
if __name__ == '__main__':

    m = ManageProducer()
    m.produce_data()


