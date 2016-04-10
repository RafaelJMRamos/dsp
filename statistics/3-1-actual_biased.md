[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)
```python
import chap01soln
import thinkstats2

df = chap01soln.ReadFemResp()
pmf = thinkstats2.Pmf(df.numkdhh, label = 'actual')

#import actual data as pmf

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf
#function for creating biased data

biasedpmf = BiasPmf(pmf, 'biased')

import thinkplot

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biasedpmf])
thinkplot.Show()
#plot actual and biased data

print(pmf.Mean())

print(biasedpmf.Mean())
#compute means for biased and actual
```
