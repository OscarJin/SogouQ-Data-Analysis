import warnings
warnings.filterwarnings('ignore')
import pandas as pd






data = pd.read_csv("processed_data.csv", sep=',')
print(data['Merge'])
data1=data['Merge']
data2=pd.value_counts(data1)
data3=data2[0:10]
print(data3)
ind=data3.index
print(ind[0])
a=ind[0]
print(a)
print(type(a))
columns=['Id', 'Word','Frequency']
dates=[]
result=pd.DataFrame(columns=columns,index=dates)
for i in range(10):
    result.loc[i,'Frequency']=data3.iloc[i]
    b=ind[i]
    c=b.split(',',2)
    d=c[0]
    e=c[1]
    if(i==0):
        x = d[1:len(d)]
        y = e[2:len(e) - 2]
    else:
        x = d[2:len(d)-1]
        y = e[2:len(e) - 2]

    result.loc[i, 'Id']=x
    result.loc[i, 'Word']=y
print(result)
result.to_csv('search_click_top10.txt', sep='\t',index=True, header = True)
