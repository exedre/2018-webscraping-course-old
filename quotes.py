# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['litquotes.com']
    start_urls = ['http://litquotes.com/Random-Quote.php']

    def parse(self, response):
        self.log('Visito : '+response.url)
