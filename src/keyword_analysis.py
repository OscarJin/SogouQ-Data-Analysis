import pandas as pd
from collections import Counter
import warnings
import jieba as jb
import numpy as np
warnings.filterwarnings('ignore')

sogou = pd.read_csv("data/SogouQ.csv")

# TODO: 获取日志数据中的查询词，去除停用词并进行中文分词后，统计得到出现次数最高的前10个关键词
sogou['查询词'] = [jb.lcut(str(line)) for line in sogou['查询词']]
print(sogou['查询词'].head())

keyword_list = []
for line in sogou['查询词']:
    keyword_list += line

# count the keywords
keyword_count = dict(Counter(keyword_list))

# sort the count
keyword_count_sorted = dict(sorted(keyword_count.items(), key=lambda x: x[1], reverse=True))
# print(keyword_count_sorted)

# delete the stopping words
stop = open("data/Chinese_stop_words.txt", 'r+', encoding='utf-8')
stopwords = stop.read().split("\n")

# output top 10
num = 0
output = open("result/keywords_top10.txt", 'w+', encoding='utf-8')
for key, value in keyword_count_sorted.items():
    if not(key in stopwords) and len(key) > 1 and num < 10:
        print(key+"\t"+str(value), file=output)
        num += 1

# output top 100 for wordcloud
# num = 0
# output_100 = open("data/keywords_top100.txt", 'w+', encoding='utf-8')
# for key, value in keyword_count_sorted.items():
#     if not(key in stopwords) and len(key) > 1 and num < 100:
#         print(key+"\t"+str(value), file=output_100)
#         num += 1
