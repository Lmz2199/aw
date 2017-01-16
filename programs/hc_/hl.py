#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
__author__ = 'top'
date = '16/11/8'
我爱学习,学习使我快乐
'''
from models import *
from random import sample

class hl :

    def __init__(self):

        self.require_keys = [

        ]
        self.model_map = {
            '领导':{
                '新娘方':lingdao_xinniangfang,
                '新郎方':lingdao_xinlangfang
                  },
            '父母':{
                '新娘方':fumu_xinniangfang,
                '新郎方':fumu_xinlangfang,
            },
            '朋友':{
                '新娘方':binke_xinlangfang,
                '新郎方':binke_xinniangfang,
            },
            '新郎':xinlang,
            '证婚人':zhenghunren
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
        all_models = ''
        if keywords['shenfen']=='新郎':
            all_models = zhenghunren
        elif keywords['shenfen']=='证婚人':
            all_models = zhenghunren
        else:
            all_models = self.model_map[keywords['shenfen']][keywords['which_fang']]
        re = []
        for m in all_models:
            b = m["model"]
            l = [a["model"] for a in b]
            c = sample(l,int(m["num"]))
            re += c
        a = '\n        '.join(re) %self.key_words
        return a

if __name__ == '__main__':
    kx = hl()
    keywords = {
        'zhongwu_or_wanshang':'中午',
        'xiansheng':'郑国伟',
        'xiaojie':'罗玉凤' ,
        'xinlangdanwei':'北京信息科技大学',
        'xinniangdanwei':'家里蹲大学',
        'guanxi':'同学',
        'shenfen':'领导',
        'which_fang':'新娘方'
    }
    print kx.generate_a_article(keywords)