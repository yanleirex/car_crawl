# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

import MySQLdb
from twisted.enterprise import adbapi


class CarPipeline(object):
    def __init__(self):
        self.file = codecs.open('car.json', 'wb', 'utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item))+'\n'
        self.file.write(line.decode("unicode_escape"))
        return item

    def close_spider(self, spider):
        self.file.close()


# class MySQLPipeline(object):
#     def __init__(self, dbpool):
#         self.dbpool = adbapi.ConnectionPool('MySQLdb',
#                                             db='cars',
#                                             user='root',
#                                             password='0622',
#                                             cursorclass=MySQLdb.cursors.DictCursor,
#                                             charset = 'utf8',
#                                             use_unicode=False
#                                             )
#
#     def process_item(self, item, spider):
#         query = self.dbpool.runInteraction(self._conditional_insert,item)
#         query.addErrback(self.handler_error)
#         return item
#
#     def _conditional_insert(self,tx,item):
#             tx.execute("""insert into car (car_desc, car_url, register_time, mileage,gear_box,city,price,msg_price ) \
#                  values (%s, %s, %s, %s,%s, %s, %s, %s)""",
#                 (item['car_desc'],item['car_url'], item['register_time'],
#                 item['mileage'],item['gear_box'],item['city'],
#                  item['price'],item['msg_price'])
#             )
#
#     def handler_error(self,e):
#         self.log.err(e)