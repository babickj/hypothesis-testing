"""
When you can run a Z Test.

Several different types of tests are used in statistics (i.e. f test, chi square test, t test). You would use a Z test if:
1. Your sample size is greater than 30. Otherwise, use a t test.
2. Data points should be independent from each other. In other words, one data point isn’t related or doesn’t affect another data point.
3. Your data should be normally distributed. However, for large sample sizes (over 30) this doesn’t always matter.
4. Your data should be randomly selected from a population, where each item has an equal chance of being selected.
5. Sample sizes should be equal if at all possible.

Two-sample Z test- In two sample z-test , similar to t-test here we are checking two independent data groups and deciding whether sample mean of two group is equal or not.
H0 : mean of two group is 0
H1 : mean of two group is not 0
"""

#import libriaries
import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests

#import data from csv file
df = pd.read_csv("input.csv")
print(df[['A','B']].describe())

#conduct z-test
ztest, pval = stests.ztest(df['A'],x2=df['A'], value=0,alternative='two-sided')

#display p-value for user
print("p-value: {:.2f}".format(pval))

if pval<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")

