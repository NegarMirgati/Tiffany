import scrapy
from urllib.parse import urlparse
import os.path
from GoodreadsChoiceAwards.items import nomineeItem
from urllib.parse import urljoin
from urllib.parse import urlparse

class WinnersSpider(scrapy.Spider):
    name = "winners"
    start_urls = [
    'https://www.goodreads.com/choiceawards/best-books-2019'
    ]

    def parse(self, response):
        u = urlparse(response.request.url).path
        print ("URL: " + response.request.url)
        u = urlparse(response.request.url).path
        award = os.path.split(u)[1]
      
        for div in response.xpath('.//*[@id="categories"]/div[@class="categoryContainer"]/div[@class="category clearFix"]'):
            id = div.xpath('.//*[@class="wtrRight wtrUp"]//*[@id="book_id"]/@value').extract_first()
            name = div.xpath('.//a/div/img/@alt').extract_first()
            category = div.xpath('.//a/h4/text()').extract_first().rstrip().replace('\n', '')
            url = urljoin(response.url, div.xpath('.//a/@href').extract_first())
            request = scrapy.Request(url, callback = self.parse_category, meta = {'category' : category, 'award' : award, 'id' : id, 'name' : name})
            yield request

    def parse_category(self, response):
        print('Parse function called on %s', response.url)
        title = response.xpath('.//title/text()').extract_first()
        book = nomineeItem()
        url = response.xpath('.//*[@class="winningBook"]/*[@class="miniBook"]/*[@class="miniBookContent"]/*[@class="u-marginTopXSmall"]/a[1]/@href').extract_first()
        book['url'] = url
        book['id'] = response.meta['id']
        book['category'] = response.meta['category']
        book['award'] = response.meta['award']
        yield book
