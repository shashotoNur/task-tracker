import math
from termplot import Plot
xvals, yvals = [], []
for i in range(0, 2000, 5):
    xx = i / 100.0
    xvals.append(xx)
    yvals.append(math.sin(xx) * float(i ** 0.5))
Plot(xvals, yvals)
