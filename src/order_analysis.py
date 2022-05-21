import pandas as pd
import warnings
from numpy import mean
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

sogou = pd.read_csv("data/SogouQ.csv")

# TODO: 计算出日志数据的Order平均值

order_mean = mean(sogou['用户点击的顺序号'])
print(order_mean)

# TODO: 分析Order的频数，将Order频数排名前十位的数据表写出

order_count = sogou.value_counts(sogou['用户点击的顺序号']).head(n=10)
print(order_count)
order_count.to_csv("result/click_order_top10.txt", sep='\t', header=False)

# TODO: 对排名前十位的Order和频数，绘制出数据分布饼状图

plt.pie(order_count, labels=order_count.index, autopct='%0.1f%%', pctdistance=0.7)
plt.title("Top 10 Click Order")
plt.savefig('result/click_order_top10.png', dpi=300)
plt.show()
