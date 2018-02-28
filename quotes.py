# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['litquotes.com']
    start_urls = ['http://litquotes.com/Random-Quote.php']

    def parse(self, response):
        self.log('Visito : '+response.url)
        yield {
            'autore': response.css('div.purple > p:nth-child(1) > a::text').extract_first(),
            'opera': response.css('div.purple > p:nth-child(1) > i > a::text').extract_first(),
            'citazione': response.css('div.purple > p:nth-child(1) > b::text').extract_first()
        }

