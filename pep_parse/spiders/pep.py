import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        numerical_index = response.css('section[id="numerical-index"]')
        pep_links = numerical_index.css('tr').css('a::attr(href)').getall()
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': response.css('ul.breadcrumbs').css(
                'li+li+li::text').get().replace('PEP ', ''),
            'name': re.sub(
                '.*– ', '', response.css('h1.page-title::text').get()),
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)
