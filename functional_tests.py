from selenium import webdriver

browser = webdriver.Chrome('E:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
browser.get('http://localhost:8000')

assert 'Django' in browser.title