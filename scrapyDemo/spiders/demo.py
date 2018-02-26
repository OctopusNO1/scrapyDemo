# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['python123.io']
    # start_urls = ['https://python123.io/ws/demo.html']
    
    def start_requests(self):
        urls = ['https://python123.io/ws/demo.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.' % fname)   
