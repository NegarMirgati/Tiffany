import json
import copy
import os
from urllib.parse import urljoin

category = []
fix = "/Users/md/Desktop/collage/goodreads/task2/"
site = "https://www.goodreads.com"
years = list(range(2012, 2020))
datafile = [str(year)+'review.json' for year in years]

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


def get_url_filter_year(year, category, list_):
	# data = list()
	fackList = list()
	datalist = list()
	url = get_urls_category(fix + 'allBooks' + str(year) + '.json')
	[get_json_data(fix + name, url, category, datalist,fackList,year,list_) for name in datafile]
	write(datalist, year, category)
	# print("year:"+str(year), " category:"+category, " number of Books:"+str(len(datalist)))


def write_(list_,filename):
	with open(filename, 'w') as the_file:
		json.dump(list_,the_file)


# json.dump(data, the_file)

def write(data, year, category):
	with open(fix + 'data2/' + str(year) + '/' + category + '.json', 'w') as the_file:
		json.dump(data, the_file)



# [the_file.write(review) for review in data]


def get_json_data(filenames, url, category, datalist,fackList,year,list_):
	with open(filenames, 'r') as reviewjson:
		for data_ in json.load(reviewjson):
			for urlcategory in url:
				if data_['url'] == urlcategory['url'] and category == urlcategory['category'] and data_ not in fackList:
					fackList.append(copy.deepcopy( data_))
					add_write_field(data_,year,list_)
					datalist.append(data_)


def add_write_field(data,year,list_):
	num_rating = -1
	with open(fix + 'writers/' + str(year) + '.json')as writer:
		for data_w in json.load(writer):
			if data['url'].split('?')[0] == site+data_w['book_url'] and num_rating < int(data_w['num_ratings']):
				data['average_rating_w'] = data_w['average_rating']
				data['num_ratings'] = data_w['num_ratings']
				data['num_reviews'] = data_w['num_reviews']
				num_rating = int(data_w['num_ratings'])
	with open(fix+'remained.json') as writer:
		for data_w in json.load(writer):
			if data['url'].split('?')[0] == site+data_w['book_url'] and num_rating < int(data_w['num_ratings']):
				data['average_rating_w'] = data_w['average_rating']
				data['num_ratings'] = data_w['num_ratings']
				data['num_reviews'] = data_w['num_reviews']
				num_rating = int(data_w['num_ratings'])

		if num_rating == -1:
			print(data['url'])
			list_.append({'url':data['url'],'name':data['name']})
			# print(data_w['book_url'])
			data['average_rating_w'] = None
			data['num_ratings'] = None
			data['num_reviews'] = None





if __name__ == '__main__':
	list_ = list()
	for year in years:
		category = get_category(fix + 'allBooks' + str(year) + '.json')
		for category_ in category:
			get_url_filter_year(year, category_,list_)





	pass
# for name in datafile:
# 	get_urls(+name)
