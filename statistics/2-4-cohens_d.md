[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
``` python
import nsfg
import thinkstats2
import math
#import packages

df = nsfg.ReadFemPreg()

print (list(df.columns.values))
#read data and check df column names

live = df[df.outcome == 1]
firsts = live[live.birthord ==1]
others = live[live.birthord !=1]
#locate relevant data

print(firsts.totalwgt_lb.mean())
print(firsts.totalwgt_lb.var())
print(firsts.totalwgt_lb.std())

print(others.totalwgt_lb.mean())
print(others.totalwgt_lb.var())
print(others.totalwgt_lb.var())
#print basic statistics for manual calculation

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
#function for calculating Cohen's D effect

print(CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb))
print(CohenEffectSize(firsts.prglngth, others.prglngth))
#Cohen's D effect size is much greater for total weight than for pregnancy length.
# -.0886 standard deviations difference in means for weight vs .0288 standard deviations difference in means for length
```
