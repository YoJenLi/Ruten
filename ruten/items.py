# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RutenItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    nnumber = scrapy.Field()
    snumber = scrapy.Field()
    seller_name = scrapy.Field()
    seller_logint = scrapy.Field()
    seller_score = scrapy.Field()
    qa_count = scrapy.Field()
    price_count = scrapy.Field()
    content = scrapy.Field()