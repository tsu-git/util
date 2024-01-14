import scrapy

class Soseki2Spider(scrapy.Spider):
    name = 'soseki2'
    start_urls = [
        'https://www.aozora.gr.jp/index_pages/person148.html'
    ] 

    def parse(self, response):
        # 作品一覧を抽出
        li_list = response.css('ol > li a')
        for a in li_list:
            # href属性とテキストを取り出す
            href = a.css('::attr(href)').extract_first()
            text = a.css('::text').extract_first()
            # フルパスに変換
            href2 = response.urljoin(href)
            # 結果を戻す
            yield {
                'text': text,
                'url': href2
            }
