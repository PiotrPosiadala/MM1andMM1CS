import logging
from numpy import random

class Event():
    
    def __init__(self, event_type=0, current_time=0, lam=0, mi=0):

        if event_type is "ingoing":
            self.timestamp = current_time + random.exponential(scale = lam)
       
        elif event_type is "outgoing":
            self.timestamp = current_time + random.exponential(scale = mi)
            
        self.type = event_type
        logging.info("--EVENT-- Event generated: type = {}, current_time = {}, timestamp = {}".format(self.type, current_time, self.timestamp))

    def __str__(self):
        return('[timestamp=' + str(self.timestamp) + ' type='+ str(self.type) + ']')

    def __repr__(self):
        return str(self)