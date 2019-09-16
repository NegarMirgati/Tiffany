# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

def convert_to_rating_stars(string):
    return {
        'it was amazing': 5,
        'really liked it': 4,
        'liked it': 3,
        'it was ok': 2,
        'did not like it': 1,
        'not rated': 0
    }[string]