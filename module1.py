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

cookie=[" PHPSESSID=67fe8fd7db50bcd90cd7fe7a96dc0ed3; analytics=a1e9736d5bda5dc6; YB_SSID=ffe4913b505498862df03b68bb9d784c; yiban_user_token=ed990130adcc6b77775552116c11c002; timezone=-8; _YB_OPEN_V2_0=h0T_5YmllK0v20f1; laravel_session=eyJpdiI6InpSdzJ2TTJtU1wvbDdBOXl3V09tSjhBPT0iLCJ2YWx1ZSI6InJUZTVNbjQzRGxpYjllbVl6aUhTK2E1RmFOeDJhRkFsdmJwRmR6TDJRTjM4eStHbVFXNlVDSndNbnZoUm0wR0NsNHdQWmRFanpkVEI2ampxTktuT0VRPT0iLCJtYWMiOiI4NjlkN2JlYzk5OTgxOGUzOWRiNGZkMjVlNjU1MjhlZmMwMjRiN2RmM2VhZGMyMzYzYzk2N2I4NzE1NTYwZDkzIn0%3D",
]
xh=['16310520331']
bj=['123456']

def get_id(cookie,urll,code):
    #选课页面的url
    #cookie都是个人的
    #code是选课页面上获取到的值
    url = 'https://q.yiban.cn/signup/getSignupAjax'
    # 18382558318
    # ray5310.
    head = {
        "Cookie": cookie,
        "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Host": "q.yiban.cn   ",
        "Origin": "https://q.yiban.cn  ", }

    App_id = urll.split('/')[-1]
    formdata = {
        "App_id": App_id,
        "code": code
    }
    data = urllib.urlencode(formdata)
    request = urllib2.Request(url, data=data, headers=head)
    response = urllib2.urlopen(request)
    return response.read().decode('unicode_escape').split(":")[4]

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
    ss = str(js_data[0].encode('utf-8')).replace(' ','').split(',')[35].split(':')[-1]
    return eval(ss)




def main():
    urll = 'https://q.yiban.cn/app/index/appid/347958'
    for i in cookie_list:
        code = get_code(urll,cookie)
        id = str(get_id(cookie,urll,code))
        tijiao(id,xh,bj)
def tijiao(id,xh,bj):
    url1 = "https://q.yiban.cn/signup/insertBoxAjax"
    formdata1 = {
    "App_id":" 347958  ",
    "id":str(id),
    "flag":" 1" ,
    "answers[]":str(xh) ,
    "answers[]":str(bj),
    }
if __name__ == '__main__':
    main()




