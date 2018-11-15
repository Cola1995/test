from django.shortcuts import render,HttpResponse
import requests
import time
import re
import json
from bs4 import BeautifulSoup
# Create your views here.


def ticket(html):
    tdict={}
    soup=BeautifulSoup(html,'html.parser')
    tag=soup.find(name='error').find_all()
    for t in tag:
        tdict[t.name]=t.text

    return tdict

def login(req):
    if req.method=='GET':
        uuid_time=int(time.time()*1000)  #获取时间戳
        base_uuid_url='https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}'
        uuid_url=base_uuid_url.format(uuid_time)  #格式化URL 传入uuid_time
        r1=requests.get(uuid_url)  #请求地址
        #print(r1.text)
        result=re.findall('= "(.*)";',r1.text)
        #print(result)
        uuid=result[0]

        req.session['UUID_TIME']=uuid_time  #存入session
        req.session['UUID']=uuid
        return render(req,'login.html',{'uuid':uuid})

def check_login(req):

    response={'code':408,'data':None}
    c_time = int(time.time() * 1000)
    base_login_url="https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip=0&r=1457378564&_={1}"
    login_url=base_login_url.format(req.session['UUID'],c_time)
    r=requests.get(login_url)
    print(r.text)
    if 'window.code=408' in r.text:
        #无人扫码
        response['code']=408
        print('无人扫码')
    elif 'window.code=201' in r.text:
        #扫码获取头像
        response['code']=201
        response['data']=re.findall("window.userAvatar = '(.*)='",r.text)[0]

    #print(r.text)
    elif 'window.code=200' in r.text:
        #点击登录
        req.session['LOGIN_COOKIES']=r.cookies.get_dict()
        base_redirect_url=re.findall('redirect_uri="(.*)";',r.text)[0]
        redirect_url=base_redirect_url+'&fun=new&version=v2'

        #获取凭证
        r2=requests.get(redirect_url)
        ticket_dict=ticket(r2.text)
        #print(ticket_dict)
        req.session['TICKET_DICT']=ticket_dict   #存入session
        req.session['TICKET_COOKIES']=r2.cookies.get_dict()
        #初始化，获取最近联系人信息

        post_data = {
            "BaseRequest": {
                "DeviceID": "e876442388480809",
                'Sid': ticket_dict['wxsid'],
                'Uin': ticket_dict['wxuin'],
                'Skey': ticket_dict['skey'],
            }
        }
        init_url='https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=1442528109&lang=zh_CN&pass_ticket={0}'.format(ticket_dict['pass_ticket'])
        r3=requests.post(
            url=init_url,
            json=post_data

        )
        # print(r3.text)
        r3.encoding='utf-8'
        init_dict=json.loads(r3.text)  #将json数据转换为字典
        print(init_dict)
        # for k,v in init_dict.items():
        #      print(k,v)

        req.session['INIT_DICT']=init_dict
        response['code']=200
        pass

    return HttpResponse(json.dumps(response))

def avatar(req):   #获取头像的方法
    prav=req.GET.get('prav')
    username=req.GET.get('username')
    skey = req.GET.get('skey')
    img_url = "https://wx.qq.com{0}&username={1}&skey={2}".format(prav, username, skey)
    #rimg = requests.get(img_url, headers={'Referer': 'https://wx.qq.com/'})
    #print(img_url)
    cookies = {}
    cookies.update(req.session['LOGIN_COOKIES'])
    cookies.update(req.session['TICKET_COOKIES'])
    #print(img_url)
    res = requests.get(img_url, cookies=cookies, headers={'Content-Type': 'image/jpeg'})
    return HttpResponse(res.content)

def index(req):
    '''
    显示最近联系人
    :param req:
    :return:
    '''
    return render(req,'index.html')
def contact_list(req):
    '''
    获取所有联系人
    :param req:
    :return:
    '''
    ctime = int(time.time() * 1000)
    base_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&r={0}&seq=0&skey={1}&pass_ticket{2}"
    url = base_url.format(ctime, req.session['TICKET_DICT']['skey'],req.session['TICKET_DICT']['pass_ticket'])
    cookies = {}
    cookies.update(req.session['LOGIN_COOKIES'])
    cookies.update(req.session['TICKET_COOKIES'])



    r1 = requests.get(url, cookies=cookies)
    r1.encoding = 'utf-8'
    print(r1.text)

    user_list = json.loads(r1.text)
    public=[]
    public_nickname=[]
    for p in user_list['MemberList']:   #获取ContactFlay为3的联系人信息  24服务号 8 公众号
        if int(p['VerifyFlag'])==8 or int(p['VerifyFlag'])==24:
        #if int(p['ContactFlag']) == 1 and int(p['VerifyFlag'])!=8 and int(p['VerifyFlag'])!=24 and int(p['VerifyFlag'])!=29:   #联系人

            public.append(p['UserName'])
            public_nickname.append(p['NickName'])
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # print( public)
    user_public=public
    pcount=len(user_public)
    req.session['use1r_dict'] = user_public
    return render(req, 'contact_list.html', {'user_list': user_list,'pcount':pcount,'public':public,'public_nickname':public_nickname})

def send_msg(req):
    """
    发送消息
    :param req:
    :return:
    """
    response={"count":None}
    current_user = req.session['INIT_DICT']['User']['UserName'] # session初始化，User.UserName
    #to = req.POST.get('to') # @dfb23e0da382f51746575a038323834a
    i=int(req.POST.get('index'))
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # print(type(i))

    msg = req.POST.get('msg')# asdfasdfasdf
    # print('_____________________________')
    # print(type(to))
    # print(to)
    # session Ticket
    # session Cookie
    ticket_dict = req.session['TICKET_DICT']
    username_list=req.session['use1r_dict']
    # for i in user_dict['MemberList']:
    #     print(i['UserName'])

    #print(username_list['MemberList'][i]['UserName'])
    count=int(len(username_list))  #联系公众号总数
    response['count']=count

    ctime = int(time.time() * 1000)
    post_data = {
        "BaseRequest":{
            "DeviceID": "e384757757885382",
            'Sid': ticket_dict['wxsid'],
            'Uin': ticket_dict['wxuin'],
            'Skey': ticket_dict['skey'],
        },
        "Msg":{
            "ClientMsgId":ctime,
                "LocalID":ctime,
            "FromUserName": current_user,
            "ToUserName":username_list[i],
            "Content": msg,
            "Type": 1
        },
        "Scene": 0
    }

    url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?pass_ticket={0}".format(ticket_dict['pass_ticket'])
    # res = requests.post(url=url,json=post_data) # application/json,json.dumps(post_data)
    # res = requests.post(url=url,data=json.dumps(post_data),headers={'Content-Type': "application/json"}) # application/json,json.dumps(post_data)

    res = requests.post(url=url,data=json.dumps(post_data,ensure_ascii=False).encode('utf-8'),headers={'Content-Type': "application/json"}) # application/json,json.dumps(post_data)
    #print(res.text)
    return HttpResponse('...')