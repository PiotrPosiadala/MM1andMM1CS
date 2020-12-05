#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

ro = [0.25, 0.5, 0.75]
lam = [2, 2, 2]
mi = [lam/ro for lam, ro in zip(lam, ro)]
triggers_to_serve = 100000   #PLEASE SET HOW MANY EVENTS YOU WANT TO SIMULATE
