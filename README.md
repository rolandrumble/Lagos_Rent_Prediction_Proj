# House Rent Price Estimator in Lagos State: Project Overview / Objective
- Lagosians (People residing within Lagos) knows getting an accommodation is one **Herculean** task especially with the whole agent and agreement complications, it can be very frustrating!!!. 
- Created a tool that estimates House rent prices within Lagos State, Nigeria. The Objective of this project, is basically to help current residents and individuals planning to relocate to the Center Of Excellence (Nickname for Lagos State), have a fair idea of current prices of rented apartment per area and make informed decisions based on their budget.
- Scrapped over 9000 properties from propertypro.ng (One of Nigeria's Formost Property sites) usisng python and selenium
- Engineered Featured from the text of each property description (Number of Bedrooms, Toilet and Bathrooms) to quantity the Price /value of the Apartment.
- Optimised Linear, Lasso, and Decision Trees Using GridSearch CV to reach the best Model
- Built a Client Facing API Using Flask

## Code and Resources Used 
**Python Version:** 3.8
**Packages:** Pandas, Numpy, Sklearn, Matplotlib, Seaborn, selenium, Flask, json, pickle
**Scrapper Guide (Github):** [https://github.com/arapfaik/scraping-glassdoor-selenium/blob/master/glassdoor%20scraping.ipynb]
**Scrapper Article Guide:** [https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905]
**Flask Productionization:** [https://github.com/codebasics]

## Web Scraping 
Got insight from webscrapping github repo (above) to scrap 9000 properties from Propertypro.ng. With each property Scrapped we got the following:
- Number of Bedrooms per Apartment
- Number of Bathrooms for each Property
- Number of Toilets
- Location 
- Links to each property (For more detiails (Pictures, Descriptions, etc)
- Property Title
- Marketing Company

## Data Cleaning
 After scrapping the Data, I needed to clean the scrapped data, in readiness for our model. In this process i made the following changes and created the following variables:
 
 - Parsed Numeric data out of House price
 - Made columns for Number of bedrooms, Toilets and Bathrooms
 - Made a column for location, after parsing out actual location of property
 
## EDA
I looked at the distibutions 
