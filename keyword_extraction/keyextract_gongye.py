#!/usr/bin/python
# coding=utf-8
# 采用TF-IDF方法提取文本关键词
# http://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting
import sys,codecs
import pandas as pd
import numpy as np
import jieba.posseg
import jieba.analyse
from collections import Counter
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from itertools import chain
"""
       TF-IDF权重：
           1、CountVectorizer 构建词频矩阵
           2、TfidfTransformer 构建tfidf权值计算
           3、文本的关键字
           4、对应的tfidf矩阵
"""
# 数据预处理操作：分词，去停用词，词性筛选
def dataPrepos(text, stopkey):
    l = []
    pos = ['n', 'nz', 'v', 'vd', 'vn', 'l', 'a', 'd']  # 定义选取的词性
    seg = jieba.posseg.cut(text)  # 分词
    for i in seg:
        if i.word not in stopkey and i.flag in pos:  # 去停用词 + 词性筛选
            l.append(i.word)
    return l

# tf-idf获取文本top10关键词
def getKeywords_tfidf(data,stopkey,topK):
    #idList, titleList, abstractList = data['id'], data['title'], data['abstract']
    urlList, titleList, abstractList = data['link'], data['title'], data['article'] #所有的输入数据表都包含这三列
    corpus = [] # 将所有文档的分词结果输出到一个list中，一行代表一个文档
    for index in range(len(urlList)):
        #text = titleList[index] #只用标题参与
        text = '%s。%s' % (titleList[index], abstractList[index]) # 拼接标题和正文文本
        text = dataPrepos(text,stopkey)  # 文本预处理，包括分词
        text = " ".join(text)  # 连接成字符串，空格分隔
        corpus.append(text)

    # 1、构建词频矩阵，将文本中的词语转换成词频矩阵
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus) # 词频矩阵,a[i][j]:表示j词在第i个文本中的词频
    # 2、统计每个词的tf-idf权值
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(X)
    # 3、获取词袋模型中的关键词
    word = vectorizer.get_feature_names()
    # 4、获取tf-idf矩阵，a[i][j]表示j词在i篇文本中的tf-idf权重
    weight = tfidf.toarray()
    # 5、打印词语权重
    ids, titles, keys = [], [], []
    for i in range(len(weight)): #对每篇文章进行一次循环，得到对应的关键词列表
        print u"-------这里输出第", i+1 , u"篇文本的词语tf-idf------"
        ids.append(urlList[i])
        titles.append(titleList[i])
        df_word,df_weight = [],[] # 当前文章的所有词汇列表、词汇对应权重列表
        for j in range(len(word)):
            print word[j],weight[i][j]
            df_word.append(word[j])
            df_weight.append(weight[i][j])
        df_word = pd.DataFrame(df_word,columns=['word'])
        df_weight = pd.DataFrame(df_weight,columns=['weight'])
        word_weight = pd.concat([df_word, df_weight], axis=1) # 拼接词汇列表和权重列表
        word_weight = word_weight.sort_values(by="weight",ascending = False) # 按照权重值降序排列
        keyword = np.array(word_weight['word']) # 选择词汇列并转成数组格式
        word_split = [keyword[x] for x in range(0,topK)] # 抽取前topK个词汇作为关键词
        word_split = " ".join(word_split) #每一篇文章的关键词转成字符串
        keys.append(word_split.encode("utf-8")) #往字符串数组后面添加关键词字符串元素

    result = pd.DataFrame({"id": ids, "title": titles, "key": keys},columns=['id','title','key']) #把三列数组合并成数据框
    return result #返回的result是一个数据框


def main():
    # 读取数据集
    #dataFile = 'data/sample_data.csv' 在同一根目录下的情况
    dataFile1 = 'C:/Users/Chinaintern_2/Documents/newschanyexinxi.csv' #爬取的网站新闻数据
    data1 = pd.read_csv(dataFile1) #从csv数据表中读数据
    dataFile2 = 'C:/Users/Chinaintern_2/Documents/newsgongyexinwen.csv'
    data2 = pd.read_csv(dataFile2)
    dataFile3 = 'C:/Users/Chinaintern_2/Documents/newsdianzigongchen.csv'
    data3 = pd.read_csv(dataFile3)


    # 停用词表
    stopkey = [w.strip() for w in codecs.open('data/stopWord.txt', 'r').readlines()]
    # tf-idf关键词抽取
    result = getKeywords_tfidf(data1,stopkey,4) #返回类型为数据框
    result2 = getKeywords_tfidf(data2, stopkey, 4)
    result3 = getKeywords_tfidf(data3, stopkey, 4)

    resultfinal= result.append([result2,result3]) #要拼接大于一个的，括号里用[result1,result2,...]
    print(resultfinal)
    resultfinal.to_csv("result/keys_gongye.csv",encoding= 'utf-8', index=False)



if __name__ == '__main__':
    main()
