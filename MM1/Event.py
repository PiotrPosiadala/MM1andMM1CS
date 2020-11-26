import logging
from numpy import random

class Event():
    
    def __init__(self, event_type=0, current_time=0, time_param=0):

        if event_type is "ingoing":
            self.timestamp = current_time + random.exponential(scale = time_param)

        if event_type is "serving":
            self.timestamp = time_param
       
        elif event_type is "outgoing":
            self.timestamp = current_time + random.exponential(scale = time_param)
            
        self.type = event_type
        logging.info("--EVENT-- Event generated: current_time = {}, type = {}, timestamp = {}".format(current_time, self.type,  self.timestamp))

    def __str__(self):
        return('[timestamp=' + str(self.timestamp) + ' type='+ str(self.type) + ']')

    def __repr__(self):
        return str(self)