import json
import os
from urllib.parse import urljoin

repurl=[]
with open('/Users/md/Desktop/collage/goodreads/task2/reviews.json', 'r') as reviewjson:
	repurl = [data_["url"] for data_ in json.load(reviewjson)]

urls2009=[]
urls2010 = []
urls2011= []
urls2012=[]
urls2013 = []
urls2014 = []
urls2015 = []
urls2016 = []
urls2017 = []
urls2018 = []
if os.path.exists('/Users/md/Desktop/collage/goodreads/task2/allBooks.json'):
		with open('/Users/md/Desktop/collage/goodreads/task2/allBooks.json', 'r') as json_file:
			data = json.load(json_file)
			for book in data:
				if book['award']== "best-books-2009" and urljoin("https://www.goodreads.com",book['url']) not in repurl:
					urls2009.append(urljoin("https://www.goodreads.com",book['url']))
				elif book['award']== "best-books-2010" and urljoin("https://www.goodreads.com",book['url']) not in repurl:
					urls2010.append(urljoin("https://www.goodreads.com",book['url']))
				elif book['award'] == "best-books-2011" and urljoin("https://www.goodreads.com", book['url']) not in repurl:
					urls2011.append(urljoin("https://www.goodreads.com", book['url']))
				elif book['award'] == "best-books-2012" and urljoin("https://www.goodreads.com", book['url']) not in repurl:
					urls2012.append(urljoin("https://www.goodreads.com", book['url']))
				elif book['award'] == "best-books-2013" and urljoin("https://www.goodreads.com", book['url']) not in repurl:
					urls2013.append(urljoin("https://www.goodreads.com", book['url']))
				elif book['award'] == "best-books-2014" and urljoin("https://www.goodreads.com", book['url']) not in repurl:
					urls2014.append(urljoin("https://www.goodreads.com", book['url']))
				elif book['award'] == "best-books-2015" and urljoin("https://www.goodreads.com", book['url']) not in repurl:
					urls2015.append(urljoin("https://www.goodreads.com", book['url']))
				elif book['award'] == "best-books-2016" and urljoin("https://www.goodreads.com", book['url']) not in repurl:
					urls2016.append(urljoin("https://www.goodreads.com", book['url']))
				elif book['award'] == "best-books-2017" and urljoin("https://www.goodreads.com", book['url']) not in repurl:
					urls2017.append(urljoin("https://www.goodreads.com", book['url']))
				else:
					urls2018.append(urljoin("https://www.goodreads.com", book['url']))

					
with open('urls2009.txt', 'w') as filehandle:
	for listitem in urls2009:
		filehandle.write('%s\n' % listitem)
						
				
with open('urls2010.txt', 'w') as filehandle:
	for listitem in urls2010:
		filehandle.write('%s\n' % listitem)

with open('urls2011.txt', 'w') as filehandle:
	for listitem in urls2011:
		filehandle.write('%s\n' % listitem)

with open('urls2012.txt', 'w') as filehandle:
	for listitem in urls2012:
		filehandle.write('%s\n' % listitem)

with open('urls2013.txt', 'w') as filehandle:
	for listitem in urls2013:
		filehandle.write('%s\n' % listitem)

with open('urls2014.txt', 'w') as filehandle:
	for listitem in urls2014:
		filehandle.write('%s\n' % listitem)
with open('urls2015.txt', 'w') as filehandle:
	for listitem in urls2015:
		filehandle.write('%s\n' % listitem)

with open('urls2016.txt', 'w') as filehandle:
	for listitem in urls2016:
		filehandle.write('%s\n' % listitem)
with open('urls2017.txt', 'w') as filehandle:
	for listitem in urls2017:
		filehandle.write('%s\n' % listitem)

with open('urls2018.txt', 'w') as filehandle:
	for listitem in urls2018:
		filehandle.write('%s\n' % listitem)
