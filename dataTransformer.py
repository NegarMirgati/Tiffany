import csv
import json
import datetime
from dateutil.parser import parse
import os

class dataTransformer(object):
    award_dates = {}
    winners = {}
    winners_found = 0
    rootdir = 'mona/data'
    def import_award_dates(self):
        with open('AwardDates.csv', mode='r') as infile:
            reader = csv.reader(infile)
            count = 0
            for row in reader:
                count = count + 1
                if(count == 1):
                    continue
                key = row[0]
                if key in self.award_dates:
                   pass
                self.award_dates[key] = row[1:]

    def extract_winners(self):
        with open('winners.json') as json_file:
            data = json.load(json_file)
            for d in data:
                self.winners[d['name']] = None
            
    def create_csv(self):
        with open('goodreads_output.csv', mode='w') as employee_file:
            output_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            output_writer.writerow(['year', 'name', 'writer', 'category', 'winner', 'num 1 stars', 'num 2 stars', 'num 3 stars', 'num 4 stars', 'num 5 stars', 'average rating'])
            for subdir, dirs, files in os.walk(self.rootdir):
                for file in files:
                    if not file.startswith('.'):
                        with open(os.path.join(subdir, file)) as json_file:
                            data = json.load(json_file)
                            category = os.path.splitext(file)[0]
                            path = os.path.normpath(subdir)
                            year = (path.split(os.sep))[3]
                            for d in data : 
                                name = d['name']
                                author = d['author']
                                num_stars = [0] * 5
                                for review in d['reviews']:
                                    review_date_str = review['date']
                                    if(self.reviewed_before_contest(year, review_date_str)):
                                        self.calc_star_nums(review, num_stars)
                                average = self.calc_average(num_stars)
                                output_writer.writerow([year, name, author, category, self.is_winner(name), num_stars[0], num_stars[1], num_stars[2], num_stars[3], num_stars[4], average])
            print(self.winners_found)
    
    def reviewed_before_contest(self, contest_year, review_date_str):
        winners_announced = self.award_dates[contest_year][3]
        end_date = parse(winners_announced).date()
        review_date = parse(review_date_str).date()
        if(review_date < end_date):
            return True
        return False

    def calc_star_nums(self, dict, num_stars):
        rating = int(dict['rating'])
        num_stars[rating - 1] += 1
    
    def calc_average(self, num_stars):
        sum = 0
        denum = 0
        for i in range(1, 6):
            sum = sum + num_stars[i - 1] * i
            denum = denum + num_stars[i - 1]
        return sum/denum
    
    def is_winner(self, name):
        if name in self.winners:
            print("THIS IS A WINNNNNNERRRRR")
            self.winners_found += 1
            return 1
        else :
            return 0


def main():
    d = dataTransformer()
    d.extract_winners()
    d.import_award_dates()
    d.create_csv()

if __name__== "__main__":
  main()