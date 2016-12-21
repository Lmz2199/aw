#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
__author__ = 'top'
date = '16/11/8'
我爱学习,学习使我快乐
'''
import sys
from werkzeug import security
from flask import Flask, request,Response
import json
UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

'''file = request.files['file']
if file and allowed_file(file.filename):
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
'''


'''
加载各组的程序到内存
'''
from programs import kx
from programs import sc
from programs import zj
from programs import hl
from programs import zs

kx = kx()
sc = sc()
zj = zj()
hl = hl()
zs = zs()

app = Flask(__name__)

app.debug=True

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.errorhandler(404)
def page_not_found(e):
    return '{"error":"404"}'

@app.errorhandler(400)
def page_not_found(e):
    return '{"error":"parms error"}'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET'])
def welcome():
    a = Response("")
    a.headers['Access-Control-Allow-Origin'] = '*'
    a.data = json.dumps({"status":"ok"})
    return a


#测试页面

@app.route('/test',methods=['GET','POST'])
def test():
    a = Response("")
    a.headers['Access-Control-Allow-Origin'] = '*'
    a.data = json.dumps({"r":"ok"})
    return a

#贺词
@app.route('/hc',methods=["POST","GET"])
def hc_():
    a = Response("")
    a.headers['Access-Control-Allow-Origin'] = '*'
    if request.method=='POST':
        data = request.form
    else:
        data = request.values
    re = ''
    if(data.getlist('type')[0]=='hl'):
        parms = {
                    'zhongwu_or_wanshang':data.getlist('p1')[0].encode('utf-8'),
            'xiansheng':data.getlist('p2')[0].encode('utf-8'),
            'xiaojie':data.getlist('p3')[0].encode('utf-8')
        }
        re = hl.generate_a_article(parms)
    if(data.getlist('type')[0]=='zs'):
        parms = {
            'name':data.getlist('p1')[0].encode('utf-8'),
            'dashou':data.getlist('p2')[0].encode('utf-8'),
            'age':data.getlist('p3')[0].encode('utf-8'),
            'year':data.getlist('p4')[0].encode('utf-8'),
        }
        re = zs.generate_a_article(parms)
    a.data = json.dumps({"r":re})
    return a


## 工作总结
@app.route('/zj',methods=["POST","GET"])
def zongjie():
    a = Response("")
    a.headers['Access-Control-Allow-Origin'] = '*'

    if request.method=='POST':
        data = request.form
    else:
        data = request.values

    keywords = data.getlist('keywords')
    keywords = keywords[0].encode('utf-8')
    keywords = keywords.replace('，',',')
    keywords = keywords.split(',')
    try :
        b = zj.generate_a_article(keywords)
    except:
        b = ''
    a.data = json.dumps({"r":b})
    return a

## 部门工作总结
@app.route('/zj1',methods=["POST","GET"])
def gerenzongjie():
    a = Response("")
    a.headers['Access-Control-Allow-Origin'] = '*'

    if request.method=='POST':
        data = request.form
    else:
        data = request.values

    keywords = data.getlist('keywords')
    keywords = keywords[0].encode('utf-8')
    keywords = keywords.replace('，',',')
    keywords = keywords.split(',')
    try :
        b = zj.generate_a_article(keywords,1)
    except:
        b = ''
    a.data = json.dumps({"r":b})
    return a

#开学典礼

@app.route('/kx',methods=["POST","GET"])
def kaixue():
    a = Response("")
    a.headers['Access-Control-Allow-Origin'] = '*'

    if request.method=='POST':
        data = request.form
    else:
        data = request.values
    parms = {'jiancheng':data.getlist('p1')[0].encode('utf-8'),'quancheng':data.getlist('p2')[0].encode('utf-8'),'didian':data.getlist('p3')[0].encode('utf-8'),'shangwu_or_xiawu':data.getlist('p4')[0].encode('utf-8')}

    try :
        b = kx.generate_a_article(parms)
    except:
        b = ''
    a.data = json.dumps({"r":b.decode('utf-8')})
    return a

#短文本

@app.route('/sc',methods=["POST","GET"])
def short_content():
    a = Response("")
    a.headers['Access-Control-Allow-Origin'] = '*'
    b = ''
    if request.method=='POST':
        data = request.form
    else:
        data = request.values
    try:
        type = data.getlist('type')[0]
        if (type=='CoverLetter'):
            b = sc.getCoverLetter(
                data.getlist('p1')[0],
                data.getlist('p2')[0],
                data.getlist('p3')[0],
                data.getlist('p4')[0],
                data.getlist('p5')[0],
                data.getlist('p6')[0],
                data.getlist('p7')[0],
                data.getlist('p8')[0],
                data.getlist('p9')[0],
                data.getlist('p10')[0],
                data.getlist('p11')[0],
                              )
        if(type=='Notice'):
            b = sc.getNotice(
                data.getlist('p1')[0],
                data.getlist('p2')[0],
                data.getlist('p3')[0],
                data.getlist('p4')[0],
                data.getlist('p5')[0],
                data.getlist('p6')[0],
                data.getlist('p7')[0],
                data.getlist('p8')[0],
                data.getlist('p9')[0],
                data.getlist('p10')[0],
            )

        if(type=='Ceremony'):
            b = sc.getCeremony(
                data.getlist('p1')[0],
                data.getlist('p2')[0],
                data.getlist('p3')[0],
                data.getlist('p4')[0],
                )

        if(type=='Meeting'):
            b = sc.getMeeting(
                data.getlist('p1')[0],
                data.getlist('p2')[0],
                data.getlist('p3')[0],
                data.getlist('p4')[0],
                )

        if(type=='Qjt'):
            parms = {
                'name1':data.getlist('p1')[0].encode('utf-8'),
                'reason':data.getlist('p2')[0].encode('utf-8'),
                'date1':data.getlist('p3')[0].encode('utf-8'),
                'date2':data.getlist('p4')[0].encode('utf-8'),
                'number':data.getlist('p5')[0].encode('utf-8'),
                'name2':data.getlist('p6')[0].encode('utf-8'),
                'date':data.getlist('p7')[0].encode('utf-8')}
            b = sc.getQjt(parms)

    except:
        b=''

    a.data = json.dumps({"r":b.decode('utf-8')})
    return a

from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    try:
        port_number = int(sys.argv[1])
    except:
        port_number = 3005
    app.run(host='0.0.0.0', port=port_number)