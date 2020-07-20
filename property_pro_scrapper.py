# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 08:03:02 2020

@author: 60004501
"""
#Importing Libaries
###############################################################################
import pandas as pd 
import time
from tqdm import tqdm
import selenium
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
webD = wb.Chrome('C:/Users/60004501/Chrome driver/chromedriver.exe')
webD.get('https://www.propertypro.ng/property-for-rent/in/lagos/')
################################################################################

#A quick look at elements we need to scrap Data from
properties = webD.find_elements_by_class_name('col-lg-12')
print(properties)

#Property Title
property_title = webD.find_element_by_xpath('/html/body/section[2]/div/div[2]/div[1]/div/div[6]/div/div[1]/div[2]/div[1]/a/h2').text
print(property_title)

#Property Location
property_location = webD.find_element_by_xpath('/html/body/section[2]/div/div[2]/div[1]/div/div[6]/div/div[1]/div[2]/h3[1]').text
print(property_location)

#Property Features
property_features = webD.find_element_by_xpath('/html/body/section[2]/div/div[2]/div[1]/div/div[6]/div/div[1]/div[2]/div[2]/span').text
print(property_features)

#Marketing Company
marketing_company = webD.find_element_by_xpath('/html/body/section[2]/div/div[2]/div[1]/div/div[6]/div/div[1]/div[2]/div[3]/small/a').text
print(marketing_company)

#Link to particular property 
property_link = webD.find_element_by_xpath('/html/body/section[2]/div/div[2]/div[1]/div/div[15]/div/div[1]/div[2]/div[1]/a').get_attribute(name="href")
print(property_link)

###################################################################################

# Looping through each property and getting all required details

alldetails =[]  
condition = True
while condition:
    
    time.sleep(2)
    properties = webD.find_elements_by_xpath('//div[contains(@class,"col-lg-8")]')
    for prop in properties:
       
        
        title = prop.find_element_by_xpath('.//h2[contains(@class,"title prop-title")]').text
        location = prop.find_element_by_xpath('.//h3[contains(@class,"pro-location")]').text
        price = prop.find_element_by_xpath('.//p[contains(@class,"prop-price")]').text
        features = prop.find_element_by_xpath('.//span[contains(@class,"prop-aminities float-left")]').text
        links = prop.find_element_by_xpath('.//div[@class="pro-main-cont"]//a').get_attribute(name="href")
        tempj = {"property_title":title,"property_location":location,"property_price":price, "property_features": features, 'property_link':links}
        alldetails.append(tempj)
        
    try:
        webD.find_elements_by_class_name('page-link')[-1].click()
    except:
        condition = False
######################################################################################

#Converting scrapped data into a Data frame and storing data in a CSV file.
data = pd.DataFrame(alldetails)
data.to_csv("property_list_2.csv", index = False)

######################################################################################

df = pd.read_csv('property_list_2.csv')













