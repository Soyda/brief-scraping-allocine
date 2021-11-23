import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MoviespiderSpider(CrawlSpider):
    name = 'movieSpider'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    rules = (
        Rule(LinkExtractor(restrict_xpaths = '//td[@class="titleColumn"]/a/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(restrict_xpaths= '(//a[@class="button-right"])[2]'))
    )

    # rules = (
    #     Rule(LinkExtractor(allow=r'meilleurs/'), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):

        item = {}

        item['movie_title'] = response.xpath('//h1[@class="TitleHeader__TitleText-sc-1wu6n3d-0 dxSWFG"]').get()

        return item

    # response.xpath('//td[@class="titleColumn"]/a/text()').getall() get titles of movies on top250 page
