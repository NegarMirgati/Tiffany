import scrapy
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json
import time
<<<<<<< Updated upstream
from .goodreads.items import GoodreadsItem
from .ReviewsSpider import convert_to_rating_stars
=======
from GoodreadsChoiceAwards.items import GoodreadsItem
from GoodreadsChoiceAwards.utils import convert_to_rating_stars
>>>>>>> Stashed changes
from webdriver_manager.chrome import ChromeDriverManager

class DateReviewsSpider(scrapy.Spider):
    name = "date_review"
    signed_in = False
    
    start_urls = [
        'https://www.goodreads.com/book/show/22628.The_Perks_of_Being_a_Wallflower'
    ]

    def __init__(self):
<<<<<<< Updated upstream
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
=======
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = '/usr/local/bin/chromedriver')
        self.sign_in()
>>>>>>> Stashed changes

    def parse(self, response):
        wait = WebDriverWait(self.driver, 10)
        book = GoodreadsItem()
        
        self.sign_in()
        self.driver.get(response.url)
            
        book['name'] = self.driver.find_element_by_css_selector('#bookTitle').text.strip()
        # book['average_rating'] = float(self.driver.find_element_by_css_selector('span.value span.average').text)
        book['reviews'] = []
        
        index = 5
        self.sort_by_stars(index)
        time.sleep(5)
        
        while True:
            self.driver.execute_script("window.scrollTo(0, 250)") 
            reviews = self.driver.find_elements_by_css_selector('div#bookReviews div.review')
            for review in reviews:
                if len(review.find_elements_by_css_selector('span.staticStars')) != 0:
                    book['reviews'].append({
                        'reviewer': review.find_element_by_css_selector('a.user').get_attribute('href'),
                        'rating': convert_to_rating_stars(review.find_element_by_css_selector('span.staticStars').get_attribute('title')),
                        'date': datetime.datetime.strptime(review.find_element_by_css_selector('a.reviewDate').text.replace(',', ''), "%b %d %Y").date()
                    })

            next_page = self.driver.find_elements_by_xpath("//a[@class='next_page']")
            if len(next_page) == 0:
                break
                print("no next")
                if index == 5:
                    break
                index += 1
                self.sort_by_stars_again(index)
                continue
            elif len(self.driver.find_elements_by_xpath("//*[@rel='next']")) == 0:
                print("no next again")
                if index == 5:
                    break
                index += 1
                self.sort_by_stars_again(index)
                continue
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
            username.send_keys('nsh.nightingale@yahoo.com')
            password = self.driver.find_element_by_id('user_password')
            password.send_keys("Fytvig-sejmi0-xirbyk")
        
            self.driver.find_element_by_xpath("//input[@type='submit']").click()
            self.signed_in = True
            
    def sort_by_date(self):
        wait = WebDriverWait(self.driver, 10)
        hover_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[id^='span_class_gr-hyperlink_sort_span']")))
        # hover_element = self.driver.find_element_by_css_selector("[id^='span_class_gr-hyperlink_filter_span']")
        # hover_element = self.driver.find_elements_by_css_selector('div.reviewControls--right a.uitext')[1]
        builder = ActionChains(self.driver)
        builder.move_to_element(hover_element).perform()
        time.sleep(2.5)
        locator = self.driver.find_element_by_xpath("//span[@class='reviewControls__sortOrders']/span[@class='loadingLinkSpan'][3]")
        builder.move_to_element(locator)
        builder.click().perform()
        time.sleep(2.5)
        # data[0]['reviews'].sort(key = lambda r: r['date'])
        
    def sort_by_stars(self, stars):        
        wait = WebDriverWait(self.driver, 10)
        hover_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[id^='span_class_gr-hyperlink_filter_span']")))
        builder = ActionChains(self.driver)
        builder.move_to_element(hover_element).perform()
        time.sleep(2.5)
        locator = self.driver.find_elements_by_css_selector("div.content div.greyText span.loadingLinkSpan")
        print(len(locator))
        builder.move_to_element(locator[stars])
        builder.click().perform()
        time.sleep(2.5)
        
    def sort_by_stars_again(self, stars):        
        wait = WebDriverWait(self.driver, 10)
        builder = ActionChains(self.driver)
        hover_element = self.driver.find_elements_by_css_selector("[id^='span_class_gr-hyperlink_filter_span']")
        print(len(hover_element))
        # self.driver.execute_script("window.scrollTo(0, 700)")
        builder.move_to_element(self.driver.find_element_by_xpath("//div[@class='footerContainer']")).perform()
        time.sleep(2.5)
        
        builder.move_to_element(hover_element[0]).perform()
        # builder.click().perform()
        time.sleep(2.5)
        
        print('hey1')
        locator = self.driver.find_elements_by_css_selector("div.tooltip div.content div.greyText span.loadingLinkSpan")
        print(len(locator))
        builder.move_to_element(locator[stars+6*(stars-1)])
        builder.click().perform()
        time.sleep(5)