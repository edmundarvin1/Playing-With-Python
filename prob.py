import collections
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats 


testlist = [1, 4, 5, 6, 9, 9, 9]
c = collections.Counter(testlist)
count_sum = sum(c.values())
for k,v in c.items():
	print("The frequency pf number %s is %s" % (k,float(v)/count_sum))
plt.boxplot(testlist)
plt.savefig("boxplot.png")
plt.show()

plt.hist(testlist,histtype='bar')
plt.savefig("histogram.png")
plt.show()

plt.figure()
graph1= stats.probplot(testlist, dist='norm', plot= plt)
plt.savefig('qq_plot.png')
plt.show()


