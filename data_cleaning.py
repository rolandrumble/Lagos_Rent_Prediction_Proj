# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 09:10:32 2020

@author: 60004501
"""
import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/60004501/property_list_2.csv')

#Checking for Null values in the DataFrame

df.isnull().sum().any()

#Cleaning up the pricing column (Removing '₦' and ,)

price = df['property_price'].apply(lambda x:x.replace('₦',''))
price_1 = price.apply(lambda x:x.replace(',',''))
print(price_1.unique())
# Observed we have some price that estimated in $, Hence the need to convert to equivalent Naira value

#-- Writing a Function that loops through the Pricing column, strips the dollar sign and multiply value ($) with naira equivalent of ₦365 to $1
def num_convert(x):
    if x.startswith("$"):
        return x.replace('$','')
        x.strip()
        x.astype(int)
        x*365
    return x.strip()

# Applying function to price column
    
price_2 = price_1.apply(num_convert)
price_2 = price_2.astype(str).astype('int64')

#assign newly converted price to price DataFrame
df['price'] = price_2
print(df.head)

####### Cleaning the Number of Bedrooms columns###########

num_bedrooms = df['property_features'].apply(lambda x:x.lower().split('bed')[0]) 
num_bedrooms = num_bedrooms.replace(r'^\s*$',str(0), regex=True)
num_bedrooms  = num_bedrooms.apply(lambda x:x.strip())
num_bedrooms = num_bedrooms.astype(str).astype(int)

#Appending Num_bedrooms to dataframe
df['num_bedrooms'] = num_bedrooms

####### Cleaning to the Number of bath_rooms columns###########
bath_rooms= df['property_features'].apply(lambda x:x.lower().split('bath')[0])
bath_rooms = bath_rooms.apply(lambda x:x.lower().split('bed')[0])
bath_rooms = bath_rooms.replace(r'^\s*$',np.nan, regex=True)
print(bath_rooms)

#Appending Num_bathrooms to dataframe
df['num_bathrooms'] = bath_rooms

####### Cleaning to the Number of toilet columns###########
num_toilet = df['property_features'].apply(lambda x:x.lower().split('bath')[1])
num_toilet = num_toilet.apply(lambda x:x.lower().split('toilet')[0])
num_toilet = num_toilet.replace(r'^\s*$',np.nan, regex=True)
num_toilet

#Appending Num_bathrooms to dataframe
df['num_toilet'] = num_toilet

#Observation from the num_bathrooms, we see most apartment with 0 or 1 num_bathrooms have NAN values
#Hence for the purpose of this Project we would fill the NAN values with 1

#Filling Null number of bathrooms with 1
df['num_bathrooms'].fillna(1, inplace = True )

#Filling Null number of toilets with number of bedrooms (assuming a bedroom should have a toilet)
df['num_toilet'].fillna(df['num_bedrooms'], inplace = True)

##### Parsing our location column and extracting key location within Lagos #########
location = df['property_location'].apply(lambda x:x.lower().split(' ')[0:2])
S =  [','.join(i) for i in location]
df['location'] =  S
df['location'] = df['location'].apply(lambda x:x.replace(',',' ').replace('-','').strip())
df['location'].value_counts().head(20)

#### Parsing Our Property
property_type = df['property_title'].apply(lambda x:x.split('/')[0])
df['property_type'] = property_type.apply(lambda x:x if "bedroom" in x.lower() or 'flat' in x.lower() else 0)








