# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class MarnetItem(Item):
    domain = Field()
    dosie = Field()
    ime = Field()
    administrative = Field()
    techical = Field()
    dns = Field()
    last_updated = Field()
