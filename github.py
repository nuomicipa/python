#-*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

Base_URL = "https://github.com/login"
Login_URL = "https://github.com/session"

def get_github_html(url):
    '''
    这里用于获取登录页的html，以及cookie
    :param url: https://github.com/login
    :return: 登录页面的HTML,以及第一次的cooke
    '''
    response = requests.get(url)
    first_cookie = response.cookies.get_dict()
    return response.text,first_cookie



def get_token(html):
    '''
    处理登录后页面的html
    :param html:
    :return: 获取csrftoken
    '''
    soup = BeautifulSoup(html,'lxml')
    res = soup.find("input",attrs={"name":"authenticity_token"})
    token = res["value"]
    return token


def gihub_login(url,token,cookie):
    '''
    这个是用于登录
    :param url: https://github.com/session
    :param token: csrftoken
    :param cookie: 第一次登录时候的cookie
    :return: 返回第一次和第二次合并后的cooke
    '''

    data= {
        "commit": "Sign in",
        "utf8":"✓",
        "authenticity_token":token,
        "login":"nuomicipa",
        "password":"love3a87yyq"
    }
    response = requests.post(url,data=data,cookies=cookie)
    print(response.status_code)
    cookie = response.cookies.get_dict()
    #这里注释的解释一下，是因为之前github是通过将两次的cookie进行合并的
    #现在不用了可以直接获取就行
    # cookie.update(second_cookie)
    return cookie


if __name__ == '__main__':
    html,cookie = get_github_html(Base_URL)
    print(cookie)
    token = get_token(html)
    cookie = gihub_login(Login_URL,token,cookie)
    response = requests.get("https://github.com/settings/repositories",cookies=cookie)
    print(response.text)
    print (response.cookies)


# import requests
# def login():
#     url = "http://www.jobbole.com/wp-admin/admin-ajax.php"
#     data = {
#         "action": "user_login",
#         "user_login":"zhaofan1015",
#         "user_pass": '******',
#     }
#     response = requests.post(url,data)
#     cookie = response.cookies.get_dict()
#     print(cookie)
#     url2 ="http://www.jobbole.com/bookmark/"
#     response2 = requests.get(url2,cookies=cookie)
#     print(response2.text)
#
# login()