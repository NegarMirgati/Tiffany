# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy

class GoodreadsItem(scrapy.Item):
    name = scrapy.Field()
    average_rating = scrapy.Field()
    author = scrapy.Field()
    reviews = scrapy.Field()
    num_of_raters = scrapy.Field()
    rating_distribution = scrapy.Field()
    url = scrapy.Field()
    pass

class nomineeItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    category = scrapy.Field()
    award = scrapy.Field()
    pass
    
class GoodreadsItemWithEdition(scrapy.Item):
    name = scrapy.Field()
    average_rating = scrapy.Field()
    reviews = scrapy.Field()
    edition_language = scrapy.Field()
    pass

class BookEditionItem(scrapy.Item):
    name = scrapy.Field()
    original_name = scrapy.Field()
    averageRating = scrapy.Field()
    numOfRaters = scrapy.Field()
    language = scrapy.Field()
    pass

class BookEditionsItem(scrapy.Item):
    name = scrapy.Field()
    urls = scrapy.Field()
    pass

class ListItem(scrapy.Item):
    name = scrapy.Field()
    bookUrls = scrapy.Field()
    pass

class WriterItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    average_rating = scrapy.Field()
    num_reviews = scrapy.Field()
    num_ratings = scrapy.Field()
    book_url =  scrapy.Field()
    pass

class BookDateItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
    isbn = scrapy.Field()
    pass
    
class BookListEditions(scrapy.Item):
    dic = scrapy.Field()
