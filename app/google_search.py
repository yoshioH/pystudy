from urllib.request import Request
from http.cookiejar import LWPCookieJar
import os
class GoogleSearch:

    home_folder
    now_page = 0
    USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0)'

    def __init__(self):
        self.home_folder = os.getenv('HOME')
        if not self.home_folder:
            self.home_folder = os.getenv('USERHOME')
            if not home_folder:
                self.home_folder = '.'   # Use the current folder on error.
        cookie_jar = LWPCookieJar(os.path.join(home_folder, '.google-cookie'))
        try:
            cookie_jar.load()
        except Exception:
            pass

    def search(url:str):
        request = Request(url)
        request.add_header('User-Agent', USER_AGENT)
        # cookie_jar.add_cookie_header(request)

        # GET
        with urlopen(request) as response:
            # cookieの保管
            cookie_jar.extract_cookies(response, request)
            html = response.read()
            # cookieをファイル保管
            cookie_jar.save()
            return html
        return ''

    def next():
        return ''
