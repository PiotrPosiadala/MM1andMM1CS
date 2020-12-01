#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""MM1 System simulation
        OAST 20Z
Please run using Python 3.6.(8)"""

import logging
from numpy import random
import config 
import Stats as sts
from Event import Event
from EventList import EventList

#CONFIG
logging.basicConfig(filename='main.log', filemode='w', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')   #PLEASE SET LOGGING INFO 
logging.info('main.py started')
ro_list = config.ro
lam_list = config.lam
mi_list = config.mi
triggers_to_serve = config.triggers_to_serve
#CONFIG

#INIT
LAM = lam_list[0]   #PLEASE SET LAMBDA INDEX FROM CONFIG MODULE
MI = mi_list[0]     #PLEASE SET MI     INDEX FROM CONFIG MODULE
event_list = EventList()
stats = sts.Stats()
current_time = 0
penultimate_event_time = 0
new_event_ID = 1
busy = False

event_list.putEvent(Event("ingoing", 0, 1/LAM, current_time, new_event_ID))
new_event_ID += 1
#INIT

while new_event_ID < triggers_to_serve:

    logging.info("### NEXT EVENT ITERATION ###")
    logging.info("EventList: {}".format(event_list))

    current_event = event_list.getEvent()
    current_time = current_event.timestamp
    stats.sys_empty_update(penultimate_event_time, current_time, busy)

    logging.info("SystemInfo: current_time = {}, busy = {}, , penultimate_event_time = {}".format(current_time, busy, penultimate_event_time))

    if current_event.type == "ingoing":
        
        if not busy:
            busy = True
            event_list.putEvent(Event("outgoing", current_time, 1/MI, current_event.birth_timestamp, current_event.event_ID))

        else:
            last_outgoing_time = event_list.findLastOutgoingTime()
            event_list.putEvent(Event("serving", current_time, last_outgoing_time, current_event.birth_timestamp, current_event.event_ID))
            
        event_list.putEvent(Event("ingoing", current_time, 1/LAM, current_time, new_event_ID))
        new_event_ID += 1
        
    elif current_event.type == "serving":       
        busy = True
        event_list.putEvent(Event("outgoing", current_time, 1/MI, current_event.birth_timestamp, current_event.event_ID))

    elif current_event.type == "outgoing":
        busy = False
        stats.delay_stats_update(current_event.event_ID, current_event.birth_timestamp, current_time)

    penultimate_event_time = current_time
    logging.info("### ITERATION FINISHED ### \n\n")


#stats.plot_delay(MI,LAM)      #PLEASE UNCOMMENT ONE OF THESE TO SHOW APPROPRIATE CHART
stats.plot_sys_empty(MI,LAM)



