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
    dataFile = "result/keys_sorted.csv"
    data = pd.read_csv(dataFile,encoding='utf-8') #从csv数据表中读数据，返回类型为dataframe
    keys = data['key']
    keys0 = keys[0] #得到词频数量前20的关键词
    keys1 = keys[1]
    keys2 = keys[2]
    keys3 = keys[3]
    keys4 = keys[4]
    keys5 = keys[5]
    keys6 = keys[6]
    keys7 = keys[7]
    keys8 = keys[8]
    keys9 = keys[9]
    keys10 = keys[10]
    keys11 = keys[11]
    keys12 = keys[12]
    keys13 = keys[13]
    keys14 = keys[14]
    keys15 = keys[15]
    keys16 = keys[16]


     #保存每个链接关键词出现的次数
    dataFile2 = 'C:/Users/Chinaintern_2/PycharmProjects/keyword_extraction-master/result/keys_TFIDF3.csv'
    data2 = pd.read_csv(dataFile2, encoding='utf-8')  # 从csv数据表中读数据，返回类型为dataframe
    linklist=data2['id']
    titlelist=data2['title']
    keylist=data2['key']
    word_count = [0] * len(linklist)
    print(linklist)
    print(word_count[0])

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split()) #得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys0.find(word_list[index2]) != -1:
                word_count[index] += 3  #给关键词设置权重

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys1.find(word_list[index2]) != -1:
                word_count[index] += 2

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys2.find(word_list[index2]) != -1:
                word_count[index] += 2

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys3.find(word_list[index2]) != -1:
                word_count[index] += 2

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys4.find(word_list[index2]) != -1:
                word_count[index] += 2

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys5.find(word_list[index2]) != -1:
                word_count[index] += 1

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys6.find(word_list[index2]) != -1:
                word_count[index] += 1

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys7.find(word_list[index2]) != -1:
                word_count[index] += 1

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys8.find(word_list[index2]) != -1:
                word_count[index] += 1

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys9.find(word_list[index2]) != -1:
                word_count[index] += 1

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys10.find(word_list[index2]) != -1:
                word_count[index] += 1

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys11.find(word_list[index2]) != -1:
                word_count[index] += 1

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys12.find(word_list[index2]) != -1:
                word_count[index] += 1

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys13.find(word_list[index2]) != -1:
                word_count[index] += 1

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys14.find(word_list[index2]) != -1:
                word_count[index] += 1

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys15.find(word_list[index2]) != -1:
                word_count[index] += 1

    for index in range(len(linklist)):
        text = keylist[index]
        word_list = []
        word_list.extend(text.split())  # 得到这篇文章的关键词列表
        # 查找文章关键词是否在关键词列表中
        for index2 in range(len(word_list)):
            if keys16.find(word_list[index2]) != -1:
                word_count[index] += 1



    print(word_count)
    for index in range(len(keylist)):
        keylist[index] = str( word_count[index])

    result = pd.DataFrame({"id": linklist, "title": titlelist, "count": word_count}, columns=['id', 'title', 'count'])  #这里columns是指定传入列的顺序

    print(result.sort_values(by='count',ascending= False))

    result.sort_values(by='count', ascending=False).to_csv("C:/Users/Chinaintern_2/Desktop/industrialNews_sorted.csv", index=False, encoding='utf-8')



if __name__ == '__main__':
    main()
