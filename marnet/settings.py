# Scrapy settings for domeinot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
# 
#     scrapy/conf/default_settings.py
#

BOT_NAME = 'marnet'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['marnet.spiders']
NEWSPIDER_MODULE = 'marnet.spiders'
DEFAULT_ITEM_CLASS = 'marnet.items.MarnetItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)


HTTPCACHE_DIR = "cache"
HTTPCACHE_EXPIRATION_SECS = 3200
DOWNLOAD_DELAY = 0.25    # 250 ms of delay

ITEM_PIPELINES = [
    'marnet.pipelines.MarnetPipeline',
]

LOG_LEVEL = "INFO"
