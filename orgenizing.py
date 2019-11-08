import json
import os
from urllib.parse import urljoin

category = []
fix = "/Users/md/Desktop/collage/goodreads/task2/"
site = "https://www.goodreads.com"
datafile = ["reviews.json", "reviews2.json", "review3.json", "reviews4.json"]
years = list(range(2009, 2019))


def get_urls_category(file):
	with open(file, 'r') as reviewjson:
		url = [{'url': site + data_["url"], 'category': data_["category"]} for data_ in json.load(reviewjson)]
		# print(type(url))
		return url

def get_category(file):
	with open(file, 'r') as reviewjson:
		category=  [data_["category"] for data_ in json.load(reviewjson)]
		return category

def get_url_filter_year(year, category):
	# data = list()
	datalist = list()
	url = get_urls_category(fix + 'allBooks' + str(year) + '.json')
	[get_json_data(fix + name, url, category , datalist) for name in datafile]
	# print(data)
	write(datalist, year, category)


def write(data, year, category):
	with open(fix + 'data/'+ str(year) +'/'+ category + '.json', 'w') as the_file:
		json.dump(data, the_file)


# [the_file.write(review) for review in data]


def get_json_data(filenames, url, category, datalist):

	with open(filenames, 'r') as reviewjson:
		for data_ in json.load(reviewjson):
			for urlcategory in url:
				if data_['url'] in urlcategory['url'] and category in urlcategory['category']:
					datalist.append(data_)




if __name__ == '__main__':

	for year in years:
		category = get_category(fix + 'allBooks' + str(year) + '.json')
		for category_ in category:
			get_url_filter_year(year, category_)
	pass
# for name in datafile:
# 	get_urls(+name)
