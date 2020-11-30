import logging
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import statistics

class Stats():
    def __init__(self):
        self.event_IDs = []
        self.event_delays = []

    def delay_stats_update(self, event_ID, event_birthtime, event_deathtime):
        event_lifetime = event_deathtime - event_birthtime
        self.event_IDs.append(event_ID)
        self.event_delays.append(event_lifetime)
        logging.debug("--STATS-- delay_stats_update(): event_ID = {}, event_lifetime = {}".format(event_ID, event_lifetime))
        logging.debug("--STATS-- delay_stats_update(): event_ID = {}, event_lifetime = {}".format(event_ID, event_lifetime))
    
    def plot_delay(self, MI, LAM):
        events_to_cut = int(0.05*len(self.event_IDs))
        temp_event_IDs = self.event_IDs[events_to_cut:]
        temp_event_delays = self.event_delays[events_to_cut:]

        plt.plot(temp_event_IDs, temp_event_delays, linewidth=0.4)

        avg_delay = statistics.mean(temp_event_delays)
        logging.debug("--STATS-- plot_delay(): avg_delay = {}".format(avg_delay))
        print("--STATS-- plot_delay(): avg_delay = {}".format(avg_delay))
        plt.plot([temp_event_IDs[1], temp_event_IDs[-1] ],[avg_delay, avg_delay],linewidth=0.7, color="lime", linestyle = "-.")

        theoretical_avg_delay = (1/(MI-LAM))
        logging.debug("--STATS-- plot_delay(): theoretical_avg_delay = {}".format(theoretical_avg_delay))
        print("--STATS-- plot_delay(): theoretical_avg_delay = {}".format(theoretical_avg_delay))
        plt.plot([temp_event_IDs[1], temp_event_IDs[-1] ],[theoretical_avg_delay, theoretical_avg_delay], linewidth=0.7, color="red", linestyle = "--")

        
        plt.title("Czas przejścia pakietu przez system dla \u03BB = {:1.1f}, \u03BC = {:1.3f}, \u03C1 = {}.".format(LAM, MI, LAM/MI))
        plt.ylabel("T - Czas przejścia przez system")
        plt.xlabel("Numer pakietu")
        plt.show()
