#encoding=utf-8


#    %(name1)s:受理人或者主管部门的称谓
#    %(reason)s:申请原因
#    %(date1)s:申请开始日期
#    %(date2)s:申请结束日期
#    %(number)s:申请请假天数
#    %(name2)s:申请人的名字
#    %(date)s:申请日期


#输入
name1 = "zxj"
yuanyin ="hsahakjhajlk"
date11= "2016.10.1"
date12 = "jsdkj"
date13 = ""
date21 = "2016.10.7"
date22 = "4568"
date23 = "56789"
number = "7"
name2 = "朱星嘉"
date31 = "20160930"
date32 = "72899"
date33 = "89902"



def gen_qjt(Name1,Reason,Date1,Date2,Number,Name2,Date):
    my_map={'name1':Name1,'reason':Reason,'date1':Date1,'date2':Date2,'number':Number,'name2':Name2,'date':Date}
    import random
    rr = random.randint(1, 10)                    # 用于生成一个指定范围内的整数
    filename = './qjt/%(i)s.txt' % {'i': rr}   #用于指定一个随机的模版给当前文件
    file_object = open(filename,'r+')             #打开文件
    try:
        all_the_text = file_object.readlines()
    finally:
        file_object.close()
    re = []
    for b in all_the_text:
        re.append(b%my_map)                         #用字典的值替换key，逐行替换
    return ''.join(re)                             #返回替换好的

print gen_qjt(name1,yuanyin,date11,date21,number,name2,date31)



