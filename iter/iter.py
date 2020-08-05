class Iter():
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()

        result = self.data[self.index]
        self.index += 1 
        return result

for t1 in Iter():
    print(t1)
'''
import datetime
import itertools
import random
import time


class Sensor():
    def __iter__(self):
        return self

    def __next__(self):
        return random.random

sensor = Sensor()
timestamps = iter(datetime.datetime.now, '2020-04-50 17:55:.530600')

for stamp, value in itertools.islice(zip(timestamps, sensor), 10):
    print(stamp, value)
    time.sleep(1)
'''