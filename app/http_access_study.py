# -*- coding: utf-8 -*-
import httplib2
import urllib.robotparser
import reppy.robots
import bs4

SAMPLE_URL = 'https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%A1%E3%83%AA%E3%82%AB%E8%88%AA%E7%A9%BA%E5%AE%87%E5%AE%99%E5%B1%80'
# SAMPLE_URL = 'http://www.cyclowired.jp/robots.txt'

def http_req():
    h = httplib2.Http()
    headers = {'cache-control':'no-cache'}
    (response, content) = h.request(SAMPLE_URL, headers=headers)

    # items = dict(response.items())
    for key,value in response.items():

        if (key != 'content-type'):
            pass
        else:
            print(key + '-------------- ' + value)

    soup = bs4.BeautifulSoup(content, "html.parser")
    aList = soup.find_all('a')
    for a in aList:
        print (a)

def robot_req():
    robots = reppy.robots.Robots.fetch(SAMPLE_URL + 'robots.txt')
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
