import jieba
import pandas as pd
from collections import Counter
import warnings
import jieba as jb
warnings.filterwarnings('ignore')

sogou = pd.read_csv("data/SogouQ_mini.csv")

sogou['查询词'] = [jieba.lcut(line) for line in sogou['查询词']]
print(sogou['查询词'].head())

keyword_list = []
for line in sogou['查询词']:
    keyword_list += line
# print(keyword_list)

keyword_count = dict(Counter(keyword_list))
print(keyword_count)

keyword_count_sorted = sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)
print(keyword_count_sorted)
