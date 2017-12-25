# -*- coding: utf-8 -*-
from httplib2 import Http
from urllib.robotparser import RobotFileParser
from html.parser import unescape
# from urllib.parse import url
#from reppy.robots import Robots
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from google import search
from http.cookiejar import LWPCookieJar
from urllib.request import Request, urlopen
import os

# SAMPLE_URL = 'https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%A1%E3%83%AA%E3%82%AB%E8%88%AA%E7%A9%BA%E5%AE%87%E5%AE%99%E5%B1%80'
# SAMPLE_URL = 'http://www.cyclowired.jp/robots.txt'
SAMPLE_URL = 'http://www.google.co.jp/search?q=integer'

home_folder = os.getenv('HOME')
if not home_folder:
    home_folder = os.getenv('USERHOME')
    if not home_folder:
        home_folder = '.'   # Use the current folder on error.
cookie_jar = LWPCookieJar(os.path.join(home_folder, '.google-cookie'))
# print (os.path.join(home_folder, '.google-cookie'))
try:
    cookie_jar.load()
except Exception:
    pass
USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'

def http_req():

    html = googe_search(SAMPLE_URL)


    soup = BeautifulSoup(html, 'lxml')
    aList = soup.find_all("a")

    with open('hoge.html', 'wb') as file:
        for a in aList:
            file.write(a.encode())

    # dammit = UnicodeDammit(html)


    # print(dammit.unicode_markup)
    # print(dammit.original_encoding)

    # print (html.decode(encoding='utf-8', errors='ignore'))
    # soup = BeautifulSoup(html, "html.parser")
    # print (soup.prettify())
    # aList = soup.find_all('p')
    # for a in aList:
    #     print (a)

    # print (html)
    # for url in search('腰痛', stop=20, lang='ja'):
    #     print (url)
        # soup = BeautifulSoup(urllib.urlopen(url))
        # print soup.find("title").text

    # h = Http()
    # headers = {}
    # (response, content) = h.request(SAMPLE_URL, headers=headers)

    # items = dict(response.items())
    # for key,value in response.items():

    #     if (key != 'content-type'):
    #         pass
    #     else:
    #         print(key + '-------------- ' + value)
    # print (content)
    # soup = BeautifulSoup(content, "html.parser")
    # aList = soup.find_all('p')
    # for a in aList:
    #     print (a)

def googe_search(url:str):
    request = Request(url)
    request.add_header('User-Agent', USER_AGENT)
    cookie_jar.add_cookie_header(request)
    # GET
    with urlopen(request) as response:
        # cookieの保管
        cookie_jar.extract_cookies(response, request)
        html = response.read()
        # cookieをファイル保管
        cookie_jar.save()
        return html
    return ''

def robot_req():
    robots = Robots.fetch(SAMPLE_URL + 'robots.txt')
    agent = robots.agent('hogehoge-agent')
    print (agent.allowed(SAMPLE_URL + 'w/load.php?'))
    print (agent.delay)

    # rp = urllib.robotparser.RobotFileParser()
    # rp.set_url('http://www.cyclowired.jp/robots.txt' )
    # rp.read()
    # print (rp.can_fetch('hogehoge-agent', 'http://www.cyclowired.jp/news'))
    # print (rp.crawl_delay('hogehoge-agent'))

http_req()
# robot_req()
