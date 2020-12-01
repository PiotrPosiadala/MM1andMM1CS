#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import logging
import matplotlib.pyplot as plt
import numpy as np 
import statistics

class Stats():
    def __init__(self):
        self.event_IDs = []
        self.event_delays = []
        self.sys_empty_time = [0]
        self.event_occurrence_time = [0]
        self.sys_empty_ratio = [0]

    def delay_stats_update(self, event_ID, event_birthtime, event_deathtime):
        event_lifetime = event_deathtime - event_birthtime
        self.event_IDs.append(event_ID)
        self.event_delays.append(event_lifetime)
        logging.debug("--STATS-- delay_stats_update(): event_ID = {}, event_lifetime = {}".format(event_ID, event_lifetime))

    def sys_empty_update(self, penultimate_event_time, current_time, busy):
        time_diff = current_time - penultimate_event_time
        prev_empty_time = self.sys_empty_time[-1]
        if not busy: self.sys_empty_time.append((prev_empty_time+time_diff))
        if busy: self.sys_empty_time.append(prev_empty_time)
        self.event_occurrence_time.append(current_time)
        self.sys_empty_ratio.append(self.sys_empty_time[-1]/current_time)
        logging.debug("--STATS-- sys_empty_update(): event_occurrence_time[-1] = {}; sys_empty_time[-1] = {} ; sys_empty_ratio[-1] = {}".format(self.event_occurrence_time[-1], self.sys_empty_time[-1], self.sys_empty_ratio[-1]))

    def plot_delay(self, MI, LAM):
        events_to_cut = int(0.05*len(self.event_IDs))
        temp_event_IDs = self.event_IDs[events_to_cut:]
        temp_event_delays = self.event_delays[events_to_cut:]

        plt.plot(temp_event_IDs, temp_event_delays, linewidth=0.4)

        avg_delay = statistics.mean(temp_event_delays)
        logging.debug("--STATS-- plot_delay(): avg_delay = {}".format(avg_delay))
        print("--STATS-- plot_delay(): avg_delay = {}".format(avg_delay))
        plt.plot([temp_event_IDs[1], temp_event_IDs[-1] ],[avg_delay, avg_delay],linewidth=0.9, color="lime", linestyle = "-.")

        theoretical_avg_delay = (1/(MI-LAM))
        logging.debug("--STATS-- plot_delay(): theoretical_avg_delay = {}".format(theoretical_avg_delay))
        print("--STATS-- plot_delay(): theoretical_avg_delay = {}".format(theoretical_avg_delay))
        plt.plot([temp_event_IDs[1], temp_event_IDs[-1] ],[theoretical_avg_delay, theoretical_avg_delay], linewidth=0.9, color="red", linestyle = "--")

        plt.title("Czas przejścia pakietu przez system dla \u03BB = {:1.1f}, \u03BC = {:1.3f}, \u03C1 = {}.".format(LAM, MI, LAM/MI))
        plt.ylabel("T - Czas przejścia przez system")
        plt.xlabel("Numer pakietu")
        plt.show()

    def plot_sys_empty(self, MI, LAM):
        plt.plot(self.event_occurrence_time, self.sys_empty_ratio, linewidth=1, label = "p\u2080(t)")

        theoretical_avg_delay = (1-(LAM/MI))
        print("theoretical_avg_delay = {}".format(theoretical_avg_delay))
        plt.plot([self.event_occurrence_time[0], self.event_occurrence_time[-1]], [theoretical_avg_delay,theoretical_avg_delay], linewidth=1.2, label = "p\u2080" )
    
        plt.title("Wykres zbieżności p\u2080(t) do wartości p\u2080 z rozkładu stacjonarnego \ndla  \u03BB = {:1.1f}, \u03BC = {:1.1f}, \u03C1 = {}.".format(LAM, MI, LAM/MI))
        plt.xlabel("t")
        plt.legend()
        plt.show()