import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# lst = np.array(sns.get_dataset_names())
# print(lst)

df = sns.load_dataset('healthexp')

# print(df.head())


sns.pairplot(df,hue='Country')
plt.tight_layout() 
plt.show()