import requests
from selenium import webdriver
import time
from lxml import etree
url = "https://search.jd.com/Search?keyword=%E8%A3%A4%E5%AD%90&enc=utf-8&page=1"


r = webdriver.Chrome()
r.get(url)
time.sleep(3)
r.execute_script("window.scrollBy(0,12000)")
time.sleep(6)
text = r.page_source
print(type(text))
html = etree.HTML(text)
a = html.xpath('//div[@class="m-list"]/div/div[2]/ul/li')
print(len(a))
r.close()

