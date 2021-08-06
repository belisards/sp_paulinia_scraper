import scrapy
import datetime
# from gazette.spiders.base import BaseGazetteSpider

class BaseGazetteSpider(scrapy.Spider):
    name = 'Sp_Paulinia'
    TERRITORY_ID = "2905206"
    allowed_domains = ['www.paulinia.sp.gov.br/semanarios']
    start_urls = ['http://www.paulinia.sp.gov.br/semanarios/']

    def parse(self, response):
        print(response.url)
        # a_selectors = response.xpath("//a")


# response.xpath("//div[@class='container body-content']//div[@class='row']//a[contains(@href, 'AbreSemanario')]/@href")
# response.xpath("//div[@class='container body-content']//div[@class='row']//a[contains(@href, 'AbreSemanario')]/text()")
