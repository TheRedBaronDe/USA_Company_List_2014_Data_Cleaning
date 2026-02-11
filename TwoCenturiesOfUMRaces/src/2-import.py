# Data manipulation
import pandas as pd
import numpy as np 

# Visualization
import matplotlib.pyplot as plt 
import seaborn as sns

# Statistical analysis
from scipy import stats
from scipy.stats import pearsonr, spearmanr

# Set visualization style
plt.style.use('seaborn-v0_8-darkgrid') # apply a predefined style to the plot
sns.set_palette("husl") # set a colour

# Display settings
pd.set_option('display.max_columns', None) # displays all the columns
pd.set_option('display.max_rows', 100) # displays up to 100 rows
pd.set_option('display.float_format', '{:.2f}'.format) # round floats up to two decimal places

# Load the cleaned dataset
df = pd.read_csv('C:\\Users\\User\\Documents\\PostgreSQL\\TWO_CENTURIES_OF_UM_RACES_CLEAN.csv')
print(df.head()) # prints first rows
