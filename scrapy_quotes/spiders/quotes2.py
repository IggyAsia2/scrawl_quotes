# scrapy_quotes/scrapy_quotes/spiders/quotes.py
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['trangvangvietnam.com']
    start_urls = ['https://trangvangvietnam.com/categories/129310/xuat-nhap-khau-cac-cong-ty-xuat-nhap-khau.html']

    def parse(self, response):
        for quote in response.css("div.w-100 h-auto shadow rounded-3 bg-white p-2 mb-3"):
            yield {
                'company': quote.css("div.listings_center h2 a::text").extract_first(),
                # 'author': quote.css("small.author::text").extract_first(),
                # 'tags': ','.join(quote.css("div.tags > a.tag::text").extract())
            }

        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
