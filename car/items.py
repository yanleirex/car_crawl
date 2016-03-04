# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CarItem(Item):
    # define the fields for your item here like:
    # name = Field()
    car_url = Field()
    car_desc = Field()
    register_time = Field()
    mileage = Field()
    gear_box = Field()
    city = Field()
    price = Field()
    msg_price = Field()

