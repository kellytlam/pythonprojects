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

df = pd.read_csv(r'/Users/KellyLam/Desktop/Data_Analysis/pythonprojects/movies.csv')

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
#Changing data type of budget, gross, votes, and runtime columns

df['budget'] = df['budget'].astype('int64')
df['gross'] = df['gross'].astype('int64')
df['votes'] = df['votes'].astype('int64')
df['runtime'] = df['runtime'].astype('int64')

# %%
df

# %%
#Create Year Correct Column
df['yearcorrect'] = df['released'].str.extract(pat = '([0-9]{4})').astype(int)

df
# %%
#Sorting by gross value

df = df.sort_values(by=['gross'], inplace=False, ascending=False)
# %%
pd.set_option('display.max_rows', None)
# %%
#Drop any duplicates
df['company'].drop_duplicates().sort_values(ascending=False)
# %%
df.head()

# %%
#Scatterplot with budget vs gross to check correlation

plt.scatter(x=df['budget'], y=df['gross'])
plt.title('Budget vs Gross Earnings')
plt.xlabel('Budget for Film')
plt.ylabel('Gross Earnings')
plt.show()
# %%
df.head()
# %%
# Plot budget vs gross using seaborn
sns.regplot(x='budget', y='gross', data=df, scatter_kws={"color":"red"}, line_kws={"color":"blue"})
# %%
#Looking at correlation
subset_df = df[['budget', 'gross', 'runtime', 'score', 'votes', 'year']]
corr_matrix = subset_df.corr(method='pearson')
print(corr_matrix)
# %%
# High correlation between budget and gross
sns.heatmap(corr_matrix, annot=True)
plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()
