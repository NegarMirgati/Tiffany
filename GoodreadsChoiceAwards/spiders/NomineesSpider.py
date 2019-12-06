# import scrapy
# from urllib.parse import urljoin
# from urllib.parse import urlparse
# import re
# import os.path
# from GoodreadsChoiceAwards.items import nomineeItem
#
#
# class NomineeSpider(scrapy.Spider):
# 	name = "nominees"
# 	start_urls = [
# 		'https://www.goodreads.com/choiceawards/best-books-2009',
# 		# 'https://www.goodreads.com/choiceawards/best-books-2010',
# 		# 'https://www.goodreads.com/choiceawards/best-books-2011',
# 		# 'https://www.goodreads.com/choiceawards/best-books-2012',
# 		# 'https://www.goodreads.com/choiceawards/best-books-2013',
# 		# 'https://www.goodreads.com/choiceawards/best-books-2014',
# 		# 'https://www.goodreads.com/choiceawards/best-books-2015',
# 		# 'https://www.goodreads.com/choiceawards/best-books-2016',
# 		# 'https://www.goodreads.com/choiceawards/best-books-2017'
# 		# 'https://www.goodreads.com/choiceawards/best-books-2018'
# 		'https://www.goodreads.com/choiceawards/best-books-2019'
# 	]
#
# 	def parse(self, response):
#
# 		u = urlparse(response.request.url).path
# 		award = os.path.split(u)[1]
# 		# //*[@id="categories"]/div/div[1]
# 		for div in response.xpath(
# 				'.//*[@id="categories"]/div[@class="categoryContainer"]/div[@class="category clearFix"]'):
# 			category = div.xpath('.//a/h4/text()').extract_first().rstrip().replace('\n', '')
# 			url = urljoin(response.url, div.xpath('.//a/@href').extract_first())
# 			request = scrapy.Request(url, callback=self.parse_category, meta={'category': category, 'award': award})
# 			yield request
#
# 	def parse_category(self, response):
# 		print('Parse function called on %s', response.url)
# 		title = response.xpath('.//title/text()').extract_first()
# 		book = nomineeItem()
# 		for div in response.xpath('.//*[@class="pollContents"]/div[@class="inlineblock pollAnswer"]'):
# 			url = div.xpath('.//a[@class="pollAnswer__bookLink"]/@href').extract_first()
# 			name = div.xpath('.//a[@class="pollAnswer__bookLink"]/img/@alt').extract_first()
# 			id = div.xpath('.//*[@id="book_id"]/@value').extract_first()
# 			book['name'] = name
# 			book['url'] = url
# 			book['id'] = id
# 			book['category'] = response.meta['category']
# 			book['award'] = response.meta['award']
# 			yield book
import scrapy
from urllib.parse import urljoin
from urllib.parse import urlparse
import re
import os.path
from GoodreadsChoiceAwards.items import nomineeItem


class NomineeSpider(scrapy.Spider):
	name = "nominees"
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
		print("URL: " + response.request.url)
		u = urlparse(response.request.url).path
		award = os.path.split(u)[1]
		for div in response.xpath(
				'.//*[@id="categories"]/div[@class="categoryContainer"]/div[@class="category clearFix"]'):
			category = div.xpath('.//a/h4/text()').extract_first().rstrip().replace('\n', '')
			url = urljoin(response.url, div.xpath('.//a/@href').extract_first())
			request = scrapy.Request(url, callback=self.parse_category, meta={'category': category, 'award': award})
			yield request

	def parse_category(self, response):
		title = response.xpath('.//title/text()').extract_first()
		book = nomineeItem()
		for div in response.xpath('.//*[@class="pollContents"]/div[@class="inlineblock pollAnswer resultShown pollAnswer--lastee"]'):
			url = div.xpath('.//a[@class="pollAnswer__bookLink"]/@href').extract_first()
			name = div.xpath('.//a[@class="pollAnswer__bookLink"]/img/@alt').extract_first()
			id = div.xpath('.//*[@id="book_id"]/@value').extract_first()
			book['name'] = name
			book['url'] = url
			book['id'] = id
			book['category'] = response.meta['category']
			book['award'] = response.meta['award']
			yield book

