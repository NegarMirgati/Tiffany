import scrapy
from urllib.parse import urlparse
import os.path
from GoodreadsChoiceAwards.items import BookDateItem
import json
import re
import copy 

class DateSpider(scrapy.Spider):
    name = "dates"
    urls = []
    flag = 0
    currentUrls = []
    yearDict = {}
    # for subdir, dirs, files in os.walk('allBooks/'):
    #     for file in files:
    #         if not file.startswith('.'):
    #             with open(os.path.join(subdir, file)) as json_file:
    #                 print(file)
    #                 result = re.search('allBooks(.*).json', file)
    #                 year = result.group(1)
    #                 data = json.load(json_file)
    #                 path = os.path.normpath(subdir)
    #                 for d in data: 
    #                     url = 'https://www.goodreads.com' + d['url']
    #                     currentUrls.append(url)
    #                     if(url not in yearDict):
    #                         yearDict[url] = [year]
    #                     else:
    #                         yearDict[url].append(year)
    #                         #print(url, yearDict[url])
    if os.path.exists('2019.json'):
        with open('2019.json') as json_file:
            data = json.load(json_file)
            for d in data: 
                print(d)
                currentUrls.append('https://www.goodreads.com' +  d['url'])    
            print(currentUrls)

                    
    print('sssss', len(currentUrls))
    start_urls = currentUrls

    def parse(self, response):
        print("URL: " + response.request.url)
        book = BookDateItem()
        book['url'] = response.request.url
        book['name'] = response.xpath('//*[@id="bookTitle"]/text()').extract_first().rstrip().replace('\n', '').lstrip()
        book['date'] = response.xpath('//*[@id="details"]/div[2]/text()').extract_first().rstrip().replace('\n', '').lstrip()
        book['isbn'] = response.xpath('//*[@id="bookDataBox"]/div[2]/div[2]/text()').extract_first().rstrip().replace('\n', '').lstrip()
        book['author'] = response.xpath('//*[@id="bookAuthors"]/span[@itemprop="author"]/div[1]/a[1]/span[@itemprop="name"]/text()').extract_first().rstrip().replace('\n', '').lstrip()
        yield book

