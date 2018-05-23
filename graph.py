import datetime
from matplotlib import pyplot as plt
loc = [1200, 1245, 1357]
dates = [1.1,3.1,5.1]

tested_loc = [500, 650, 670]


plt.plot(dates,tested_loc)
plt.plot(dates,loc)
plt.show()