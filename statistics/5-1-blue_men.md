[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
#create distribution

low = dist.cdf(177.8)    # 5'10" is 177.8 cm
high = dist.cdf(185.4)   # 6'1" is 185.4 cm
print(high-low)
#find percentage of upper and lower bounds of blue man group height requirements, and compute difference
#the percentage of the male population that is in this height range is 34.21%
