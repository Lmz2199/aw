#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
__author__ = 'top'
date = '16/11/8'
我爱学习,学习使我快乐
'''
'''
问候语 套话
shangwu_or_xiawu :上午 下午 中午 早上
'''

model_1 = [
    {
      "model":"老师们、同学们：大家好!"
    },
    {
      "model":"尊敬的老师们、亲爱的同学们：大家%(shangwu_or_xiawu)s好！"
    },
    {
      "model":"老师们、同学们：%(shangwu_or_xiawu)s好!！"
    },
    {
      "model":"老师们、同学们：大家%(shangwu_or_xiawu)s好！"
    },
    {
      "model":"老师们、同学们："
    },
    {
      "model":"尊敬的老师、亲爱的同学们："
    },
    {
      "model":"各位老师，同学们："
    },
    {
      "model":"尊敬的老师们，亲爱的同学们："
    },
    {
      "model":"亲爱的老师们，同学们："
    },
    {
      "model":"敬爱的各位老师、亲爱的孩子们:"
    },
    {
      "model":"尊敬的老师们、亲爱的同学们，%(shangwu_or_xiawu)s好！"
    },
  ]