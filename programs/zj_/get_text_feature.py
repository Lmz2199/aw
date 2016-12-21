#-*- encoding:utf-8 -*-
from __future__ import print_function
import operation_database
import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import sys
import os
class Get_text_feature:
    def get_text_feature(self,file):
        try:
            reload(sys)
            sys.setdefaultencoding('utf-8')
        except:
            pass
        path=os.getcwd()
        file=path+'\\file\\'+file
        text = codecs.open(file, 'r', 'utf-8').read()
        tr4w = TextRank4Keyword()
        feature={}
        tr4w.analyze(text=text, lower=True, window=3)   # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
        feature['content']=text

        print( '关键词：' )
        weight=[]
        feature_keywords=[]
        for item in tr4w.get_keywords(10, word_min_len=1):
            feature_keywords.append(item.word)
            weight.append(str(item.weight))
        print(len(feature))
        feature['feature_words']=feature_keywords
        feature['weight']=weight
#keywords
        print( '关键短语：' )
        feature_phrase=[]
        for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2):
            feature_phrase.append(phrase)
        feature['feature_phrase']=feature_phrase

        tr4s = TextRank4Sentence()
        tr4s.analyze(text=text, lower=True, source = 'all_filters')
        print( '摘要：')
        abstract = []
        for item in tr4s.get_key_sentences(num=3):
#            feature.append(item.weight)
            abstract.append(item.sentence+' ')
            print(len(feature))
        feature['abstract']=abstract
        operation_database.MySQL().insert_feature(feature)

if __name__=='__main__':
    get_text_feature=Get_text_feature()
    path=os.getcwd()+'\\file'
    for file in os.listdir(path):
        print (file)
        get_text_feature.get_text_feature(file)

