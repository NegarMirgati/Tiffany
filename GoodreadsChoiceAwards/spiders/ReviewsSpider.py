import scrapy
from urllib.parse import urlparse
import os.path
from GoodreadsChoiceAwards.items import winnerItem

class WinnersSpider(scrapy.Spider):
    name = "winners"
    start_urls = [
        'https://www.goodreads.com/choiceawards/best-books-2009',
        'https://www.goodreads.com/choiceawards/best-books-2010',
        'https://www.goodreads.com/choiceawards/best-books-2011',
        'https://www.goodreads.com/choiceawards/best-books-2012',
        'https://www.goodreads.com/choiceawards/best-books-2013',
        'https://www.goodreads.com/choiceawards/best-books-2014',
        'https://www.goodreads.com/choiceawards/best-books-2015',
        'https://www.goodreads.com/choiceawards/best-books-2016',
        'https://www.goodreads.com/choiceawards/best-books-2017',
        'https://www.goodreads.com/choiceawards/best-books-2018'
    ]

    def parse(self, response):
        print ("URL: " + response.request.url)
        u = urlparse(response.request.url).path
        award = os.path.split(u)[1]
        book = winnerItem()
        
        print(response.xpath('//*[@class="wtrRight wtrUp"]//*[@id="book_id"]/@value').extract())
  
        for div in response.xpath('.//*[@id="categories"]/div[@class="categoryContainer"]/div[@class="category clearFix"]'):
            book['id'] = div.xpath('.//*[@class="wtrRight wtrUp"]//*[@id="book_id"]/@value').extract_first()
            book['name'] = div.xpath('.//a/div/img/@alt').extract_first()
            book['category'] = div.xpath('.//a/h4/text()').extract_first().rstrip().replace('\n', '')
            book['award'] =  award
            yield book