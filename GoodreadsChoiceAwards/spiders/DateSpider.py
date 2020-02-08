import scrapy
from urllib.parse import urlparse
import os.path
from GoodreadsChoiceAwards.items import BookDateItem
import json

class DateSpider(scrapy.Spider):
	name = "dates"
	urls = []
	flag = 0
	currentUrls = []
	for subdir, dirs, files in os.walk('allBooks/'):
		for file in files:
			if not file.startswith('.'):
				with open(os.path.join(subdir, file)) as json_file:
					data = json.load(json_file)
					path = os.path.normpath(subdir)
					for d in data: 
						currentUrls.append('https://www.goodreads.com' + d['url'])
	print('sssss', len(currentUrls))
	start_urls = currentUrls

	def parse(self, response):
		print("URL: " + response.request.url)
		book = BookDateItem()
		book['url'] = response.request.url
		book['name'] = response.xpath('//*[@id="bookTitle"]/text()').extract_first().rstrip().replace('\n', '')
		book['date'] = response.xpath('//*[@id="details"]/div[2]/text()').extract_first().rstrip().replace('\n', '')
		yield book

