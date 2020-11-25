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


event_list = EventList()
current_event = Event("ingoing", 0, lam_list[0], mi_list[0])
logging.info('Handling event started: timestamp={}, type={}'.format(current_event.timestamp, current_event.type))
current_time = 0


while event_list:
    logging.info('--While-- next iteration')
    current_event = event_list.getEvent()
    logging.info('Handling event started: timestamp={}, type={}'.format(current_event.timestamp, current_event.type))
    logging.info('event_list = {}'.format(event_list))


