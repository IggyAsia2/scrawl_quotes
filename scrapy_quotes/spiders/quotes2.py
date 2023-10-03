import scrapy


class Quotes2Spider(scrapy.Spider):
    name = "quotes2"
    allowed_domains = ["trangvangvietnam.com"]
    start_urls = ["http://trangvangvietnam.com/"]

    def parse(self, response):
        pass
