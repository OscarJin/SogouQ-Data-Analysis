import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/keywords.txt', sep="\t", names=['word', 'Frequency'])
print(data.head())
print(data.describe())

data_100 = data.head(n=100)
plt.plot(data_100.index, data_100['Frequency'])
plt.title("Keyword Frequency Distribution")
plt.xlabel("Keyword Ranking")
plt.ylabel("Frequency")
plt.show()

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
plt.show()
