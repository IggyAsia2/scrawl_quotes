# scrapy_quotes/scrapy_quotes/spiders/quotes.py
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['trangvangvietnam.com']
    start_urls = ['https://trangvangvietnam.com/srch/xuat_nhap_khau.html']

    def parse(self, response):
        for quote in response.css("div.bg-white"):
            company =  quote.css("div.listings_center a::text").extract_first()
            sponsor = quote.css("span.star_text::text").extract_first()
            # email = quote.css("div.listings_center a::text").extract_first()
            
            if company:
                yield {
                    'company': company,
                    'sponsor': sponsor or "",
                    # 'email': email,
                    # 'author': quote.css("small.author::text").extract_first(),
                    # 'tags': ','.join(quote.css("div.tags > a.tag::text").extract())
                }

        next_page_url = response.xpath('//div[@id="paging"]/a/@href')[-1].extract()
        last_page_url = response.xpath('//div[@id="paging"]/a/@href')[-1].extract()
        if next_page_url != '?page=3':
            yield scrapy.Request(response.urljoin(next_page_url))