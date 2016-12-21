#-*- coding: utf-8 -*-
import mate_keyWords
import logging
class Automatic_writing:
    def getkey(self):
        input_key=[]
        input=raw_input("请输入关键词并以空格隔开：")
        for key in input.split():
            input_key.append(key)
        return input_key

    def action(self,input_key=[]):
        try:
            mate_keyWorder=mate_keyWords.Mate_keyWords()
            articl_id_list=mate_keyWorder.get_mate_atticle(input_key)
            if articl_id_list:
                article=mate_keyWorder.get_article_by_id(articl_id_list)[0][0]
                return article
            return '您输入的关键词有错误'
        except Exception ,e:
            logging.error(e)

if __name__=="__main__":
    au = Automatic_writing()
    print au.action(['你好'])