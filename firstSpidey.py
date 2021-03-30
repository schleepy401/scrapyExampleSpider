# -*- coding: utf-8 -*-
import scrapy


class FirstspideySpider(scrapy.Spider):
    name = 'firstSpidey'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass
