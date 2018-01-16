# -*- coding: utf-8 -*-
from urllib.robotparser import RobotFileParser
<<<<<<< HEAD
from bs4 import BeautifulSoup
from http.cookiejar import LWPCookieJar
=======
from html.parser import unescape
from http.cookiejar import LWPCookieJar
from bs4 import BeautifulSoup
>>>>>>> ec461270892d9ea04d673fe0d71151ed91fc2ea6
import ggrks

SAMPLE_URL = 'http://www.google.co.jp/search?q=integer'

def http_req():

<<<<<<< HEAD
    gs = ggrks.Ggrks('サターン V')
    html = gs.search()

    # with open('get.html', 'wb') as file:
    #     file.write(html)
=======
    gs = ggrks.Ggrks()
    html = gs.search(SAMPLE_URL)
>>>>>>> ec461270892d9ea04d673fe0d71151ed91fc2ea6

    soup = BeautifulSoup(html, 'lxml')
    aList = soup.find_all("a")

    with open('hoge.html', 'wb') as file:
        for a in aList:
            file.write(a.encode())

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
