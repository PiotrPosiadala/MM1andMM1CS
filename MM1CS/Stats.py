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
        self.event_IDs2 = []
        self.event_delays = []
        self.event_waitings = []
        self.sys_empty_time = [0]
        self.sys_imagbusy_time = [0]
        self.event_occurrence_time = [0]
        self.event_occurrence_time2 = [0]
        self.event_occurrence_time3 = []
        self.event_occurrence_time4 = [0]
        self.sys_empty_ratio = [0]
        self.sys_imagbusy_ratio = [0]
        self.serving_events_amount = [0]
        self.serv_and_out_events_amount = []

    def delay_stats_update(self, event_ID, event_birthtime, event_deathtime):
        event_lifetime = event_deathtime - event_birthtime
        self.event_IDs.append(event_ID)
        self.event_delays.append(event_lifetime)
        logging.debug("--STATS-- delay_stats_update(): event_ID = {}, event_lifetime = {}".format(event_ID, event_lifetime))

    def sys_empty_update(self, penultimate_event_time, current_time, busy):
        time_diff = current_time - penultimate_event_time
        prev_empty_time = self.sys_empty_time[-1]
        if not busy: self.sys_empty_time.append((prev_empty_time+time_diff))
        elif busy: self.sys_empty_time.append(prev_empty_time)
        self.event_occurrence_time.append(current_time)
        self.sys_empty_ratio.append(self.sys_empty_time[-1]/current_time)
        logging.debug("--STATS-- sys_empty_update(): event_occurrence_time[-1] = {}; sys_empty_time[-1] = {} ; sys_empty_ratio[-1] = {}".format(self.event_occurrence_time[-1], self.sys_empty_time[-1], self.sys_empty_ratio[-1]))

    def serving_stats_update(self, current_time, serving_events_amount):
        self.event_occurrence_time2.append(current_time)
        self.serving_events_amount.append(serving_events_amount)

    def serv_and_out_stats_update(self, current_time, serv_and_out_events_amount):
        self.event_occurrence_time3.append(current_time)
        self.serv_and_out_events_amount.append(serv_and_out_events_amount)

    def waiting_time_stats_update(self, event_ID, event_birthtime, event_servicetime):
        event_waitingtime = event_servicetime - event_birthtime
        self.event_IDs2.append(event_ID)
        self.event_waitings.append(event_waitingtime)
        logging.debug("--STATS-- waiting_time_stats_update(): event_ID = {}, event_waitingtime = {}".format(event_ID, event_waitingtime))

    def sys_imagbusy_update(self, penultimate_event_time, current_time, imagbusy):
        time_diff = current_time - penultimate_event_time
        prev_imagbusy_time = self.sys_imagbusy_time[-1]
        if imagbusy: self.sys_imagbusy_time.append((prev_imagbusy_time+time_diff))
        elif not imagbusy: self.sys_imagbusy_time.append(prev_imagbusy_time)
        self.event_occurrence_time4.append(current_time)
        self.sys_imagbusy_ratio.append(self.sys_imagbusy_time[-1]/current_time)
        logging.debug("--STATS-- sys_imagbusy_update(): event_occurrence_time[-1] = {}; sys_imagbusy_time[-1] = {} ; sys_imagbusy_ratio[-1] = {}".format(self.event_occurrence_time4[-1], self.sys_imagbusy_time[-1], self.sys_imagbusy_ratio[-1]))

    def plot_delay(self, MI, LAM):
        events_to_cut = int(0.05*len(self.event_IDs))
        temp_event_IDs = self.event_IDs[events_to_cut:]
        temp_event_delays = self.event_delays[events_to_cut:]

        plt.plot(temp_event_IDs, temp_event_delays, linewidth=0.4)

        avg_delay = statistics.mean(temp_event_delays)
        logging.debug("--STATS-- plot_delay(): avg_delay = {}".format(avg_delay))
        print("--STATS-- plot_delay(): avg_delay = {}".format(avg_delay))
        plt.plot([temp_event_IDs[1], temp_event_IDs[-1] ],[avg_delay, avg_delay],linewidth=1.5, color="limegreen", label="Średnie opóźnienie")
        #plt.plot([temp_event_IDs[1], temp_event_IDs[-1] ],[avg_delay, avg_delay],linewidth=1.5, color="limegreen", label="t_constant")

        RHO = LAM/MI
        theoretical_avg_delay = (( (2-RHO) * RHO) / (LAM * (1-RHO) ))
        #theoretical_avg_delay = 0.75181
        logging.debug("--STATS-- plot_delay(): theoretical_avg_delay = {}".format(theoretical_avg_delay))
        print("--STATS-- plot_delay(): theoretical_avg_delay = {}".format(theoretical_avg_delay))
        plt.plot([temp_event_IDs[1], temp_event_IDs[-1] ],[theoretical_avg_delay, theoretical_avg_delay], linewidth=1.5, color="red", linestyle = "--", label="Teoretyczne średnie opóźnienie")
        #plt.plot([temp_event_IDs[1], temp_event_IDs[-1] ],[theoretical_avg_delay, theoretical_avg_delay], linewidth=1.5, color="red", linestyle = "--", label="t_variable")

        plt.title("Czas przejścia pakietu przez system dla \u03BB = {:1.1f}, \u03BC = {:1.3f}, \u03C1 = {}.".format(LAM, MI, LAM/MI))
        plt.ylabel("T - Czas przejścia przez system")
        plt.xlabel("Numer pakietu")
        plt.legend(loc=2)
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

    def plot_buffer(self, MI, LAM):
        events_to_cut = int(0.05*len(self.serving_events_amount))
        self.serving_events_amount = self.serving_events_amount[events_to_cut:]
        self.event_occurrence_time2 = self.event_occurrence_time2[events_to_cut:]
        plt.plot(self.event_occurrence_time2, self.serving_events_amount, linewidth=0.1)

        avg_buffer_temp=0
        for x in range(0, len(self.serving_events_amount)-1):
            avg_buffer_temp += (self.event_occurrence_time2[x+1]-self.event_occurrence_time2[x])*self.serving_events_amount[x+1]
        avg_buffer = avg_buffer_temp / ( self.event_occurrence_time2[-1]-self.event_occurrence_time2[0] )
        logging.debug("--STATS-- plot_buffer(): avg_buffer = {}".format(avg_buffer))
        print("--STATS-- plot_buffer(): avg_buffer = {}".format(avg_buffer))
        plt.plot([self.event_occurrence_time2[1], self.event_occurrence_time2[-1] ],[avg_buffer, avg_buffer],linewidth=1.5, color="limegreen", label="Średnia ilość zgłoszeń w kolejce")
        #plt.plot([self.event_occurrence_time2[1], self.event_occurrence_time2[-1] ],[avg_buffer, avg_buffer],linewidth=1.5, color="limegreen", label="t_const")

        RHO = LAM/MI
        theoretical_avg_buffer = ( RHO / (1-RHO) )
        #theoretical_avg_buffer = 3.00518
        logging.debug("--STATS-- plot_buffer(): theoretical_avg_buffer = {}".format(theoretical_avg_buffer))
        print("--STATS-- plot_buffer(): theoretical_avg_buffer = {}".format(theoretical_avg_buffer))
        plt.plot([self.event_occurrence_time2[1], self.event_occurrence_time2[-1] ],[theoretical_avg_buffer, theoretical_avg_buffer], linewidth=1.5, color="red", linestyle = "--", label="Teoretyczna średnia ilość zgłoszeń w kolejce")
        #plt.plot([self.event_occurrence_time2[1], self.event_occurrence_time2[-1] ],[theoretical_avg_buffer, theoretical_avg_buffer], linewidth=1.5, color="red", linestyle = "--", label="t_variable")

        plt.title("Liczba klientów w buforze dla \u03BB = {:1.1f}, \u03BC = {:1.3f}, \u03C1 = {}.".format(LAM, MI, LAM/MI))
        plt.ylabel("Q - liczba klientów w buforze")
        plt.xlabel("Czas symulacji")
        plt.legend(loc=2)
        plt.show()

    def plot_system(self, MI, LAM):
        events_to_cut = int(0.05*len(self.serv_and_out_events_amount))
        self.serv_and_out_events_amount = self.serv_and_out_events_amount[events_to_cut:]
        self.event_occurrence_time3 = self.event_occurrence_time3[events_to_cut:]
        plt.plot(self.event_occurrence_time3, self.serv_and_out_events_amount, linewidth=0.1)

        avg_system_temp=0
        for x in range(0, len(self.serv_and_out_events_amount)-1):
            avg_system_temp += (self.event_occurrence_time3[x+1]-self.event_occurrence_time3[x])*self.serv_and_out_events_amount[x+1]
        avg_system = avg_system_temp / ( self.event_occurrence_time3[-1]-self.event_occurrence_time3[0] )
        logging.debug("--STATS-- plot_system(): avg_system = {}".format(avg_system))
        print("--STATS-- plot_system(): avg_system = {}".format(avg_system))
        plt.plot([self.event_occurrence_time3[1], self.event_occurrence_time3[-1] ],[avg_system, avg_system],linewidth=1.5, color="limegreen", label="Średnia ilość zgłoszeń w systemie")
        #plt.plot([self.event_occurrence_time3[1], self.event_occurrence_time3[-1] ],[avg_system, avg_system],linewidth=1.5, color="limegreen", label="t_const")

        RHO = LAM/MI
        theoretical_avg_system = ( (2 - RHO) * RHO / (1-RHO) )
        #theoretical_avg_system = 0.58
        logging.debug("--STATS-- plot_system(): theoretical_avg_system = {}".format(theoretical_avg_system))
        print("--STATS-- plot_system(): theoretical_avg_system = {}".format(theoretical_avg_system))
        plt.plot([self.event_occurrence_time3[1], self.event_occurrence_time3[-1] ],[theoretical_avg_system, theoretical_avg_system], linewidth=1.5, color="red", linestyle = "--", label="Teoretyczna średnia ilość zgłoszeń w systemie")
        #plt.plot([self.event_occurrence_time3[1], self.event_occurrence_time3[-1] ],[theoretical_avg_system, theoretical_avg_system], linewidth=1.5, color="red", linestyle = "--", label="t_variable")

        plt.title("Liczba klientów w systemie dla \u03BB = {:1.1f}, \u03BC = {:1.3f}, \u03C1 = {}.".format(LAM, MI, LAM/MI))
        plt.ylabel("N - liczba klientów w systemie")
        plt.xlabel("Czas symulacji")
        plt.legend(loc=2)
        plt.show()

    def plot_waiting_time(self, MI, LAM):
        events_to_cut = int(0.05*len(self.event_IDs2))
        temp_event_IDs = self.event_IDs2[events_to_cut:]
        temp_event_waitings = self.event_waitings[events_to_cut:]

        plt.plot(temp_event_IDs, temp_event_waitings, linewidth=0.4)

        avg_waiting_time = statistics.mean(temp_event_waitings)
        logging.debug("--STATS-- plot_waiting_time(): avg_waiting_time = {}".format(avg_waiting_time))
        print("--STATS-- plot_waiting_time(): avg_waiting_time = {}".format(avg_waiting_time))
        plt.plot([temp_event_IDs[1], temp_event_IDs[-1] ],[avg_waiting_time, avg_waiting_time],linewidth=1.5, color="limegreen", label="Średni czas oczekiwania na obsługę")
        #plt.plot([temp_event_IDs[1], temp_event_IDs[-1] ],[avg_waiting_time, avg_waiting_time],linewidth=1.5, color="limegreen", label="t_const")

        RHO = LAM/MI
        theoretical_avg_waiting_time = ((RHO) / (LAM * (1-RHO) ))
        #theoretical_avg_waiting_time = 1.503
        logging.debug("--STATS-- plot_waiting_time(): theoretical_avg_waiting_time = {}".format(theoretical_avg_waiting_time))
        print("--STATS-- plot_waiting_time(): theoretical_avg_waiting_time = {}".format(theoretical_avg_waiting_time))
        plt.plot([temp_event_IDs[1], temp_event_IDs[-1] ],[theoretical_avg_waiting_time, theoretical_avg_waiting_time], linewidth=1.5, color="red", linestyle = "--", label="Teoretyczny czas oczekiwania na obsługę ")
        #plt.plot([temp_event_IDs[1], temp_event_IDs[-1] ],[theoretical_avg_waiting_time, theoretical_avg_waiting_time], linewidth=1.5, color="red", linestyle = "--", label="t_var")

        plt.title("Czas oczekiwania na obsługę dla \u03BB = {:1.1f}, \u03BC = {:1.3f}, \u03C1 = {}.".format(LAM, MI, LAM/MI))
        plt.ylabel("T - Czas oczekiwania na obsługę")
        plt.xlabel("Numer pakietu")
        plt.legend(loc=2)
        plt.show()

    def plot_sys_imagbusy(self, MI, LAM):
        plt.plot(self.event_occurrence_time4, self.sys_imagbusy_ratio, linewidth=1, label = "B_imag(t)")

        rho = (LAM/MI)
        one_minus_rho = 1 - rho

        print("--STATS-- plot_waiting_time(): rho = {}".format(rho))
        plt.plot([self.event_occurrence_time4[0], self.event_occurrence_time4[-1]], [rho,rho], linewidth=1.2, label = "\u03C1" )
        plt.plot([self.event_occurrence_time4[0], self.event_occurrence_time4[-1]], [one_minus_rho,one_minus_rho], linewidth=1.2, label = "1 - \u03C1" )
    
        plt.title("Wartość stosunku zajętości klientem wymaginowanym B_imag(t) \ndo pozostałych stanów systemu dla  \u03BB = {:1.1f}, \u03BC = {:1.1f}, \u03C1 = {}.".format(LAM, MI, LAM/MI))
        plt.xlabel("t")
        plt.legend()
        plt.show()