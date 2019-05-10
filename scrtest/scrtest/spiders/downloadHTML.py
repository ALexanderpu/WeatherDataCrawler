import scrapy
from scrapy.selector import Selector

from datetime import datetime
from datetime import timedelta
import csv
import os


class htmlsSpider(scrapy.Spider):
    name = "htmls"

    def start_requests(self):
        urls = list()
        start_date = "1945-01-01"
        stop_date = "2018-01-01"

        start = datetime.strptime(start_date, "%Y-%m-%d")
        stop = datetime.strptime(stop_date, "%Y-%m-%d")
        url = "https://www.almanac.com/weather/history/postalcode/"
        postalcode = "J0L%202N0/"

        while start < stop:
            start = start + timedelta(days=1)
            crawl_date = start.strftime("%Y-%m-%d")
            self.log("crawling date: " + crawl_date)
            path = url + postalcode + crawl_date
            # 2018-12-03
            urls.append(path)
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # pattern:  <table: class="weatherhistory_results">   tr :weatherhistory_results_section;  weatherhistory_results_datavalue
    def parse(self, response):
        cur_date = response.url.split("/")[-1]
        filename = '%s.html' % cur_date

        # data = response.xpath('//*[@id="block-system-main"]/table')
        data = response.xpath('//*[contains(@class, "value") or contains(@class, "nullvalue")]/text()').extract()
        data = [cur_date] + data
        row = ",".join(data)
        row = row +"\n"
        self.log(row)
        # check if csv file exist
        if os.path.isfile('document.csv'):
            with open('document.csv','a') as fd:
                fd.write(row)
        else:
            with open('document.csv','w+') as fd:
                fd.write(row)

        self.log('Saved current row to csv')