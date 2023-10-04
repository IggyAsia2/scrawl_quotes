# scrapy_quotes/scrapy_quotes/spiders/quotes.py
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['trangvangvietnam.com']
    start_urls = ['https://trangvangvietnam.com/srch/xuat_nhap_khau.html']

    def parse(self, response):
        for quote in response.css("div.bg-white"):
            company =  quote.css("div.listings_center a::text").extract_first()
            email = quote.css("div.email_web_section a::attr(href)").extract_first()
            address = quote.css("div.logo_congty_diachi small::text").extract_first()
            phone = quote.css("div.listing_dienthoai a::text").extract_first()
            sponsor = quote.css("span.star_text::text").extract_first()
            major = quote.css("span.nganh_listing_txt::text").extract_first()
            website = quote.css("div.email_web_section a:nth-child(2)::attr(href)").extract_first()
            
            if company:
                yield {
                    'company': company,
                    'email': email.split(":")[1],
                    'address': address,
                    'phone': phone,
                    'sponsor': sponsor,
                    'major': major,
                    'website': website
                }

        next_page_url = response.xpath('//div[@id="paging"]/a/@href')[-1].extract()
        last_page_url = response.xpath('//div[@id="paging"]/a/@href')[-2].extract()
        if next_page_url != '?page=27':
            yield scrapy.Request(response.urljoin(next_page_url))