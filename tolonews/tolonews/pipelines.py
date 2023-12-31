# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TolonewsPipeline:
    def process_item(self, item, spider):
        return item


import mysql.connector

class SaveToMySQLPipeLine():

    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Muchom@2019',
            database = 'news'
        )

        self.cur = self.conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS news(id int NOT NULL PRIMARY KEY AUTO_INCREMENT, title TEXT, image TEXT, url TEXT, text TEXT)")


    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO news VALUES(NULL, %s, %s, %s, %s)" , (item['title'], item['image'], item['url'], item['text']))
        
        self.conn.commit()
        return item


    def close_spider(self, spider):

        self.cur.close()
        self.conn.close()


