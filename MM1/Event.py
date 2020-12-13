#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from numpy import random

class Event():
    
    def __init__(self, event_type=0, current_time=0, time_param=0, birth_timestamp=0, event_ID=0):  

        if event_type is "ingoing":
            self.timestamp = current_time + random.exponential(scale = time_param)
            self.birth_timestamp = self.timestamp           
        
        elif event_type is "outgoing":
            self.timestamp = current_time + random.exponential(scale = time_param)
            self.birth_timestamp = birth_timestamp

        elif event_type is "serving":
            self.timestamp = time_param
            self.birth_timestamp = birth_timestamp

        self.event_ID = event_ID
        self.type = event_type
        logging.debug("--EVENT-- Event generated: current_time = {}, event = {}".format(current_time, self))

    def __str__(self):
        return('[timestamp=' + str(self.timestamp) + '; type='+ str(self.type) + '; birth_timestamp='+ str(self.birth_timestamp) +  '; event_ID='+ str(self.event_ID) + ']')

    def __repr__(self):
        return str(self)