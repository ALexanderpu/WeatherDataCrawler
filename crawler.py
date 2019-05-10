from datetime import datetime

start_date = "1945-01-01"
stop_date = "1945-05-01"

start = datetime.strptime(start_date, "%Y-%m-%d")
stop = datetime.strptime(stop_date, "%Y-%m-%d")

from datetime import timedelta

url = "https://www.almanac.com/weather/history/postalcode/"
postalcode = "J0L%202N0/"

while start < stop:
    start = start + timedelta(days=1)
    crawl_date = start.strftime("%Y-%m-%d")
    print("crawling date: " + crawl_date)
    path = url + postalcode + crawl_date
    # 2018-12-03

    # pattern:  <table: class="weatherhistory_results">
    
