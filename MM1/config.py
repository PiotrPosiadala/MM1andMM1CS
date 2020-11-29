from __future__ import division

ro = [0.25, 0.5, 0.75]
lam = [2, 2, 3]
mi = [lam/ro for lam, ro in zip(lam, ro)]
triggers_to_serve = 10000
