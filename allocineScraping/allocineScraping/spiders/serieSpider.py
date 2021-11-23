import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SeriespiderSpider(CrawlSpider):
    name = 'serieSpider'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths = '//td[@class="titleColumn"]'), callback='parse_serie', follow=True),
        # Rule(LinkExtractor(restrict_xpaths= '(//a[@class="button-right"])[2]'))
    )

    def parse_serie(self, response):

        serie = {}

        serie['title'] = response.xpath('//h1/text()').get()
        serie['original_title'] = response.xpath('//div[@data-testid="hero-title-block__original-title"]/text()').get().replace('Original title: ', '')
        serie['score'] = response.xpath('//div[@data-testid="hero-rating-bar__aggregate-rating__score"]/span/text()').get()
        serie['type'] = response.xpath('//a[@class="GenresAndPlot__GenreChip-cum89p-3 fzmeux ipc-chip ipc-chip--on-baseAlt"]/span/text()').getall()
        serie['release_date'] = response.xpath('//span[@class="TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex"]/text()')[0].get()
        serie['duration'] = "".join(response.xpath('//li[@data-testid="title-techspec_runtime"]/div[@class="ipc-metadata-list-item__content-container"]/text()').getall())
        serie['resume'] = response.xpath('//div[@class="ipc-html-content ipc-html-content--base"]/div/text()').get()
        serie['top_cast'] = response.xpath('//a[@data-testid="title-cast-item__actor"]/text()').getall()
        serie['audience'] = response.xpath('//span[@class="TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex"]/text()')[1].get()
        serie['country'] = response.xpath('//a[contains(@href, "?country_of_origin")]/text()').getall()
        serie['original_language'] = response.xpath('//a[contains(@href, "primary_language")]/text()').getall()

        return serie
