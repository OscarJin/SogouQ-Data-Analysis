import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Transfer dataset to csv

sogou = pd.read_table("data/SogouQ.reduced", header=None,
                      names=['访问时间', '用户ID', '查询词', '该URL在返回结果中的排名', '用户点击的顺序号', '用户点击的URL'],
                      sep='\s+', encoding='gb18030', error_bad_lines=False)

# Delete '[' and ']' in Queries
sogou['查询词'] = pd.DataFrame([str(line).strip('[').strip(']') for line in sogou['查询词']])

print(sogou['查询词'].head())
sogou.to_csv("data/SogouQ.csv", index=False, encoding='utf_8_sig')

# Same for sample dataset
sogou_mini = pd.read_table("data/SogouQ.sample", header=None,
                      names=['访问时间', '用户ID', '查询词', '该URL在返回结果中的排名', '用户点击的顺序号', '用户点击的URL'],
                      sep='\s+', encoding='gb18030', error_bad_lines=False)

sogou_mini['查询词'] = pd.DataFrame([str(line).strip('[').strip(']') for line in sogou_mini['查询词']])

print(sogou_mini['查询词'].head())
sogou_mini.to_csv("data/SogouQ_mini.csv", index=False, encoding='utf_8_sig')

