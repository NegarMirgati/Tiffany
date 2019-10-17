import scrapy
from GoodreadsChoiceAwards.items import GoodreadsItem

class ReviewsSpider(scrapy.Spider):
    name = "reviews"
    start_urls = [
        'https://www.goodreads.com/book/show/29056083-harry-potter-and-the-cursed-child?ac=1&from_search=true'
    ]

    def parse(self, response):
        book = GoodreadsItem()
        book['name'] = response.css('#bookTitle::text').extract_first().strip()
        book['author'] = response.xpath('//*[@id="bookAuthors"]/span[@itemprop="author"]/div[@class="authorName__container"]/a[@class="authorName"]/span/text()').extract()
        book['average_rating'] = float(response.xpath('//*[@id="bookMeta"]/span[@itemprop="ratingValue"]/text()').extract_first())
        book['reviews'] = []
        for review in response.css('div#bookReviews div.review'):
            if len(review.css('span.staticStars')) != 0:
                book['reviews'].append({
                    'rating': self.convert_to_rating_stars(review.css('span.staticStars').xpath('@title').extract_first()),
                    'date' : review.xpath('.//a[@class="reviewDate createdAt right"]/text()').extract_first()
                })
        #next_page = response.xpath("//a[@class='next_page']").extract_first()
        #if next_page is not None :
        #    yield response.follow(next_page, callback=self.parse)
        #else :
        yield book
        
    def convert_to_rating_stars(self, string):
        return {
            'it was amazing': 5,
            'really liked it': 4,
            'liked it': 3,
            'it was ok': 2,
            'did not like it': 1    
        }[string]