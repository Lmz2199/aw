#-*- coding:utf-8 -*-
import operation_database,operator,random,time
class Mate_keyWords:
    def get_mate_atticle(self,input_key,is_department):
        operation=operation_database.MySQL()
        all_keywords=operation.get_all_keywords(is_department)
        result={}
        time1=time.time()
        for key in all_keywords:
            realKey = key[1].strip().split()
            mate_number = 0
            weight = 0.0
            for input1 in input_key:
                inp = input1.decode('utf-8')
                if inp in realKey:
                    realWeight=key[2].strip().split()
                    mate_number+=1
                    weight+=float(realWeight[realKey.index(inp)])
#                    print key[1].index(input1)
#                    print 'start'+input1+'end'
            weight+=mate_number*0.01
            result[key[0]]=(weight,key[3])
        result=sorted(result.iteritems(),key=operator.itemgetter(1),reverse=True)
        returnResult=result[:]
        for x in returnResult:
            if x[1][1] is not None:
                if time1-float(x[1][1])<300:
                    result.remove(x)
        return result[0:8]
    def get_article_by_id(self,article_id_list):
        operation = operation_database.MySQL()
        article_id=article_id_list[int(random.uniform(0, len(article_id_list)))][0]
        article = operation.get_article_by_id(article_id)
        return article





