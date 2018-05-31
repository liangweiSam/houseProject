# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    address = scrapy.Field()
    average_price = scrapy.Field()
    avg_price_start = scrapy.Field()
    avg_price_start_unit = scrapy.Field()
    bizcircle_name = scrapy.Field()
    city_id = scrapy.Field()
    city_name = scrapy.Field()
    tags = scrapy.Field()
    total_price_start = scrapy.Field()
    total_price_start_unit = scrapy.Field()
    title = scrapy.Field()
    min_frame_area = scrapy.Field()
    max_frame_area = scrapy.Field()
    district_name = scrapy.Field()
