Domeinot 2.0
============

Crawls and scrapes the web-site of Marnet_. The MarNET Network Information
Center (MARNET-MIC) is the registrar for the .mk domain.

.. _Marnet: http://dns.marnet.net.mk/registar.php


Dependencies:
~~~~~~~~~~~~~

Scrapy_ and Twisted_ and CouchDB_/CouchDB-Python_

.. _Scrapy: http://scrapy.org/
.. _Twisted: http://twistedmatrix.com/
.. _CouchDB: http://couchdb.org/
.. _CouchDB-Python: http://code.google.com/p/couchdb-python/


Description
~~~~~~~~~~~

The spider is defined in `marnet/spiders/registar.py`. This file describes what
the spider crawls over (which links it follows) and what pages it scrapes for
(see: `MarnetSpider.rules`).

Xpath rules are used to scrape the needed info. The info is packed in
`marnet.items.MarnetItem` objects and sent to the
`marnet.pipelines.MarnetPipeline` pipeline that stores it to a CouchDB
database.


The spiders begins at the page http://dns.marnet.net.mk/registar.php, and then
follows each http://dns.marnet.net.mk/registar.php?bukva=<smth> url, and
scrapes any http://dns.marnet.net.mk/registar.php?dom=domain.name.mk pages it
finds.
