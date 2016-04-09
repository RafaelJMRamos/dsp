[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

import random
import thinkstats2
import thinkplot


t = [random.random() for _ in range(1000)]
#generate 1000 random numbers
pmf = thinkstats2.Pmf(t)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Show()
#plot pmf

cdf2 = thinkstats2.Cdf(t)
thinkplot.Cdf(cdf2)
thinkplot.Show(legend=False)
#plot cdf
