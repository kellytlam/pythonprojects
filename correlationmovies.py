# %%
# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

%matplotlib inline
matplotlib.rcParams['figure.figsize'] = (12,8) # adjusts configuration of plots created later

# Read in the data

df = pd.read_csv(r'/Users/KellyLam/Desktop/Data_Analysis/Portfolio Project/Correlation in Python/movies.csv')

# %%
# Looking at data

df.head()
# %%
# Checking for missing data

for col in df.columns:
   pct_missing = np.mean(df[col].isnull())
   print('{} - {}%'.format(col, pct_missing))
# %%
# Dropping missing data
df = df.dropna()
# %%
# Data types for the columns

df.dtypes
# %%
