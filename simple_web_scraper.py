# Thanks to https://medium.com/@joonasvenlinen/build-simple-web-scraper-using-python-selenium-f0376b6cc8fa

from os import system
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


while(True):
    # Ask from user what to search
    search_word = raw_input("What to search?: ")

	# Uncomment this to run chrome normally
	#driver = webdriver.Chrome()
	# If you want to run headless uncomment first three lines
    options = Options()
    options.set_headless(headless=True)
    driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
    wait = WebDriverWait(driver, 5)
    driver.get("http://google.com")
    system('cls')
    search_input = driver.find_element_by_name("q")
    search_input.send_keys(search_word + " site:stackoverflow.com")
    search_input.send_keys(Keys.RETURN)


    # Check if page contains element
    def element_is_present(xpath):
        try:
            driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True

    # Wait until results are visible
    results = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="r"]/a')))

    # Open the first result
    results[0].click()

    # If page contains acccepted answer
    if element_is_present('//div[@class="answer accepted-answer"]'):
        answer = driver.find_element(By.XPATH, '//div[@class="answer accepted-answer"]//pre//code')
        print("### Answer ###")
        print(answer.text)

    # If there is no accepted answer get all the code blocks from the topic
    else:
        code_blocks = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//pre/code')))
        for i in range(0,len(code_blocks)):
            print(code_blocks[i].text+"\n\n")

    driver.quit()
