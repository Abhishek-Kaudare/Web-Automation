from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('E:\Software\chromedriver')

driver.get("http://www.python.org")

assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()

elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No result found" not in driver.page_source

driver.__exit__()