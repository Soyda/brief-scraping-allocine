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

        original_title = response.xpath('//div[@data-testid="hero-title-block__original-title"]/text()')
        if original_title != [] :
            serie['original_title'] = original_title.get().replace('Original title: ', '')

        serie['score'] = response.xpath('//div[@data-testid="hero-rating-bar__aggregate-rating__score"]/span/text()').get()
        serie['type'] = response.xpath('//a[@class="GenresAndPlot__GenreChip-cum89p-3 fzmeux ipc-chip ipc-chip--on-baseAlt"]/span/text()').getall()

        number_of_seasons = response.xpath('//select[@id="browse-episodes-season"]/option/text()')
        # single_season = response.xpath('//a[@class="ipc-button ipc-button--single-padding ipc-button--center-align-content ipc-button--default-height ipc-button--core-base ipc-button--theme-base ipc-button--on-accent2 ipc-text-button"]/div/text()').get()[0]
        if number_of_seasons == [] :
            serie['number_of_seasons'] = 1 # single_season
        else :
            serie['number_of_seasons'] = number_of_seasons.get()

        serie['number_of_episodes'] = response.xpath('//span[@class="ipc-title__subtext"]/text()')[0].get()
        serie['release_date'] = response.xpath('//span[@class="TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex"]/text()')[0].get()
        serie['duration'] = "".join(response.xpath('//li[@data-testid="title-techspec_runtime"]/div[@class="ipc-metadata-list-item__content-container"]/text()').getall())
        serie['resume'] = response.xpath('//div[@class="ipc-html-content ipc-html-content--base"]/div/text()').get()
        serie['top_cast'] = response.xpath('//a[@data-testid="title-cast-item__actor"]/text()').getall()
        serie['audience'] = response.xpath('//span[@class="TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex"]/text()')[1].get()
        serie['country'] = response.xpath('//a[contains(@href, "?country_of_origin")]/text()').getall()
        serie['original_language'] = response.xpath('//a[contains(@href, "primary_language")]/text()').getall()

        return serie
