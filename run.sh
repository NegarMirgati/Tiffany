#!/usr/bin/env bash
scrapy crawl nominees -o allBooks.json
scrapy crawl date_review -o reviews1.json
