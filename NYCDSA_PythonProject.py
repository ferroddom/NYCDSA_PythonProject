#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 100)


# In[ ]:


import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(15,12)})


# In[ ]:


business_data = pd.read_csv('yelp_academic_dataset_business.csv')
business_data.head()


# In[ ]:


review_data = pd.read_csv('yelp_academic_dataset_review.csv')
review_data.head()


# In[ ]:


review_data.dtypes


# In[ ]:


user_data = pd.read_csv('yelp_academic_dataset_user.csv')
user_data.head()


# Clean business data

# Check for columns that have missing values and drop those that ONLY have them

# In[ ]:


sns.heatmap(business_data.isnull(), cbar = False)


# In[ ]:


business_data.dropna(axis = 'columns', how = 'all', inplace = True)
business_data.shape


# Chang the format of column names

# In[ ]:


business_data.columns = business_data.columns.str.replace('.', '_').str.lower()
business_data.columns


# Drop not needed columns

# In[ ]:


business_data.drop(columns = ['attributes_acceptsinsurance', 'attributes_agesallowed', 'attributes_alcohol',
       'attributes_ambience', 'attributes_byob', 'attributes_byobcorkage', 'attributes_bestnights',
       'attributes_bikeparking', 'attributes_businessacceptsbitcoin',
       'attributes_businessacceptscreditcards', 'attributes_businessparking',
       'attributes_byappointmentonly', 'attributes_caters', 'attributes_coatcheck',
       'attributes_corkage', 'attributes_dietaryrestrictions', 'attributes_dogsallowed',
       'attributes_drivethru', 'attributes_goodfordancing', 'attributes_goodforkids',
       'attributes_goodformeal', 'attributes_hairspecializesin',
       'attributes_hastv', 'attributes_music', 'attributes_noiselevel', 'attributes_open24hours',
       'attributes_outdoorseating', 'attributes_restaurantsattire',
       'attributes_restaurantscounterservice', 'attributes_restaurantsdelivery',
       'attributes_restaurantsgoodforgroups', 'attributes_restaurantspricerange2',
       'attributes_restaurantsreservations', 'attributes_restaurantstableservice',
       'attributes_restaurantstakeout', 'attributes_smoking', 'attributes_wheelchairaccessible',
       'attributes_wifi'], inplace = True)
business_data.info()


# Create open on weekends clumns

# In[ ]:


business_data['open_on_weekends'] = np.where((business_data['hours_saturday'].notnull() == True) | (business_data['hours_sunday'].notnull == True), 1, 0)
business_data.head(5)


# Remove hours columns

# In[ ]:


business_data.drop(columns = ['hours_friday', 'hours_monday', 'hours_saturday', 'hours_sunday', 'hours_thursday', 'hours_tuesday', 'hours_wednesday'], inplace = True)
business_data.info()


# Load home prices index data

# In[ ]:


home_prices = pd.read_csv("Metro_mlp_uc_sfrcondo_sm_month.csv")
home_prices.head()


# In[ ]:


home_prices.drop(index=home_prices.index[0], axis=0, inplace=True)
home_prices = home_prices[['RegionName', 'StateName', '2021-02-28']]


# Take City from RegionName

# In[ ]:


home_prices['city'] = home_prices['RegionName'].str.split(',', expand=True).drop(1, axis=1)
home_prices.drop(['RegionName'], axis=1, inplace=True)
home_prices.rename(columns={'2021-02-28': 'list_price'}, inplace=True)
home_prices.head()


# In[ ]:


home_prices['list_price_range'] = pd.qcut(home_prices['list_price'], q=4, labels=['low', 'mid_low', 'mid_high', 'high'])
home_prices.head()


# Merge price index with business data on city

# In[ ]:


business_data = business_data.merge(home_prices, how='inner', on='city')


# Use only food establishments

# In[ ]:


food_establishments = business_data.copy()
food_establishments['categories'] = food_establishments['categories'].str.lower()
filt_food = food_establishments['categories'].str.contains(pat = r'dining|restaurant', regex = True) == True
food_establishments = food_establishments.loc[filt_food]
food_establishments['categories'].count()


# In[ ]:


food_establishments.head()


# Do food_establishments in cities with higher listing prices have more reviews?

# In[ ]:


fig, ax = plt.subplots(figsize = (10,10))
ax.set_yscale('log')

sns.boxplot(data = food_establishments, x = 'list_price_range', y = 'review_count', notch = True)
fig.suptitle('Relationship between Review Count and List Price', fontsize = 25)
ax.set_ylabel('Number of reviews')


# Do food establishments in cities with higher listing prices have higher ratings?

# In[ ]:


food_establishments.groupby(by=['list_price_range'])['stars'].agg(['count', 'mean', 'median', 'std']).round(2)


# Check if in deciles it changes anything

# Scatterplot of list price and star
