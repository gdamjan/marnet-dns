from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst, Compose, MapCompose

from scrapy.selector import HtmlXPathSelector
from scrapy.utils.url import url_query_parameter

from marnet.items import MarnetItem

import time


class MarnetLoader(XPathItemLoader):
    default_input_processor = MapCompose(unicode)
    default_output_processor = TakeFirst()
    dns_out = Compose(lambda v: zip(v[::2], v[1::2]))


class MarnetSpider(CrawlSpider):
    domain_name = "dns.marnet.net.mk"
    start_urls = ["http://dns.marnet.net.mk/registar.php"]
    rules = [
        Rule(SgmlLinkExtractor(allow=[r'registar\.php\?dom=.+']), callback='parse_item'),
        Rule(SgmlLinkExtractor(allow=[r'registar\.php\?bukva=.+']), follow=True),
    ]

    def parse_item(self, response):
        dom = url_query_parameter(response.url, "dom")
        if dom:
            hxs = HtmlXPathSelector(response)
            base = hxs.select('/html/body/table/tr[2]/td/table[3]/tr/td/table')
            l = MarnetLoader(item=MarnetItem(), selector=base)
            l.add_value('domain', dom)
            l.add_xpath('dosie', './/tr/td/div/b/i/text()', re=':(\\d+)')
            l.add_xpath('ime', './/tr[4]/td[2]/text()')
            l.add_xpath('administrative', './/tr[9]/td[2]/text()')
            l.add_xpath('techical', './/tr[13]/td[2]/text()')
            l.add_xpath('dns', './/tr[@align="center"]/td/text()')
            l.add_value('last_updated', time.time())
            return l.load_item()


SPIDER = MarnetSpider()
