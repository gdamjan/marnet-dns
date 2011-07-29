# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from couchdbkit import Database
from scrapy.conf import settings

import time

class MarnetPipeline(object):
    """Store in CouchDB, check if it's new or changed item"""
    def __init__(self):
        self.db = Database(settings['COUCHDB_URL'])

    def process_item(self, item, spider):
        """item is an instance of MarnetItem,
        spider of MarnetSpider

        check if the domain exists in the database, and if so compare for
        differences. If no difference exists do nothing.
        """
        _rev = None
        seq = None
        db = self.db
        new_data = dict(item)
        doc_id = new_data['domain']
        # check if we already have it in the database
        if doc_id in db:
            old_doc = db.get(doc_id)
            _rev = old_doc['_rev']
            seq = old_doc.get('seq', 1)
            old_data = old_doc['data']
            if old_data == new_data:
                # no changes, just skip over
                return item
            # TODO: there are changes!
            #       perhaps make a diff, and notify about it?
        new_doc = dict(
                _id = doc_id,
                data = new_data,
                last_updated = time.time()
            )
        if _rev:
            new_doc['_rev'] = _rev
        if seq:
            new_doc['seq'] = seq + 1
        db.save_doc(new_doc)
        return item
