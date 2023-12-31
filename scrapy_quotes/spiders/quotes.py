# scrapy_quotes/scrapy_quotes/spiders/quotes.py
import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["trangvangvietnam.com"]
    start_urls = ["https://trangvangvietnam.com/srch/xuat_nhap_khau.html"]

    def parse(self, response):
        for quote in response.css("div.bg-white"):
            company = quote.css("div.listings_center a::text").extract_first()
            if not company:
                company = quote.css(
                    "div.listings_center_khongxacthuc a::text"
                ).extract_first()
            email = quote.css("div.email_web_section a::attr(href)").extract_first()
            if email:
                email = email.split(":")[1]
            address = quote.css("div.logo_congty_diachi small::text").extract_first()
            phone = quote.css("div.listing_dienthoai a::text").extract_first()
            if not phone:
                phone = quote.css(
                    "div.listing_diachi_nologo div.pb-0 a::text"
                ).extract_first()
            if phone:
                phone = re.sub("[^0-9]", "", phone)
            website = quote.css(
                "div.email_web_section a:nth-child(2)::attr(href)"
            ).extract_first()

            if company:
                yield {
                    "TÊN KHÁCH HÀNG": company,
                    "ĐIỆN THOẠI": phone,
                    # 'EMAIL': email.split(":")[1],
                    "EMAIL": email,
                    "NHÓM KHÁCH HÀNG": "Khách Đoàn Logistics",
                    "ĐỊA CHỈ": address,
                    "WEBSITE": website,
                }

        next_page_url = response.xpath('//div[@id="paging"]/a/@href')[-1].extract()
        if next_page_url != '?page=27':
            yield scrapy.Request(response.urljoin(next_page_url))
