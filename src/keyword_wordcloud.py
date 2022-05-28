from matplotlib import pyplot as plt
from wordcloud import WordCloud
import pandas as pd
from PIL import Image
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# TODO: 统计得到出现次数最高的前100个搜索关键词，根据其出现次数绘制词云图

keyword_df = pd.read_table("data/keywords_top100.txt", header=None)

# 转换成词典制作词云
df0 = keyword_df[0].tolist()
df1 = keyword_df[1].tolist()
keyword_top100 = dict(zip(df0, df1))
print(keyword_top100)

# create mask
img = Image.open(r'data/mask.jpg')
img_array = np.array(img)

# 创建词云
wc = WordCloud(
    mask=img_array,
    width=1200,
    height=800,
    background_color='white',
    max_words=200,
    font_path='simhei')
wc.generate_from_frequencies(keyword_top100)
plt.imshow(wc)
plt.axis("off")
wc.to_file('result/keywords_top100.png')
plt.show()
