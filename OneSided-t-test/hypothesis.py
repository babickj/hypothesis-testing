
from scipy.stats import ttest_1samp
import numpy as np

#imports data from csv file ages
ages = np.genfromtxt("ages.csv")

#displays data from user to ensure correctness
print(ages)

#calculates the mean ages from the csv file
ages_mean = np.mean(ages)

#prints the mean for the user
print("mean age: {}".format(ages_mean))

#conduct t-test
tset, pval = ttest_1samp(ages,30)

print("p-values", pval)

#alpha = 0.05 or 5%
if pval < 0.05:
    print ("We reject the null hypothesis")
else:
    print("We accept the null hypothesis")

##END HYPOTHESIS TEST
    
