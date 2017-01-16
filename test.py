#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
__author__ = 'top'
date = '16/11/8'
我爱学习,学习使我快乐
kx : 开学典礼的程序
sc : 短文本
zj : 总结
'''
import unittest
from programs import kx
from programs import sc
from programs import zj
from programs import zs
from programs import hl

#unicode编码中文每个汉字的len为3
min_at_len = 10*3

class mytest(unittest.TestCase):

    ##初始化工作
    def setUp(self):
        self.kx = kx()
        self.sc = sc()
        self.aw = zj()
        self.hl = hl()
        self.zs = zs()

    #退出清理工作
    def tearDown(self):
        pass

    #测试开学典礼
    def testgenerate_a_article(self):
        parms = {'jiancheng':'北信科','quancheng':'北京信息科技大学','didian':'北京','shangwu_or_xiawu':'上午'}
        at = self.kx.generate_a_article(parms)
        print at
        self.assertGreater(len(at), min_at_len)
    #测试婚礼贺词
    def testhlgenerate_a_article(self):
        parms = {'zhongwu_or_wanshang':'上午','xiansheng':'杨林','xiaojie':'郑国伟'}
        at = self.hl.generate_a_article(parms)
        self.assertGreater(len(at), min_at_len)
    #测试祝寿词
    def testzsgenerate_a_article(self):
        parms = {'name':'王文超','dashou':'三十大寿','age':'24岁','year':'八十年'}
        at = self.zs.generate_a_article(parms)
        self.assertGreater(len(at), min_at_len)

    #测试短文本
    def testgetNotice(self):
        at = self.sc.getNotice("党员发展大会", "全体党员", "2016-11-15 09:00", "评选党员积极分子",
                                "通过前几周的学习和考核评选出积极分子", "党支部书记，副书记及全体学生党员",
                               "教三六阶", "请大家带好笔和本做好笔记",
                                "计算机院办", "2016-11-10 10:00")
        print at
        self.assertGreater(len(at), min_at_len)

    def testregenerateNotice(self):
        at = self.sc.regenerateNotice()
        print at
        self.assertGreater(len(at), min_at_len)

    def testgetCeremony(self):
        at = self.sc.getCeremony("北京信息科技大学", "2016-11-15 09:00", "报告厅", "计算机学院")
        print at
        self.assertGreater(len(at), min_at_len)

    def testregenerateCeremony(self):
        at = self.sc.regenerateCeremony()
        print at
        self.assertGreater(len(at), min_at_len)

    def testgetCoverLetter(self):
        at = self.sc.getCoverLetter("程序员", "bingham", "北京信息科技大学", "计算机应用技术", "NLP",
                        "熟练掌握机器学习算法", "英语六级", "联想集团", "开发测试工程师",
                                    "在实习过程中不断认识自我修正自我", "工作富有责任心")
        print at
        self.assertGreater(len(at), min_at_len)

    def testregenerateCoverLetter(self):
        at = self.sc.regenerateCoverLetter()
        print at
        self.assertGreater(len(at), min_at_len)

    def testgetMeeting(self):
        at = self.sc.getMeeting("20", "2016-11-15 09:00", "北京信息科技大学", "同学会筹备组")
        print at
        self.assertGreater(len(at), min_at_len)

    def testregenerateMeeting(self):
        at = self.sc.regenerateMeeting()
        print at
        self.assertGreater(len(at), min_at_len)
    def testqjt(self):
        p ={
                'name1':'zxj',
                'reason':'hsahakjhajlk',
                'date1':'2016.10.1',
                'date2':'2016.10.7',
                'number':'7',
                'name2':'朱星嘉',
                'date':'20160930'}
        at = self.sc.getQjt(p)
        print at
        self.assertGreater(len(at), min_at_len)

    #测试工作总结
    def testawgenerate_a_article(self):
        at = self.aw.generate_a_article(['学生'])
        self.assertGreater(len(at),min_at_len)

if __name__ =='__main__':
    unittest.main()