# Thanks to [Reference](https://medium.com/analytics-vidhya/web-data-scraping-with-python-selenium-7a1e91206642)
from selenium.webdriver import Chrome
import pandas as pd
webdriver = r"/Users/kang/Downloads/chromedriver" ### put your browser driver's path
driver = Chrome(webdriver)
driver.get("https://www.itftennis.com/en/tournament-calendar/mens-world-tennis-tour-calendar?startDate=2019-12") ### here the website url
items = len(driver.find_elements_by_class_name("whatson-table__tournament")) ### here you put the class name of the HTML element which contains the data to scrap
total = []
for item in range(items):
        items = driver.find_elements_by_class_name("whatson-table__tournament")
        for item in items:
            t_name = item.find_element_by_class_name('name').text
            t_date = item.find_element_by_class_name('date').text
            t_hostname = item.find_element_by_class_name('hostname').text
            t_location = item.find_element_by_class_name('location').text
            t_category = item.find_element_by_class_name('category').text
            t_prize_money = item.find_element_by_class_name('prize-money').text
            t_surface = item.find_element_by_class_name('surface').text
            t_status = item.find_element_by_class_name('status').text
            new = ((t_name, t_date, t_hostname, t_location, t_category,t_prize_money,t_surface,t_status))
            total.append(new)
df = pd.DataFrame(total, columns=['Name', 'Date', 'Hostname','Location','Category','Prize Money','Surface','Status'])
df.to_csv('itf_tournaments.csv')
driver.close()
