import warnings
import pandas as pd
warnings.filterwarnings('ignore')

sogou = pd.read_csv("SogouQ.csv", sep=',')
# for i in range(len(sogou)):
#     sogou.loc[i,'ID']=str(sogou.loc[i,'ID'])
columns = ['Id', 'Word', 'Merge']
dates = []
data = pd.DataFrame(columns=columns,index=dates)
data['Id']=sogou['ID']
data['Word']=sogou['word']
for i in range(len(data)):
    data.loc[i, 'Merge'] = [data.loc[i, 'Id'], data.loc[i, 'Word']]
data1 = data['Merge']
print(data1)
data1.to_csv("processed_data.csv", sep=",", index=True, header=True)
