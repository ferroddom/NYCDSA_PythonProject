#!/usr/bin/env python
# coding: utf-8

# ## Import packages and setup display options

# In[1]:


import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 100)


# In[2]:


import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(15,12)})


# ## Import business data from Yelp Academic Dataset

# In[3]:


business_data = pd.read_csv('yelp_academic_dataset_business.csv')
business_data.head()


# ### Clean business data

# Check for columns that have missing values and drop those that ONLY have them

# In[4]:


sns.heatmap(business_data.isnull(), cbar = False)


# In[5]:


business_data.dropna(axis = 'columns', how = 'all', inplace = True)
business_data.shape


# Chang the format of column names

# In[6]:


business_data.columns = business_data.columns.str.replace('.', '_').str.lower()
business_data.columns


# Drop not needed columns

# In[7]:


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


# Remove hours columns

# In[8]:


business_data.drop(columns = ['hours_friday', 'hours_monday', 'hours_saturday', 'hours_sunday', 'hours_thursday', 'hours_tuesday', 'hours_wednesday'], inplace = True)
business_data.info()


# ### Load home prices index data (median list price all homes zillow)

# In[9]:


home_prices = pd.read_csv("Metro_mlp_uc_sfrcondo_sm_month.csv")
home_prices.head()


# Select list price index from February 2022

# In[11]:


home_prices.drop(index=home_prices.index[0], axis=0, inplace=True)
home_prices = home_prices[['RegionName', 'StateName', '2021-02-28']]


# Take City from RegionName

# In[12]:


home_prices['city'] = home_prices['RegionName'].str.split(',', expand=True).drop(1, axis=1)
home_prices.drop(['RegionName'], axis=1, inplace=True)
home_prices.rename(columns={'2021-02-28': 'list_price'}, inplace=True)
home_prices.head()


# Create buckets of list price range for the cities in the analysis

# In[13]:


home_prices['list_price_range'] = pd.qcut(home_prices['list_price'], q=5, labels=['low', 'mid_low', 'mid', 'mid_high', 'high'])
home_prices.head()


# In[14]:


home_prices['city'].nunique()


# In[15]:


home_prices['StateName'].nunique()


# Subset to only States

# In[17]:


us_data = pd.read_csv('territory_abbr.csv')


# In[18]:


us_data.columns = us_data.columns.str.lower()
us_data.rename(columns = {'state': 'longform', 'abbreviation': 'state'}, inplace = True)
us_data.head()


# In[19]:


business_data = business_data.merge(us_data, how = 'inner', on = 'state')
business_data['state'].nunique()


# ### Merge business data with home price data

# In[20]:


business_data = business_data.merge(home_prices, how='inner', on='city')


# Rank cities by list price

# In[21]:


business_data['list_price'].isna().sum()


# In[22]:


business_data = business_data[business_data['list_price'].notna()]


# In[26]:


business_data.sort_values(by='list_price', ascending = False).head()


# ### Use only food establishments

# In[27]:


food_establishments = business_data.copy()
food_establishments['categories'] = food_establishments['categories'].str.lower()
filt_food = food_establishments['categories'].str.contains(pat = r'dining|restaurant', regex = True) == True
food_establishments = food_establishments.loc[filt_food]
food_establishments['categories'].count()


# In[28]:


food_establishments.head()


# # Data Analysis

# ## Are higher rated restaurants the most reviewd?

# In[30]:


fig, ax = plt.subplots(figsize = (10,10))
ax.set_yscale('log')

sns.boxplot(data = food_establishments, x = 'stars', y = 'review_count', notch = True)
fig.suptitle('Relationship between Stars and No. of Reviews', fontsize = 25)
ax.set_ylabel('Number of reviews')


# ## Do food establishments in cities with higher listing prices have higher ratings?

# In[33]:


food_establishments.groupby(by=['list_price_range'])['stars'].agg(['count', 'mean', 'median', 'std']).round(2)


# ## Is Mexican food better rated in border states than the rest of the US?

# In[34]:


filt_mexican = food_establishments['categories'].str.contains(pat = r'mexican', regex = True) == True
mexican_establishments = food_establishments.loc[filt_mexican]


# In[35]:


len(mexican_establishments)


# In[36]:


border_state = ['CA', 'AZ', 'NM', 'TX']
mexican_establishments['border'] = np.where(mexican_establishments['state'].isin(border_state) , 1, 0)
mexican_establishments.sample(5)


# In[37]:


mexican_establishments['border'].value_counts()


# In[38]:


fig, ax = plt.subplots(figsize = (10,10))
ax.set_yscale('log')

sns.boxplot(data = mexican_establishments, x = 'border', y = 'review_count')
fig.suptitle('Relationship between Review Count and Border State', fontsize = 25)
ax.set_ylabel('Number of reviews')


# In[39]:


mexican_establishments.groupby(by=['border'])['stars'].agg(['count', 'mean', 'median', 'std']).round(2)


# ## Load Review data from teh Yelp Academic Dataset

# In[40]:


review_data = pd.read_csv('yelp_academic_dataset_review.csv')
review_data.head()


# In[41]:


len(review_data)


# Subset to only food establishments

# In[42]:


review_data = review_data.merge(food_establishments, on = 'business_id', how = 'inner')
len(review_data)


# In[43]:


review_data = review_data.merge(food_establishments, on = 'business_id', how = 'inner')
filt_review = review_data.groupby(['business_id']).agg({'review_id': 'count'})
food_review = food_establishments.merge(filt_review, on = 'business_id', how = 'inner')
food_review = food_review[['business_id', 'review_count', 'review_id']]
food_review.rename(columns = {'business_id': 'business_id', 'review_count': 'review_count', 'review_id': 'number_reviews'}, inplace = True)
food_review.tail()


# Text based analysis

# In[ ]:


excl = review_data['text'].str.extract(pat = r'(!+)')
excl.head()


# In[ ]:


p21 = pd.concat([review_data, excl], axis = 'columns')
p21.head()


# In[ ]:


p21 = p21[['stars', 0]]
p21


# In[ ]:


p21['exclamations'] = p21[0].str.len()
p21['exclamations'] = p21['exclamations'].fillna(0)
#p21['has_excl'] = 'No' if p21['exclamations'] == 0 else 'Yes'
p21


# In[ ]:


p21.sort_values(by='exclamations', ascending = False)


# In[ ]:


p21['has_excl'] = [False if n == 0 else True for n in p21['exclamations']]
p21.head()


# In[ ]:


p21['exclamations'].value_counts().head()


# In[ ]:


p21.groupby('has_excl').agg({'stars': ['mean', 'std']})


# In[ ]:


p21.plot(kind = 'scatter', x = 'stars', y = 'exclamations', figsize = (8,5))


# In[ ]:


p21_b = p21.groupby('stars').agg({'exclamations': ['mean', 'std']})
p21_b.dropna(inplace = True)
p21_b


# In[ ]:


p21_b = p21_b.reset_index()
p21_b.plot(kind = 'scatter', x = 'stars', y = [('exclamations', 'mean')], figsize = (8,5))


# In[ ]:




