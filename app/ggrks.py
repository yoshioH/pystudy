# -*- coding: utf-8 -*-
from urllib.request import Request,urlopen
from http.cookiejar import LWPCookieJar
from bs4 import BeautifulSoup
import os
# TODO 情強おにいちゃんファクトリからこのクラスを返したい
# TODO コンストラクタに検索ワードを渡し、ggrみたいな関数を呼び出す作りにする
class Ggrks:

    USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0)'

    def __init__(self):
        self.home_folder = os.getenv('HOME')
        if not self.home_folder:
            self.home_folder = os.getenv('USERHOME')
            if not home_folder:
                self.home_folder = '.'   # Use the current folder on error.
        self.cookie_jar = LWPCookieJar(os.path.join(self.home_folder, '.google-cookie'))
        try:
            self.cookie_jar.load()
        except Exception:
            pass

    def search(self, url:str) -> str:
        '''
        ググってリンクURLとを返す
        '''
        request = Request(url)
        request.add_header('User-Agent', Ggrks.USER_AGENT)
        # cookie_jar.add_cookie_header(request)

        # GET
        with urlopen(request) as response:
            # cookieの保管
            self.cookie_jar.extract_cookies(response, request)
            html = response.read()
            # cookieをファイル保管
            self.cookie_jar.save()
            return html
        return ''

    def next():
        return ''
