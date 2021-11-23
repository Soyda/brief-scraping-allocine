import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MoviespiderSpider(CrawlSpider):
    name = 'movieSpider'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    rules = (
        Rule(LinkExtractor(restrict_xpaths = '//td[@class="titleColumn"]'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(restrict_xpaths= '(//a[@class="button-right"])[2]'))
    )

    # rules = (
    #     Rule(LinkExtractor(allow=r'meilleurs/'), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):

        item = {}

        item['title'] = response.xpath('//h1/text()').get()
        item['original_title'] = response.xpath('//div[@data-testid="hero-title-block__original-title"]/text()').get()
        item['score'] = response.xpath('//div[@data-testid="hero-rating-bar__aggregate-rating__score"]/span/text()').get()
        item['type'] = response.xpath('//a[@class="GenresAndPlot__GenreChip-cum89p-3 fzmeux ipc-chip ipc-chip--on-baseAlt"]/span/text()').getall()
        item['release_date'] = response.xpath('//span[@class="TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex"]/text()')[0].get()
        item['duration'] = "".join(response.xpath('//li[@data-testid="title-techspec_runtime"]/div[@class="ipc-metadata-list-item__content-container"]/text()').getall())
        # item['resume'] = response.xpath('//div[@data-testid="hero-title-block__original-title"]/text()').get()
        item['top_cast'] = response.xpath('//a[@data-testid="title-cast-item__actor"]/text()').getall()
        item['audience'] = response.xpath('//span[@class="TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex"]/text()')[1].get()
        # item['country'] = response.xpath('//div[@data-testid="hero-title-block__original-title"]/text()').get()
        # item['original_language'] = response.xpath('//div[@data-testid="hero-title-block__original-title"]/text()').get()

        return item

    # response.xpath('//td[@class="titleColumn"]/a/text()').getall() get titles of movies on top250 page
