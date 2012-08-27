#coding:utf-8
import web
import os
import sys
#import model
from time import sleep
from web.contrib.template import render_mako

import time
month_label = ['Jan','Feb','Mar','Apr','May',\
                'Jun' ,'Jul' ,'Aug' ,'Sep' ,'Oct',\
                'Nov' ,'Dec']
week_label = ['Sun' ,'Mon' ,'Tue' ,'Wed' ,'Thu' ,'Fri' ,'Sta' ,]

web.config.debug = True
#日志对象

def initlog():
    import logging
    logger=logging.getLogger("sina_twitter")
    hd=logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s') 
    hd.setFormatter(fmt)
    logger.addHandler(hd)
    logger.setLevel(logging.DEBUG)
    return logger 


logger=initlog()

 
#url映射配置
urls = (
    '/','Index',
)

app = web.application(urls, globals())
render = render_mako(
        directories=[os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )




#store = web.session.DBStore(model.db, 'weibo_sessions')
#session = web.session.Session(app, store, initializer={'isLogin':0,'userName':'',})
#web.config._session = session


class Index:
    def GET(self):
        user = 'rosickey'
        code = file('basic.js').read().decode('utf-8')
        code2 = 'aacode2'
        return render.hi(user=user,code=code,code2=code2)
    def POST(self):
        data = web.input()
        print '111'
        print data['img']
        f = open('s.png')
        print f.read()
        web.header("Content-Type", "text/html;charset=utf-8")
        return render.hello()

class Updata:
    def GET(self):
        fayan = '每月的'+str(best_date)+'号总有那么几天....～快来通过微博分析分析你的生活吧。http://bigyma.sinaapp.com/'
        web.header("Content-Type", "text/html;charset=utf-8")
        #web.header("Content-type","text/html")
        return render.hello()
 
def notfound():
    web.header("Content-Type", "text/html;charset=utf-8")
    return web.notfound("nooooooooooootfound,尝试刷新一下，F5")

    # You can use template result like below, either is ok:
    #return web.notfound(render.notfound())
    #return web.notfound(str(render.notfound()))

app.notfound = notfound

def internalerror():
    return web.internalerror("wait for a monment,sorry...or you can use F5")

#app.internalerror =  web.debugerror

app.internalerror =  internalerror
if __name__=='__main__':
    #logger.debug("web.py服务开始启动……")
    app.run()