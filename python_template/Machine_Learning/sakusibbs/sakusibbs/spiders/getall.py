import scrapy, pprint
# SeleniumのMiddleWareを使うために取り込む
from ..selenium_middleware import *

# ユーザー名とパスワードの指定
USER = "JS-TESTER"
PASS = "ipCU12ySxI"

class GetallSpider(scrapy.Spider):
    name = 'getall'
    # ミドルウェアを登録する
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "sakusibbs.selenium_middleware.SeleniumMiddleware": 0
        }
    }

    # リクエスト実行前にログインする
    def start_requests(self):
        # ログインページを開く
        url = 'https://uta.pw/sakusibbs/users.php?action=login'
        selenium_get(url)
        # ユーザー・パスワードを入力
        user = get_dom('#user')
        user.send_keys(USER)
        pw = get_dom('#pass')
        pw.send_keys(PASS)
        # ログインボタンをクリック
        btn = get_dom('#loginForm input[type=submit]')
        btn.click()
        # ユーザーページを得る
        a = get_dom('.islogin a')
        mypage = a.get_attribute('href')
        print("mypage=", mypage)
        yield scrapy.Request(mypage, self.parse)

    #allowed_domains = ['uta.pw']
    #start_urls = ['http://uta.pw/']

    def parse(self, response):
        # 詩の一覧を得る
        alist = response.css('ul#mmlist > li a')
        for a in alist:
            url = a.css('::attr(href)').extract_first()
            url2 = response.urljoin(url)
            yield response.follow(
                url2, self.parse_sakuhin)

    def parse_sakuhin(self, response):
        # 作品名を取り出す
        title = response.css('title::text').extract_first()
        print("---", title)
        # 詩の書かれているフレームを取り出す
        src = response.css(
            '#postform > center > div > iframe::attr(src)').extract_first()
        #    'iframe::attr(src)').extract_first()
        src2 = response.urljoin(src)
        # リクエストを作成
        req = scrapy.Request(src2, self.parse_download)
        req.meta["title"] = title
        yield req

    def parse_download(self, response):
        # 作品のHTMLをダウンロード
        title = response.meta["title"]
        fname = title + ".html"
        with open(fname, "wb") as f:
            f.write(response.body)

    def closed(self, reason):
        selenium_close()
