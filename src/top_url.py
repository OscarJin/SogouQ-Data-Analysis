import warnings
import numpy as np
warnings.filterwarnings('ignore')
import pandas as pd
data = pd.read_csv("SogouQ.csv", sep=',')
# print(data)
url=data['click_URL']
a=url.value_counts()
# print(a)
columns=['url', 'Frequency']
dates=[]
result=pd.DataFrame(columns=columns,index=dates)
ind=a.index
length=len(a)
b=pd.DataFrame(a)
b=np.array(b)
result['url']=ind
result['Frequency']=b
print(result)
result.to_csv('top_url.csv',sep=',')
print(result.describe())
