import warnings
import pandas as pd
warnings.filterwarnings('ignore')

# TODO: 统计得到每个用户每个查询词点击网页的次数，写出次数最高的前10项


def merge_data(_input_df):
    _data_merge = pd.DataFrame(columns=['Merge'])
    _data_merge['Merge'] = [str([_input_df.loc[i, '用户ID'], _input_df.loc[i, '查询词']]) for i in range(len(_input_df))]
    return _data_merge
    pass


if __name__ == "__main__":
    sogou = pd.read_csv("data/SogouQ.csv", sep=',')

    # merge id and keyword
    data_merge = merge_data(sogou)
    print(data_merge.head())

    search_click_top10 = pd.value_counts(data_merge['Merge'])[0:10]
    print(search_click_top10)

    # output to file
    output = open("result/search_click_top10.txt", 'w+', encoding='utf-8')
    for i, v in search_click_top10.items():
        line = i.strip('[').strip(']').split(', ')
        print(str(eval(line[0])) + "\t" + str(eval(line[1])) + "\t" + str(v), file=output)
