import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MoviespiderSpider(CrawlSpider):
    name = 'movieSpider'
    allowed_domains = ['www.allocine.fr']
    start_urls = ['https://www.allocine.fr/film/meilleurs/']

    rules = (
        Rule(LinkExtractor(allow=r'meilleurs/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        movie_title = response.css('a.meta-title-link::text')

        # [title.get() for title in movie_title]

        for title in movie_title:
            yield {
                'movie_title' : title.get()
            }

        #     # next_page = response.css('li.next a::attr(href)').get()
        #     # if next_page is not None:
        #     #     next_page = response.urljoin(next_page)
        #     #     yield scrapy.Request(next_page, callback=self.parse)

