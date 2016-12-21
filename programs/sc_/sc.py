# -*-coding:utf-8 -*-
import os
import logging
import random

class sc:

    def __init__(self):
        '''
        os environment must be seted before import autoclass
        '''
        self.current_path = os.path.dirname(__file__)
        jar_file_path =  os.path.join(os.path.dirname(__file__),'short-context.jar')
        os.environ['CLASSPATH'] = jar_file_path
        from jnius import autoclass
        self.logger = logging.getLogger('short-context')
        self.logger.info('jar file path is '+jar_file_path)
        NC =  autoclass('com.shortContextApplication.NoticeController')
        IC =  autoclass('com.shortContextApplication.InvitationController')
        CLP =  autoclass('com.shortContextApplication.CoverLetterController')
        self.nc = NC()
        self.ic = IC()
        self.clp = CLP()


    def getCoverLetter(self,*parm):
        try:
            self.logger.info('getCoverLetter')
            re =  self.clp.getCoverLetter(*parm)
            return re
        except Exception ,e:
            self.logger.error(e)
            return ''

    def regenerateCoverLetter(self):
        try:
            self.logger.info('regenerateCoverLetter')
            re =  self.clp.regenerateCoverLetter()
            return re
        except Exception ,e:
            self.logger.error(e)
            return ''

    def getCeremony(self,*parm):
        try:
            self.logger.info('getCeremony')
            re =  self.ic.getCeremony(*parm)
            return re
        except Exception ,e:
            self.logger.error(e)
            return ''

    def regenerateCeremony(self):
        try:
            self.logger.info('regenerateCeremony')
            re =  self.ic.regenerateCeremony()
            return re
        except Exception ,e:
            self.logger.error(e)
            return ''

    def getMeeting(self,*parm):
        try:
            self.logger.info('getMeeting')
            re =  self.ic.getMeeting(*parm)
            return re
        except Exception ,e:
            self.logger.error(e)
            return ''

    def regenerateMeeting(self):
        try:
            self.logger.info('regenerateMeeting')
            re =  self.ic.regenerateMeeting()
            return re
        except Exception ,e:
            self.logger.error(e)
            return ''

    def getNotice(self,*parm):
        try:
            self.logger.info('getNotice')
            re =  self.nc.getNotice(*parm)
            return re
        except Exception ,e:
            self.logger.error(e)
            return ''
    def regenerateNotice(self):
        try:
            self.logger.info('regenerateNotice')
            re =  self.nc.regenerateNotice()
            return re
        except Exception ,e:
            self.logger.error(e)
            return ''

    def getQjt(self,parm ):
        my_map=parm
        rr = random.randint(1, 10)                    # 用于生成一个指定范围内的整数
        filename = self.current_path+'/qjt/%(i)s.txt' % {'i': rr}   #用于指定一个随机的模版给当前文件
        file_object = open(filename,'r+')             #打开文件
        try:
            all_the_text = file_object.readlines()
        finally:
            file_object.close()
        re = []
        for b in all_the_text:
            re.append(b%my_map)                         #用字典的值替换key，逐行替换
        return ''.join(re)
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    a = []
    m = sc()
    a.append(m.getNotice("党员发展大会", "全体党员", "2016-11-15 09:00", "评选党员积极分子",
                            "通过前几周的学习和考核评选出积极分子", "党支部书记，副书记及全体学生党员", "教三六阶", "请大家带好笔和本做好笔记",
                            "计算机院办", "2016-11-10 10:00"))
    a.append(m.regenerateNotice())

    a.append(m.getCeremony("北京信息科技大学", "2016-11-15 09:00", "报告厅", "计算机学院"))
    a.append(m.regenerateCeremony())

    a.append(m.getCoverLetter("程序员", "bingham", "北京信息科技大学", "计算机应用技术", "NLP",
                    "熟练掌握机器学习算法", "英语六级", "联想集团", "开发测试工程师", "在实习过程中不断认识自我修正自我", "工作富有责任心"))
    a.append(m.regenerateCoverLetter())

    a.append(m.getMeeting("20", "2016-11-15 09:00", "北京信息科技大学", "同学会筹备组"))
    a.append(m.regenerateMeeting())

    print a