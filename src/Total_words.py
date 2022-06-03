import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv('data/keywords.txt', sep="\t", names=['word', 'Frequency'])
print(data.head())
print(data.describe())
data['target'] = 0
conditions = [
    data['Frequency'] >= 500,
    (data['Frequency'] < 500) & (data['Frequency'] >= 200),
    (data['Frequency'] < 200) & (data['Frequency'] >= 50),
    (data['Frequency'] < 50) & (data['Frequency'] >= 10)]
rating = [4, 3, 2, 1]
data['rating'] = np.select(conditions, rating, default=0)
print(data)
print(data.rating.value_counts())
data2 = data[data['rating'] < 4]
bx = sns.boxplot(x="rating", y='Frequency', data=data2)
bx.set(xlabel='Word Label', ylabel='Word Frequency', title='Word Frequency With Different Labels')
