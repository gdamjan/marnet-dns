# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import couchdb

class MarnetPipeline(object):
    """Store in CouchDB, check if it's new or changed item"""
    def __init__(self):
        self.db = couchdb.Database("http://localhost:5984/dns")

    def process_item(self, domain, item):
        self.db[item['domain']] = dict(item)
        return item
