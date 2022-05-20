import pandas as pd
import warnings
from numpy import mean
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

sogou = pd.read_csv("data/SogouQ.csv")

order_mean = mean(sogou['用户点击的顺序号'])
print(order_mean)

order_count = sogou.value_counts(sogou['用户点击的顺序号']).head(n=10)
print(order_count)
order_count.to_csv("result/click_order_top10.txt", sep='\t', header=False)

plt.pie(order_count, labels=order_count.index, autopct='%0.1f%%', pctdistance=0.7)
plt.title("Top 10 Click Order")
plt.savefig('result/click_order_top10.png', dpi=300)
plt.show()
