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
I looked at the distibutione and value counts for various categorical variables within the locations columns. Below are visual highlights:

<img src="https://github.com/rolandrumble/Lagos_Rent_Prediction_Proj/blob/Images/Correlation_plot.png" width="256" height="256" title="correlation_plot"> 

## Model Building
 First, I transformed the categorical variables (location column) into dummy variables. I splitted the data into a train and test sets wih a test size of 20%
 I progressed by trying different models and evaluated them using Mean Absolute Error (MSE). I Choose MAE beacuse it is relatively easy to interpret and outliers are not particularly bad for this type of model.
 
 I tried Three Different Models:
  - Linear Regression - Baseline for the model
  - Lasso Regression - Due to the sparse data from many categorical varibles in the **Location** column
  - Decision Trees - Was a very good fit due to the sparsity of the data
 
## Productinization
 In this step, I built a Flask API end point that was hosted on my local webserver by following along with the **CODEBASICS** tutorials in the refrence section above. The API end ppoint takes in a request with a list (Number of Bedrooms, Number of Bathrooms, and Number of Toilets) which returns an Estimated House rent Price
