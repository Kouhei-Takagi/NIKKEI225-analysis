import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import numpy

tsd = web.DataReader("NIKKEI225", "fred", "2019/1/5")

fig1 = plt.figure(figsize=(10, 10))
fig1.suptitle("Figure 1 RAW")
plt.plot(tsd)

fig2 = plt.figure(figsize=(10, 10))
fig2.suptitle("Figure 2 DIFF")
plt.plot(tsd.diff())

fig3 = plt.figure(figsize=(10, 10))
fig3.suptitle("Figure 3 LOG(RAW)")
plt.plot(numpy.log(tsd))

fig4 = plt.figure(figsize=(10, 10))
fig4.suptitle("Figure 4 LOG(DIFF)")
plt.plot(numpy.log(tsd).diff())

plt.show()