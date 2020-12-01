#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from Event import Event

class EventList(list):

    def __init__(self):
        pass
    
    def putEvent(self, event):
        self.append(event)
        if event.type is "outgoing": self.updateAllServingEvents(event.timestamp) 
        self.sort(key=lambda x: (x.timestamp, x.type), reverse=False)
        logging.debug("--EVENTLIST-- PutEvent: {}".format(event))

    def getEvent(self):
        temp_event = self[0]
        self.pop(0)
        logging.debug("--EVENTLIST-- GetEvent: {}".format(temp_event))
        return temp_event

    def findLastOutgoing(self):
        event_index = self.index(next(event for event in reversed(self) if event.type is "outgoing"))
        logging.debug("--EVENTLIST-- findLastOutgoing: {}".format(event_index))
        return event_index

    def findLastOutgoingTime(self):
        event_time = self[self.findLastOutgoing()].timestamp
        logging.debug("--EVENTLIST-- findLastOutgoingTime: {}".format(event_time))
        return event_time

    def updateAllServingEvents(self, new_timestamp):
        for event in self: 
             if event.type is "serving": event.timestamp = new_timestamp

    def printListElements(self):
        for elemnt in self:
            print(elemnt)



