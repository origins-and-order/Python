from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import sys

# connect to Chrome browser
driver = webdriver.Chrome()

# go to webpage
driver.get("https://my.utrgv.edu/home")

# go to class schedule
elem = driver.find_element_by_css_selector('#portlet_56_INSTANCE_tHQyBPIrksaK > div > div > div > div.journal-content-article > section > div > section.resources.row.unhinge.white-bg.medium-block.float-left > ul > li:nth-child(8) > a')

# click on it
elem.click()

# find fall 2016
elem = driver.find_element_by_css_selector('#term_input_id > option:nth-child(4)')

# select fall 2016
elem.click()

# find submit
elem = driver.find_element_by_css_selector('body > div.pagebodydiv > form > input[type="submit"]:nth-child(5)')

# submit
elem.click()

# find computer science
elem = driver.find_element_by_css_selector('#subj_id > option:nth-child(22)')

# click the option
elem.click()

# find class search
elem = driver.find_element_by_css_selector('body > div.pagebodydiv > form > input[type="submit"]:nth-child(15)')

# class search
elem.click()

# find all classes
classes = driver.find_elements_by_css_selector('th.ddtitle')

for _class in classes:
    print _class.text

# write to excel file
f = open('classes.csv', 'wt')

try:
    writer = csv.writer(f)
    writer.writerow(('Classes',         )) # these are columns
    for _class in classes:
        writer.writerow((str(_class.text),    ))
finally:
    f.close()

# close da browser
driver.close()