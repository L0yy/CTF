# -------------------------------------------------------------------------------
# Author:      Crayon
# Created:     26/11/2018
# Copyright:   (c) Crayon 2018
# -------------------------------------------------------------------------------
#!/usr/bin/env python
# coding:utf8
import urllib
import urllib2
import json
from lxml import etree

cookie_list=["analytics=a1e9736d5bda5dc6; PHPSESSID=380af69c33655da453167f8525a7e8ac; YB_SSID=39c54356e682a85ce64961a967c1e306; yiban_user_token=ed990130adcc6b77775552116c11c002; _YB_OPEN_V2_0=M0Jeitvm0lE_S025; laravel_session=eyJpdiI6IlJhUFcySWVSUnp0N0lSSnZVS1wvZkR3PT0iLCJ2YWx1ZSI6InR4aVIxSHVMTDNud09lS3R6UTNMckQ4YWc0T1hoVjFmMmRraTk0QVdJNk0rSmFwcjlTdVIxeDJFckdFZGRXSmE4c2pQWkw2dDRsR1VVZGlwbERWbmNBPT0iLCJtYWMiOiI0Mjg3OTY4MDRmZjIwZWQwMjk2YzI5Nzc4ZTlhMDM2YWQ0YjZkMmE5Y2Y4YzIxN2E3ZjRlYTNkODIxMThjMDMzIn0%3D"]
xh=['16310520331',]
bj=['123456',]

def get_id(cookie,urll,code):
    #选课页面的url
    #cookie都是个人的
    #code是选课页面上获取到的值
    url111 = 'https://q.yiban.cn/signup/getSignupAjax'
    # 18382558318
    # ray5310.
    head = {
        "Cookie": cookie,
        "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Host": "q.yiban.cn   ",
        "Origin": "https://q.yiban.cn  ", }

    App_id = urll.split('/')[-1]
    #print App_id
    formdata = {
        "App_id": App_id,
        "code": code
    }
    data = urllib.urlencode(formdata)
    request = urllib2.Request(url111, data=data, headers=head)
    response = urllib2.urlopen(request)
    print response.read().decode('utf-8').split(":")
    #return response.read().decode('unicode_escape').encode('utf-8').split(":")[4]

def get_code(urll,cookie):
    #返回选课所用code值
    head = {
        "Cookie": cookie,
        "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
         }
    request = urllib2.Request(urll, headers=head)
    response = urllib2.urlopen(request)
    html = etree.HTML(response.read())
    #dd =  response.read().decode('unicode_escape').encode('utf-8')
    js_data = html.xpath('/html/head/script[1]/text()')
    #print js_data[0]
    #ss = str(js_data[0].encode('utf-8')).replace(' ','').split(',')[35].split(':')[-1]
    ss = str(js_data[0].encode('utf-8')).split(',')
    print ss
    for k1 in range(len(ss)):
        print k1,ss[k1]

    #return eval(ss)

def tijiao(cookie,id,xh,bj):
    url = "https://q.yiban.cn/signup/insertBoxAjax"
    formdata1 = {
    "App_id":" 347958  ",
    "id":str(id),
    "flag":" 1" ,
    "answers[]":str(xh) ,
    "answers[]":str(bj),
    }
    head = { "Cookie": cookie,
        "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
       }
    request = urllib2.Request(url,data=formdata1, headers=head)
    response = urllib2.urlopen(request)
    response_texte = response.text().decode('unicode_escape').encode('utf-8')
    return response_texte


def main():
    urll = 'https://q.yiban.cn/app/index/appid/347958'
    for i in range(len(cookie_list)):
        code = get_code(urll,cookie_list[i])
        #id = get_id(cookie_list[i],urll,code)
        #print tijiao(cookie_list[i],id,xh[i],bj[i])
        break
if __name__ == '__main__':
    main()




