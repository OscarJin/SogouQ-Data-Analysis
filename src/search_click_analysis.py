import warnings
import pandas as pd
warnings.filterwarnings('ignore')

# TODO: 统计得到每个用户每个查询词点击网页的次数，写出将次数最高的前10项
sogou = pd.read_csv("data/SogouQ.csv", sep=',')

# data = pd.DataFrame(columns=['Id', 'Word'], index=[])
# data['Id'] = sogou['用户ID']
# data['Word'] = sogou['查询词']
# for i in range(len(data)):
#     data.loc[i, 'Merge'] = [data.loc[i, 'Id'], data.loc[i, 'Word']]
data1 = pd.DataFrame([[sogou.loc[i, '用户ID'], sogou.loc[i, '查询词']] for i in range(len(sogou))])
print(data1.head())
# data1.to_csv("data/processed_data.csv", sep=",", index=False, header=None)
