import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MoviespiderSpider(CrawlSpider):
    name = 'movieSpider'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    rules = (
        Rule(LinkExtractor(restrict_xpaths = '//td[@class="titleColumn"]'), callback='parse_movie', follow=True),
        # Rule(LinkExtractor(restrict_xpaths= '(//a[@class="button-right"])[2]'))
    )

    # rules = (
    #     Rule(LinkExtractor(allow=r'meilleurs/'), callback='parse_movie', follow=True),
    # )

    def parse_movie(self, response):

        movie = {}

        movie['title'] = response.xpath('//h1/text()').get()

        original_title = response.xpath('//div[@data-testid="hero-title-block__original-title"]/text()')
        if original_title != [] :
            movie['original_title'] = original_title.get().replace('Original title: ', '')
        
        movie['score'] = response.xpath('//div[@data-testid="hero-rating-bar__aggregate-rating__score"]/span/text()').get()
        movie['type'] = response.xpath('//a[@class="GenresAndPlot__GenreChip-cum89p-3 fzmeux ipc-chip ipc-chip--on-baseAlt"]/span/text()').getall()
        movie['release_date'] = response.xpath('//span[@class="TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex"]/text()')[0].get()
        movie['duration'] = "".join(response.xpath('//li[@data-testid="title-techspec_runtime"]/div[@class="ipc-metadata-list-item__content-container"]/text()').getall())
        movie['resume'] = response.xpath('//div[@class="ipc-html-content ipc-html-content--base"]/div/text()').get()
        movie['top_cast'] = response.xpath('//a[@data-testid="title-cast-item__actor"]/text()').getall()
        movie['audience'] = response.xpath('//span[@class="TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex"]/text()')[1].get()
        movie['country'] = response.xpath('//a[contains(@href, "?country_of_origin")]/text()').getall()
        movie['original_language'] = response.xpath('//a[contains(@href, "primary_language")]/text()').getall()

        return movie
