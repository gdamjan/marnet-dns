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

    def process_item(self, item, spider):
        """item is an instance of MarnetItem,
        spider of MarnetSpider

        check if the domain exists in the database, and if so compare for
        differences. If no difference exists do nothing.
        """
        db = self.db
        data = dict(item)
        doc_id = data.pop('domain')
        if doc_id in db:
            old_data = db.get(doc_id)
            data['_rev'] = old_data['_rev']
            if compare(old_data, data):
                return item
            # make a diff, and notify it?
        db[doc_id] = data
        return item


def compare(old_item, new_item):
    old_item.pop('_id')
    old_item.pop('last_updated')
    new_item.pop('last_updated')
    return old_item == new_item
