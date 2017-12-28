# -*- coding: utf-8 -*-
from urllib.request import Request,urlopen
from http.cookiejar import LWPCookieJar
import os
import urllib

# TODO 情強お兄ちゃんファクトリを作ってそこからインスタンスを返したい。
class Ggrks:
    BASE_SEARCH_PATH = 'http://www.google.co.jp/search'
    USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0)'

    def __init__(self, word:str):
        self.word = word
        self.resource_path = Ggrks.BASE_SEARCH_PATH + '?q=' + urllib.parse.quote(word)
        print (self.resource_path)
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

    def search(self) -> str:
        """
        simple search from google
        """
        request = Request(self.resource_path)
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
