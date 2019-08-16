# -*- coding: utf-8 -*-
import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        for quote in response.css('div.quote'):
            try:
                yield {
                    'text': quote.css('span.text::text').get(),
                    'author': quote.xpath('//span/small/text()').get(),
                    'tags': quote.css('div.tags a.tag::text').getall(),
                }
            except:
                continue

        next_page = response.css('li.next a::attr("href")').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
