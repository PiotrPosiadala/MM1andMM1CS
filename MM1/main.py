import logging
from numpy import random
import config #config module (config.py file)
from Event import Event
from EventList import EventList

logging.basicConfig(filename='main.log', filemode='w', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info('main.py started')

ro_list = config.ro
lam_list = config.lam
mi_list = config.mi

LAM = lam_list[0]
MI = mi_list[0]

############################################################################################################################

#INIT#
event_list = EventList()
current_time = 0
busy = False
event_list.putEvent(Event("ingoing", 0, LAM))
#INIT#

for n in range(100):
    logging.info("### NEXT EVENT ITERATION ###")
    logging.info("EventList: {}".format(event_list))
    current_event = event_list.getEvent()
    current_time = current_event.timestamp
    logging.info("SystemInfo: current_time = {}, busy = {}".format(current_time, busy))

    if current_event.type is "ingoing":
        
        if not busy:
            busy = True
            event_list.putEvent(Event("outgoing", current_time, MI))

        else:
            last_outgoing_time = event_list.findLastOutgoingTime()
            event_list.putEvent(Event("serving", current_time, last_outgoing_time))
            
        event_list.putEvent(Event("ingoing", current_time, LAM))

    elif current_event.type is "serving":       
        busy = True
        event_list.putEvent(Event("outgoing", current_time, MI))

    elif current_event.type is "outgoing":
        busy = False


    logging.info("### ITERATION FINISHED ### \n\n")



