import warnings
import numpy as np
import pandas as pd
warnings.filterwarnings('ignore')

data = pd.read_csv("data/SogouQ.csv", sep=',')
# print(data)
url = data['用户点击的URL']
a = url.value_counts()

# print(a)
columns = ['url', 'Frequency']
dates = []
result = pd.DataFrame(columns=columns, index=dates)
ind = a.index
length = len(a)
b = pd.DataFrame(a)
b = np.array(b)
result['url'] = ind
result['Frequency'] = b
print(result)
result.to_csv('top_url.csv', sep=',')
print(result.describe())
