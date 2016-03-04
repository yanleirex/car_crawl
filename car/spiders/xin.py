from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from car.items import CarItem

class XinSpider(CrawlSpider):
    name = 'xin'
    allowed_domains = ['xin.com']
    base_url = 'http://www.xin.com'
    start_urls = ['http://www.xin.com/quanguo/s']
    fix = 'a10o2i'
    post_fix = 'v1'

    def parse(self, response):
        self.log('response from %s just arrived!' % response.url)
        sel = Selector(response)
        urls = sel.xpath('//p[@class="cityMore"]//a/@href').extract()
        for url in urls:
            for page in range(1,51):
                fetch_url = self.base_url + url + self.fix + str(page) + self.post_fix
                yield Request(fetch_url, callback=self.parse_detail)

    def parse_detail(self, response):
        self.log('A response from %s just arrived!' % response.url)
        cars = Selector(response).xpath('//div[@class="car-vtc vtc-border "]')
        for car in cars:
            car_item = CarItem()
            car_info = car.xpath('div[@class="vtc-info"]')
            car_info_box = car_info.xpath('div[@class="box"]/ul/li/text()').extract()
            car_item['car_desc'] = car_info.xpath('p/a/text()').extract()
            car_item['car_url'] = car_info.xpath('p/a/@href').extract()
            car_item['register_time'] = car_info_box[0]
            car_item['mileage'] = car_info_box[1]
            car_item['gear_box'] = car_info_box[2]
            car_item['city'] = car_info_box[3]
            car_item['price'] = car.xpath('div[@class="vtc-money"]/em/text()').extract()
            car_item['msg_price'] = car.xpath('div[@class="vtc-money"]/div[@class="msg-price"]/p/del/text()').extract()
            yield car_item

        # next page
        # next_page_url = response.url + self.fix + str(self.page) + 'v1'
        # self.page += 1
        # if self.page < 51:
        #     yield Request(next_page_url, callback=self.parse_detail)

