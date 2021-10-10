"""
    Paired sampled t-test :- The paired sample t-test is also called dependent sample t-test. It’s an uni variate test that tests for a significant difference between 2 related variables. An example of this is if you where to collect the blood pressure for an individual before and after some treatment, condition, or time point.
    H0 :- means difference between two sample is 0
    H1:- mean difference between two sample is not 0
"""

#inport libraires for data analysis
import pandas as pd
from scipy import stats

#import data from a csv file
df = pd.read_csv('input.csv')

#Displays key statistical parameters for the user
print(df[['A','B']].describe())

#condcut t-test and calcualte p-value
ttest, pval = stats.ttest_rel(df['A'],df['B'])

#display pval for the user
print("p-value: {:.2f}".format(pval))

#Displays if hypothesis was accepted or rejected to the user
if pval < 0.05:
    print("Reject the null hypothesis")
else:
    print("Accept the null hypothesis")
