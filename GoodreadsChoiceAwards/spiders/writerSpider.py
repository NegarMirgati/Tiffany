# import scrapy
# from urllib.parse import urljoin
# from urllib.parse import urlparse
# import re
# import os.path
# import json
# from GoodreadsChoiceAwards.items import WriterItem

# class WriterSpider(scrapy.Spider):
#     name = "writers"
#     urls = []
#     # current =[]
#     # with open('writers/wr3.json', 'r') as crawled:
#     #     data_crawled = json.load(crawled)
#     #     for d in data_crawled : 
#     #         current.append(urljoin("https://www.goodreads.com", d['url'] + '?from_choice=true'))

#     with open('allBooks2011.json', 'r') as json_file:
#         data = json.load(json_file)  
#         for book in data :
#             url = book['url']
#             book_url = urljoin("https://www.goodreads.com", url)
#             urls.append(book_url)
#     start_urls = urls


#     def parse(self, response):
#         book_url = urlparse(response.request.url).path
#         for author in response.xpath('.//*[@id="bookAuthors"]/span[@itemprop="author"]/div[@class="authorName__container"]'):
#             name = author.xpath('.//a[@class="authorName"]/span/text()').extract_first()
#             url =  author.xpath('.//a[@class="authorName"]/@href').extract_first()
#             request = scrapy.Request(url, callback = self.get_writer_info, meta = {'name' : name, 'url' : url, 'book_url' : book_url})
#             yield request

#     def get_writer_info(self, response):
#         writer = WriterItem()
#         print('Parse function called on %s', response.url)
#         writer['average_rating'] = response.xpath('.//*[@class="hreview-aggregate"]/span[@class="rating"]/span[@class="average"]/text()').extract_first()
#         writer['num_ratings'] = response.xpath('.//*[@class="hreview-aggregate"]/span[@class="votes"]/span[@class="value-title"]/@content').extract_first()
#         writer['num_reviews'] = response.xpath('.//*[@class="hreview-aggregate"]/span[@class="count"]/span[@class="value-title"]/@content').extract_first()
#         writer['name'] = response.meta['name']
#         writer['url'] = response.meta['url']
#         writer['book_url'] = response.meta['book_url']
#         yield writer