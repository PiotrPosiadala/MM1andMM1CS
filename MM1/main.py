import logging
import config
from Event import Event
from EventList import EventList

logging.basicConfig(filename='main.log', filemode='w', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.info('main.py started')

ro_list = config.ro

event_list = EventList()
current_event = Event()

#TEST
event1 = Event(2, 1)
logging.info(event1)
event2 = Event(10, 3)
logging.info(event2)

event_list.putEvent(event2)
logging.info('event_list = {}'.format(event_list))
event_list.putEvent(event1)
logging.info('event_list = {}'.format(event_list))



#TEST

while event_list:
    logging.info('--While-- next iteration')
    current_event = event_list.getEvent()
    logging.info('Handling event started: timestamp={}, type={}'.format(current_event.timestamp, current_event.type))
    logging.info('event_list = {}'.format(event_list))


