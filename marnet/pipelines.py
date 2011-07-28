# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from couchdbkit import Database
from scrapy.conf import settings


class MarnetPipeline(object):
    """Store in CouchDB, check if it's new or changed item"""
    def __init__(self):
        self.db = Database(settings.get('COUCHDB_URL'))

    def process_item(self, domain, item):
        data = dict(item)
        id = data.pop('domain')
        old_data = self.db.get(id, None)
        compare(old_data, data)
        self.db[id] = data
        return item

def compare(old_item, new_item):
    old_item.pop('last_updated')
    old_item.pop('_id')
    old_item.pop('_rev')
    new_item.pop('last_updated')
