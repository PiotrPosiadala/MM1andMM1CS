import logging
from Event import Event

class EventList(list):

    def __init__(self):
        pass
    
    #putEvent przyjmuje jako parametr obiekt klasy Event
    def putEvent(self, event):
        self.append(event)
        self.sort(key=lambda x: x.timestamp, reverse=False)
        logging.info("--EVENTLIST-- Event appended: {}".format(event))

    #get first event from list and remove that event from list
    def getEvent(self):
        temp_event = self[0]
        self.pop(0)
        return temp_event

    def printListElements(self):
        for elemnt in self:
            print('timestamp={}, type={}'.format(elemnt.timestamp, elemnt.type))



