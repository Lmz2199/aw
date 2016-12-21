#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
__author__ = 'top'
date = '16/11/8'
我爱学习,学习使我快乐
'''
import models1
from random import sample

class zs :

    def __init__(self):

        self.require_keys = [

        ]
        self.model_map = {
            '女性':{
                '晚辈':models1.woman_wanbei,
                '主持人':models1.woman_zhuchi
                  },
            '男性':{
                '晚辈':models1.man_wanbei,
                '主持人':models1.man_wanbei,
            }
        }

    def check_keys(self):

        try :
            for k in self.require_keys:
                if k not in self.key_words:
                    raise Exception('require more keys')

        except Exception :
            raise Exception('input keyword format error')

    def generate_a_article(self,keywords):

        self.key_words = keywords
        self.check_keys()

        re = []
        all_models = self.model_map[keywords['xingbie']][keywords['shenfen']]
        for m in all_models:
            b = m["model"]
            l = [a["model"] for a in b]
            c = sample(l,int(m["num"]))
            re += c
        a = '\n        '.join(re) %self.key_words
        return a

if __name__ == '__main__':
    kx = zs()
    keywords = {
        'xingbie':'女性',
        'shenfen':'主持人',
        'bf':'叔叔',
        'nl':'八十',
        'xm':'李长磊',
        'jbdz':'钓鱼台',
        'jtzz':'中南海',
        'fyrbf':'侄子',
        'zbxm':'王文超',
        'jj':'冬季',
        'qtxm':'杨林,郑国伟',
    }
    print kx.generate_a_article(keywords)