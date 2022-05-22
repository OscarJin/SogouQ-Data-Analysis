import warnings
import pandas as pd
warnings.filterwarnings('ignore')

data_merge = pd.read_csv("data/search_click_data.csv", sep=',', encoding='utf-8')
search_click_top10 = pd.value_counts(data_merge['Merge'])[0:10]
print(search_click_top10)

# output to file
output = open("result/search_click_top10.txt", 'w+', encoding='utf-8')
for i, v in search_click_top10.items():
    line = i.strip('[').strip(']').split(', ')
    print(str(eval(line[0]))+"\t"+str(eval(line[1]))+"\t"+str(v), file=output)
    #print(str(i[0])+"\t"+str(i[1])+"\t"+str(v), file=output)
