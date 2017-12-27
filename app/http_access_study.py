# -*- coding: utf-8 -*-
from httplib2 import Http
from urllib.robotparser import RobotFileParser
from html.parser import unescape
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from google import search
from http.cookiejar import LWPCookieJar
import google_search

SAMPLE_URL = 'http://www.google.co.jp/search?q=integer'

def http_req():

    gs = google_search.GoogleSearch()
    html = gs.search(SAMPLE_URL)

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
