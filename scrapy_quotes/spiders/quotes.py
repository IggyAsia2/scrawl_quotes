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
            major = quote.css("span.nganh_listing_txt::text").extract_first()
            address = quote.css("div.logo_congty_diachi small::text").extract_first()
            phone = response.css("div.listing_dienthoai a::text").extract_first()
            email = response.css("div.email_web_section a::attr(href)").extract_first()
            website = response.css("div.email_web_section a::attr(href)")[-1].extract()
            
            if company:
                yield {
                    'company': company,
                    'email': email.split(":")[1],
                    'address': address,
                    'phone': phone,
                    'sponsor': sponsor or "",
                    'major': major,
                    'website': website
                }

        next_page_url = response.xpath('//div[@id="paging"]/a/@href')[-1].extract()
        last_page_url = response.xpath('//div[@id="paging"]/a/@href')[-1].extract()
        if next_page_url != '?page=2':
            yield scrapy.Request(response.urljoin(next_page_url))