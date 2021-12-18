from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
x = int(input('number of the video in a link: '))
x1 = int(input('Enter try number: '))

i = 0
driver = webdriver.Chrome()
driver.get(f'https://www.aparat.com/video/video/list/tagid/18/catid/2/perpage/{x}/nextid/40011202/isnextpage/true')
wait = WebDriverWait(driver, 60)
link, channelname, idsh = [], [], []
for xxx in driver.find_elements_by_class_name('thumb-preview'):
    link.append(xxx.get_attribute("href"))
    idsh.append(xxx.get_attribute("id"))
wait = WebDriverWait(driver, 60)
for xxx in driver.find_elements_by_class_name('thumb-channel'):
    channelname.append(xxx.get_attribute("href"))
for xx in range(x1):
    obj = idsh.pop()
    driver.get(f'https://www.aparat.com/video/video/list/tagid/18/catid/2/perpage/{x}/nextid/{obj}/isnextpage/true')
    wait = WebDriverWait(driver, 60)
    for xxx in driver.find_elements_by_class_name('thumb-preview'):
        link.append(xxx.get_attribute("href"))
        idsh.append(xxx.get_attribute("id"))
    wait = WebDriverWait(driver, 60)
    for xxx in driver.find_elements_by_class_name('thumb-channel'):
        channelname.append(xxx.get_attribute("href"))
df1 = pd.DataFrame(list(zip(channelname, link, idsh)), columns= ['Channel', 'Link', 'ID'], )
df1.to_excel("output.xlsx")
driver.close()


# print(len(b) != len(set(b)))
# print(b.pop())
# print(channelname.pop())
# print(len(channelname))
# print(len(link), len(channelname))
