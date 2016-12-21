#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
__author__ = 'top'
date = '16/11/8'
我爱学习,学习使我快乐
'''
from models import all_models
from random import sample

class hl :

    def __init__(self):

        self.require_keys = [
        ]


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
        for m in all_models:
            b = m["model"]
            l = [a["model"] for a in b]
            c = sample(l,int(m["num"]))
            re += c
        a = '\n        '.join(re) %self.key_words
        return a

if __name__ == '__main__':
    hl = hl()
    print hl.generate_a_article({'jiancheng':'北信科','quancheng':'北京信息科技大学','didian':'北京','shangwu_or_xiawu':'上午'})