#-*- coding: utf-8 -*-
import mate_keyWords
class zj:
    import mate_keyWords
    def getkey(self):
        input_key=[]
        input=raw_input("请输入关键词并以空格隔开：")
        for key in input.split():
            input_key.append(key)
        return input_key

    def generate_a_article(self,input_key=[],type=0):
        try:
            mate_keyWorder=mate_keyWords.Mate_keyWords()
            articl_id_list=mate_keyWorder.get_mate_atticle(input_key,type)
            if articl_id_list:
                article=mate_keyWorder.get_article_by_id(articl_id_list)[0][0]
                return article
            return '您输入的关键词有错误'
        except Exception ,e:
            raise e


if __name__=="__main__":
    au = zj()
    private_article=au.generate_a_article(['你好'])
    print private_article
    department_article=au.generate_a_article(['你好'],1)
    print department_article
