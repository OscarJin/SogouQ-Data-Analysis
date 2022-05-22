"""
作者：Krist
日期：2022年05月19日
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/SogouQ.csv", sep=',')

# 依据“访问时间”列中的“小时”重组dataframe
df['访问时间'] = pd.DataFrame([item.split(':')[0] for item in df['访问时间']])
sg_time = df.groupby(['访问时间'])

# 得到每一组对应的时间段和用户搜索次数
key_sg_time = pd.DataFrame(sg_time.groups.keys())
size_sg_time = pd.DataFrame(sg_time.size()).reset_index(drop=True)

# 将时间段和用户搜索次数两列合并为新的dataframe，存为search_time_analysis.txt
res = pd.concat([key_sg_time, size_sg_time], axis=1)
res.columns = ['时间段', '用户搜索次数']
res.to_csv('result/search_time_analysis.txt', sep='\t', index=False, encoding='utf_8_sig')

# 画出柱状图（在极大极小值上标数值）并保存为search_time_analysis.png
plt.bar(res['时间段'], res['用户搜索次数'])
plt.xlabel('时间段(h)')
plt.ylabel('用户搜索次数')
plt.title('搜索时间段统计')
plt.plot(res['时间段'], res['用户搜索次数'], color='r', linewidth=2, linestyle='solid')
max_min = [0, 4, 10, 12, 16, 18, 21, 23]
for a, b in zip(res['时间段'][max_min], res['用户搜索次数'][max_min]):
    plt.text(a, b+0.1, '%.0f' % b, ha='center', va='bottom', fontsize=11)
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
plt.savefig("result/search_time_analysis.png")
