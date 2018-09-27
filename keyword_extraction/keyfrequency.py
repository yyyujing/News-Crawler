#!/usr/bin/python
#coding=utf-8
# -*- coding: UTF-8 -*-
# 采用TF-IDF方法提取文本关键词
# http://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting
import sys,codecs
import pandas as pd
import json
from collections import Counter



def main():
    # 读取数据集
    dataFile = 'C:/Users/Chinaintern_2/PycharmProjects/keyword_extraction-master/result/keys_TFIDF3.csv'
    data = pd.read_csv(dataFile,encoding='utf-8') #从csv数据表中读数据，返回类型为dataframe
    keys = data['key']
    word_lst = []
    word_dict = {}
    for index in range(len(keys)):
        word_lst.extend(keys[index].split()) #把所有的关键词按照空格分割并存入列表
    for index in range(len(word_lst)):
        print(word_lst[index])
    print(len(word_lst))
    for item in word_lst:
        if item not in word_dict:
            word_dict[item] = 1
        else:
            word_dict[item] += 1

    print(json.dumps(word_dict,encoding='utf-8',ensure_ascii= False)) #打印字典里的中文

    c=Counter(word_dict).most_common()
    for index in range(len(word_dict)):
        print(json.dumps(c[index], encoding='utf-8', ensure_ascii=False)) #打印列表中的中文fantastic!!!!

    keydata=pd.DataFrame(c) #这里可以直接将嵌套列表转为数据框
    keydata.columns = ['key','frequency']

    print(keydata)
    keydata.to_csv("result/keys_sorted.csv", index=False, encoding='utf-8')#EXCEL是无法直接打开UTF-8编码的CSV中文文件的，需要使用记事本打开


if __name__ == '__main__':
    main()
