import scrapy


class Soseki3Spider(scrapy.Spider):
    name = 'soseki3'
    allowed_domains = ['www.aozora.gr.jp']
    # 夏目漱石の作品一覧ページ
    start_urls = ['http://www.aozora.gr.jp/index_pages/person148.html']

    # 作品一覧ページの解析
    def parse(self, response):
        li_list = response.css('ol > li a')
        for a in li_list:
            href = a.css('::attr(href)').extract_first()
            href2 = response.urljoin(href)
            # 図書カードのページの取得を指示
            yield response.follow(
                href2, self.parse_card
            )

    # 図書カードのページの解析
    def parse_card(self, response):
        # タイトルの取得
        title = response.css('title::text').extract_first()
        # ダウンロード先ZIPファイルの取得
        alist = response.css('table.download tr td a')
        for a in alist:
            href = a.css('::attr(href)').extract_first()
            href2 = response.urljoin(href)
            # ZIPファイル以外は別のファイル形式なので除外
            if href2[-4:] != ".zip": continue
            # 結果を出力
            yield {
                'title': title,
                'url': href2
            }
