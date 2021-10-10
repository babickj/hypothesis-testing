import numpy as np
import pandas as pd

# Set the seed so that the numbers can be reproduced.
np.random.seed()

#df = pd.DataFrame(np.random.randn(5, 3), columns=list('ABC'))
#df = pd.DataFrame(np.random.rand(100,1))*100
df = pd.DataFrame(np.random.randn(50, 4), columns=list('ABCD'))

# Another way to set column names is "columns=['column_1_name','column_2_name','column_3_name']"

print(df)

#write to a csv file
#index = False prevents the row index names from going to csv file
df.to_csv('input.csv', index=False)
