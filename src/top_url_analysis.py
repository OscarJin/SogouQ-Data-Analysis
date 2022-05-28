import pandas as pd
from collections import Counter
import warnings
import jieba as jb
import numpy as np
warnings.filterwarnings('ignore')
sogou = pd.read_csv("SogouQ.csv")
# print(sogou)
# TODO: 获取日志数据中的查询词，去除停用词并进行中文分词后，统计得到出现次数最高的前10个关键词
sogou['word'] = [jb.lcut(str(line)) for line in sogou['word']]
print(sogou['word'].head())

keyword_list = []
for line in sogou['word']:
    keyword_list += line

# count the keywords
keyword_count = dict(Counter(keyword_list))

# sort the count
keyword_count_sorted = dict(sorted(keyword_count.items(), key=lambda x: x[1], reverse=True))
# print(keyword_count_sorted)

# delete the stopping words
stop = open("Chinese_stop_words.txt", 'r+', encoding='utf-8')
stopwords = stop.read().split("\n")

# output top 10
num = 0
output = open("keywords.csv", 'w+', encoding='utf-8')
for key, value in keyword_count_sorted.items():
    if not(key in stopwords) and len(key) > 1 :
        print(key+"\t"+str(value), file=output)
        num += 1
