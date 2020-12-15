#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

ro = 0.25                   #change ro
lam = 2                     #rather than lambda
mi = lam/ro
triggers_to_serve = 10000    #please set how many events you want to simulate

#Parametry do przesymulowania (do wyboru)
E_T_id = 1                  #srednie opoznienie w systemie
E_Q_id = 2                  #srednia liosc klientow w buforze
E_N_id = 3                  #srednia liosc klientow w systemie
E_W_id = 4                  #sredni czas oczekiwania na obsluge
P_id = 5                    #wykres p-stwa, ze serwer jest zajety obsluga klienta wyimaginowanego

simulation = 2              #tutaj prosze wpisac ID 1,2,3,4 lub 5, w zaleznosci od tego co ma byc przesymulowane
