import json
import os
from urllib.parse import urljoin

category = []
fix = "/Users/md/Desktop/collage/goodreads/task2/"
site = "https://www.goodreads.com"
datafile = ["reviews.json","oldreviews.json", "oldreviews2.json", "oldreview3.json", "oldreviews4.json",
            "2013_remained.json", "reviews_extra_2011.json","reviews_extra_2012.json","reviews_extra_2014.json",
            "reviews_extra_2015.json","2013_jome.json","2015_jome.json","2012_jome.json","2014_jome.json"]
years = list(range(2011, 2019))
# years = [2018]


def get_urls_category(file):
	with open(file, 'r') as reviewjson:
		url = [{'url': site + data_["url"], 'category': data_["category"]} for data_ in json.load(reviewjson)]
		# print(type(url))
		return url


def get_category(file):
	with open(file, 'r') as reviewjson:
		category = [data_["category"] for data_ in json.load(reviewjson)]
		return set(category)


def get_url_filter_year(year, category):
	# data = list()
	fackList = list()
	datalist = list()
	url = get_urls_category(fix + 'allBooks' + str(year) + '.json')
	[get_json_data(fix + name, url, category, datalist,fackList,year) for name in datafile]
	write(datalist, year, category)
	print("year:"+str(year), " category:"+category, " number of Books:"+str(len(datalist)))


def write(data, year, category):
	with open(fix + 'data1/' + str(year) + '/' + category + '.json', 'w') as the_file:
		json.dump(data, the_file)



# [the_file.write(review) for review in data]


def get_json_data(filenames, url, category, datalist,fackList,year):
	with open(filenames, 'r') as reviewjson:
		for data_ in json.load(reviewjson):
			for urlcategory in url:
				if data_['url'] == urlcategory['url'] and category == urlcategory['category'] and data_ not in fackList:
					fackList.append(data_)
					add_write_field(data_,year)
					datalist.append(data_)


def add_write_field(data,year):
	with open(fix + 'writers/' + str(year) + '.json')as writer:
		num_rating = 0
		for data_w in json.load(writer):
			if data['url'].split('?')[0] == site+data_w['book_url'] and num_rating <int(data_w['num_ratings']):
				data['average_rating_w'] = data_w['average_rating']
				data['num_ratings'] = data_w['num_ratings']
				data['num_reviews'] = data_w['num_reviews']
				num_rating = int(data_w['num_ratings'])




if __name__ == '__main__':

	for year in years:
		category = get_category(fix + 'allBooks' + str(year) + '.json')
		for category_ in category:
			get_url_filter_year(year, category_)
	pass
# for name in datafile:
# 	get_urls(+name)
