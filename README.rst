Domeinot 2.0
============

Crawls and scrapes the web-site of Marnet_. The MarNET Network Information
Center (MARNET-MIC) is the registrar for the .mk domain.

.. _Marnet: http://dns.marnet.net.mk/registar.php


Dependencies:
~~~~~~~~~~~~~

Scrapy_ and Twisted_ and CouchDB_/CouchDBKit_

.. _Scrapy: http://scrapy.org/
.. _Twisted: http://twistedmatrix.com/
.. _CouchDB: http://couchdb.org/
.. _CouchDBKit: http://couchdbkit.org/


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

Installation
~~~~~~~~~~~~

::
    git clone git://github.com/gdamjan/marnet-dns.git
    cd marnet-dns
    export PYTHONUSERBASE=$PWD/env
    pip install --user -r requires.txt


Operation
~~~~~~~~~

Run ``scrapy crawl marnet``

The first time I started it, it worked for 30 minutes, and createad
a 261MB ./cache/ folder - which suggests that's the amount of
Internet traffic it generated. Since the marnet site doesn't use E-Tags or
Timestamps, each run of the crawler will download everything again.

The couchdb database has 16789 documents and is 41MB (a very recent
CouchDB version).
