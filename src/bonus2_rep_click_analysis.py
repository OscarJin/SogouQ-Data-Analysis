"""
作者：Krist
日期：2022年05月28日
"""
import pandas as pd

# 去掉URL列
sogou = pd.read_csv("data/SogouQ.csv", sep=',').drop(columns=['用户点击的URL'])

# 依据‘用户ID’分组
sg_ID = sogou.groupby('用户ID')

# 用户ID列表
ID_total = pd.DataFrame(sg_ID.groups.keys())

# 用户ID个数
ID_count = ID_total.size

# 每个用户ID所含的查询词个数
ID_wordcount = sg_ID['查询词'].nunique()

# 每个用户ID的总点击数
ID_clickcount = sg_ID.size()

# 每个用户ID单次搜索的平均点击数
ID_meanclick = pd.DataFrame(ID_clickcount / ID_wordcount).reset_index(drop=True)
ID_meanclick.columns = ['mean_click']

# 合并为新的dataframe
ID_wordcount = pd.DataFrame(ID_wordcount).reset_index(drop=True)
ID_merge = pd.concat([ID_total, ID_wordcount, ID_meanclick], axis=1)
ID_merge.columns = ['ID_total', 'ID_wordcount', 'ID_meanclick']

# 分5个level
group1 = ID_meanclick[ID_meanclick['mean_click'] == 1].size
group1_rate = group1 / ID_count
group2 = ID_meanclick[ID_meanclick['mean_click'] >= 3].size
group2_rate = group2 / ID_count
group3 = ID_meanclick[ID_meanclick['mean_click'] >= 5].size
group3_rate = group3 / ID_count
group4 = ID_meanclick[ID_meanclick['mean_click'] >= 7].size
group4_rate = group4 / ID_count
group5 = ID_meanclick[ID_meanclick['mean_click'] >= 10].size
group5_rate = group5 / ID_count

# 将统计结果合并为新的dataframe
rep_click = pd.DataFrame({'单次搜索平均点击量': ['=1', '>=3', '>=5', '>=7', '>=10'],
                          '用户数': [group1, group2, group3, group4, group5],
                          '用户占比': [group1_rate, group2_rate, group3_rate, group4_rate, group5_rate]},
                         index=[1, 2, 3, 4, 5])
rep_click.to_csv('result/rep_click.csv', index=False, encoding='utf_8_sig')

# 结论：83%的用户在一次搜索中的平均点击数<3, 即大部分用户不会在一次搜索结果中较多次点击。
# 这可能说明整体而言，搜狗引擎得到的结果与用户需求匹配度较高
# 单次搜索点击率较高的用户有可能会通过改变关键词来获得新的搜索结果，这也是之后可以继续研究的
