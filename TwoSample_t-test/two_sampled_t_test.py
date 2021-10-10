from scipy.stats import ttest_ind
import numpy as np

#inport data from files
week1 = np.genfromtxt("out1.csv",  delimiter=",")
week2 = np.genfromtxt("out2.csv",  delimiter=",")

#calculate the mean of each sample size
week1_mean = np.mean(week1)
week2_mean = np.mean(week2)

#calculate the std deviation of each sample
week1_std = np.std(week1)
week2_std = np.std(week2)

#conduct the t-test and calculate p-value
ttest, pval = ttest_ind(week1, week2)

#display results to user
if pval < 0.05:
    print ("We reject the null hypothesis")
else:
    print("We accept the null hypothesis")


