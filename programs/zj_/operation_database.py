#coding=utf-8
import sqlite3,time
import os
import logging
class MySQL:
    def __init__(self):
        self.logger = logging.getLogger('operation_database')
        try:
            db_file_path =  os.path.join(os.path.dirname(__file__),'database/automatic_write.db')
            self.conn=sqlite3.connect(db_file_path)
            self.logger.info('open database successfully')
        except Exception, e:
            self.logger.error(e)

    def insert_feature(self,feature):
        content ="".join(feature['content'])
        weight =" ".join(feature['weight'])
        feature_words =" ".join(feature['feature_words'])
        feature_phrase =" ".join(feature['feature_phrase'])
        abstract ="".join(feature['abstract'])
        list=(content,feature_words,weight,feature_phrase,abstract,1,1)
        print content
        print feature_words
        print feature_phrase
        print abstract
        sql='insert into article (content,feature_words,feature_words_weight,feature_phrase,abstract,is_article,is_department) values (?,?,?,?,?,?,?)'
        self.conn.execute(sql,list)
#        self.cur.execute("insert into text (content,feature_words,feature_phrase,abstract) values ('1','2','3','4')")
        self.conn.commit()
        self.conn.close()
        self.logger.info('close database successfully')
    def get_all_keywords(self,is_department):
        sql='select id,feature_words,feature_words_weight,last_access from article where is_article=1 and is_department=?'
        cu = self.conn.cursor()
        cu.execute(sql,(is_department,))
        info=cu.fetchall()
        self.conn.commit()
        self.conn.close()
        self.logger.info('close database successfully')
        return info
    def get_article_by_id(self,article_id):
        print article_id
        sql='select content from article where is_article=1 and id =? '
        cu = self.conn.cursor()
        para=(article_id,)
        cu.execute(sql,para)
        article = cu.fetchall()
        time1 = time.time()
        sql='update article set last_access =? where id =?'
        cu.execute(sql,(time1,article_id))
        self.conn.commit()
        self.conn.close()
        self.logger.info('close database successfully')
        return article






