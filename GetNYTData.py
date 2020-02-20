import requests
import json
import os
import ast
import csv
import time 
class NYTbooksDownloader(object):
    def __init__(self):
        self.api_keys = ['CDsHX8sy0A3plOHHhhEU8He9nP2RqZom', 'kCGRPsAnS8LmHsDNWVShdOVzYK7N0XO0', 'Uz0ei78qDYSMfo2GoUKX8CUpbqrehGIk', 'z3cuzjsAFm3wUUl2Y3YQyJYoI9axy0lL', 'Q5PSibsxrGCkVA5nm4pfnJmcMe6fpGNQ']
        self.all_lists_names_addr = 'nylists.json'
        self.books_json_addr = '2019datesAndIsbn.json'
        self.books = {}
        self.current = {}
        self.english = []
        self.current_key = 0

    def get_all_lists(self):
        payload = {'api-key': self.api_key}
        r = requests.get('https://api.nytimes.com/svc/books/v3/lists/names.json', params = payload)
        print (r.url)
        data = r.json()
        with open(self.all_lists_names_addr, 'w') as new:
            json.dump(data, new)
    
    def load_books(self):
        if os.path.exists(self.books_json_addr):
            with open(self.books_json_addr, 'r') as json_file:
                data = json.load(json_file)
                for book in data :
                    isbn = book['isbn']
                    self.books[isbn] = book['name']
                    url = book['url']
            print(self.books)
    
    def load_books_eng(self):
        if os.path.exists('2019datesAndIsbn.json'):
            with open('2019datesAndIsbn.json', 'r') as json_file:
                data = json.load(json_file)
                for book in data :
                    if(book['isbn'] == "English"):
                        self.english.append(book)
                        print('HERE')
            print(len(self.english))
     
    def extract_data_by_isbn(self):
        i = 0
        data_dict = {}
        flag = False
        for key, value in self.books.items():
            flag = False
            if(key not in data_dict):
                print(key, value)
                while(flag == False):
                    sleep = 1
                    data = self.process_history_request(key)
                    if('fault' in data):
                        print('FAULT')
                        sleep = sleep * 2
                        time.sleep(sleep)
                        self.current_key = (self.current_key + 1) % 5
                        continue
                    elif ( data['status'] != 'OK'):
                        print('OOOOOOPS')
                    elif(data['status'] == 'OK'):
                        data_dict[key] = data
                        with open('res12.json', 'w') as outfile:
                            json.dump(data_dict, outfile)
                        i = i + 1
                        print(i)
                        flag = True
                    else:
                        print(data)
        
        with open('result.json', 'w') as fp:
            json.dump(data_dict, fp)

    def extract_data_by_name(self):
        i = 0
        data_dict = {}
        flag = False
        #with open('rems_cleaned.json', 'r') as json_file:
            #data = json.load(json_file)  
        for i in range(0, len(self.english)):
            d = self.english[i]
            print(i)
            key = d['url']
            value = d['name']
            author = d['author']
            flag = False
            if(key not in data_dict):
                print(value)
                while(flag == False):
                    sleep = 1
                    data = self.process_history_request_name(value, author)
                    if('fault' in data):
                        print('FAULT')
                        sleep = sleep * 2
                        time.sleep(sleep)
                        self.current_key = (self.current_key + 1) % 5
                        continue
                    elif ( data['status'] != 'OK'):
                        print('OOOOOOPS')
                    elif(data['status'] == 'OK'):
                        data_dict[key] = data
                        with open('res13.json', 'w') as outfile:
                            json.dump(data_dict, outfile)
                        i = i + 1
                        print(i)
                        flag = True
                    else:
                        print(data)
            
        with open('result.json', 'w') as fp:
            json.dump(data_dict, fp)
            
    def process_history_request_name(self, title, author):
        payload = {'api-key' : self.api_keys[self.current_key], 'title' : title, 'author' : author}
        r = requests.get('https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json', params = payload)
        return(r.json())


    def process_history_request(self, isbn):
        payload = {'api-key' : self.api_keys[self.current_key], 'isbn' : isbn}
        r = requests.get('https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json', params = payload)
        return(r.json())


def main() :
    nytdl = NYTbooksDownloader()
    nytdl.load_books_eng()
    nytdl.extract_data_by_name()
    

if __name__== "__main__":
      main()
