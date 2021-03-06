import scrapy
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from urllib.parse import urljoin
from urllib.parse import urlparse
import json
import os
import time
from GoodreadsChoiceAwards.items import GoodreadsItem
from GoodreadsChoiceAwards.utils import convert_to_rating_stars


class DateReviewsSpider(scrapy.Spider):
	name = "date_review"
	signed_in = False
	urls = []
	flag = 0
	currentUrls = []
	for subdir, dirs, files in os.walk('RAW DATA/2019'):
		for file in files:
			if not file.startswith('.'):
				with open(os.path.join(subdir, file)) as json_file:
					data = json.load(json_file)
					category = os.path.splitext(file)[0]
					path = os.path.normpath(subdir)
					print(category, path)
					for d in data: 
						currentUrls.append(d['url'])
	print(len(currentUrls))

	if os.path.exists('2019.json'):
		with open('2019.json', 'r') as json_file:
				data = json.load(json_file)
				for book in data :
					url = book['url']
					book_url = urljoin("https://www.goodreads.com", url)
					if(book_url not in currentUrls):
						urls.append(book_url)
						flag += 1
					else:
						print('heheheheheh')
			#print(flag)
	# if os.path.exists('allBooks2014.json'):
    #          with open('allBooks2014.json', 'r') as json_file:
    #             data = json.load(json_file)
    #             for book in data :
    #                 url = book['url']
    #                 book_url = urljoin("https://www.goodreads.com", url)
    #                 urls.append(book_url)
	print('numboooooks : ', len(urls))
	start_urls = urls

	def __init__(self):
		chrome_options = webdriver.ChromeOptions()
		prefs = {"profile.managed_default_content_settings.images": 2}
		chrome_options.add_experimental_option("prefs", prefs)
		chrome_options.add_argument("--kiosk")
		self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = '/usr/local/bin/chromedriver')
		self.sign_in()

	def parse(self, response):
		wait = WebDriverWait(self.driver, 10)
		book = GoodreadsItem()
		self.driver.get(response.url)
		book['url'] = response.request.url    
		book['name'] = self.driver.find_element_by_css_selector('#bookTitle').text.strip()
		book['author'] = response.xpath('//*[@id="bookAuthors"]/span[@itemprop="author"]/div[@class="authorName__container"]/a[@class="authorName"]/span/text()').extract()
		book['average_rating'] = float(self.driver.find_element_by_xpath('//*[@id="bookMeta"]/span[@itemprop="ratingValue"]').text)
		book['reviews'] = []
        
		time.sleep(5)
		num_of_stars = 5
		self.filter_by_stars()
		time.sleep(5)

		while True:
			self.driver.execute_script("window.scrollTo(0, 250)") 
			reviews = self.driver.find_elements_by_css_selector('div#bookReviews div.review')
			for review in reviews:
				try:
					if len(review.find_elements_by_css_selector('span.staticStars')) != 0:
							book['reviews'].append({
								'rating': convert_to_rating_stars(review.find_element_by_css_selector('span.staticStars').get_attribute('title')),
								'date': datetime.datetime.strptime(review.find_element_by_css_selector('a.reviewDate').text.replace(',', ''), "%b %d %Y").date()
							})
				except:
					print("ERR")


				next_page = self.driver.find_elements_by_xpath("//a[@class='next_page']")
            
			if len(next_page) == 0:
				print("break")
				break

			next_page = self.driver.find_elements_by_xpath("//a[@class='next_page disabled']")
			if len(next_page) != 0:
				break

			elif len(self.driver.find_elements_by_xpath("//*[@rel='next']")) == 0:
				print("break")
				break

			element = self.driver.find_element_by_xpath("//a[@class='next_page']")
			actions = ActionChains(self.driver)
			time.sleep(2.5)
			actions.move_to_element(element).click().perform()
			time.sleep(5)
			
		yield book
	
	def sign_in(self):
		if not self.signed_in:
			self.driver.get('https://www.goodreads.com/')
			username = self.driver.find_element_by_id('userSignInFormEmail');
			username.send_keys('SCooperCaltech80@gmail.com')
			password = self.driver.find_element_by_id('user_password')
			password.send_keys("bazingapunk")
			self.driver.find_element_by_xpath("//input[@type='submit']").click()
			self.signed_in = True
    
	
	def filter_by_stars(self):        
		wait = WebDriverWait(self.driver, 10)
		hover_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[id^='span_class_gr-hyperlink_sort_order_span_tip_']")))
        # hover_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, " div.reviews div.reviewControls--left span.gr-hyperlink")))
		builder = ActionChains(self.driver)
		builder.move_to_element(hover_element).perform()
        # hover_element.click()
		time.sleep(2.5)
		locator = self.driver.find_elements_by_css_selector("div.tooltip.goodreads div.content.clearfix span.reviewControls__sortOrders span.loadingLinkSpan")
		print(len(locator))
		builder.move_to_element(locator[2])
		builder.click().perform()
		time.sleep(2.5)
