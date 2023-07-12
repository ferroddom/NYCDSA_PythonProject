#!/usr/bin/env python
# coding: utf-8

# In this Python project I will use the Yelp Academic Dataset (Business dataset and Reviews dataset) in conjunction with a dataset from Zillow (median list price for homes) in order to answer different questions regarding how food establishments are reviewed.

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


# In[3]:


import scipy.stats as stats


# ## Import business data from Yelp Academic Dataset

# In[4]:


business_data = pd.read_csv('yelp_academic_dataset_business.csv')
business_data.head()


# ### Clean business data

# Check for columns that have missing values and drop those that ONLY have them

# In[5]:


sns.heatmap(business_data.isnull(), cbar = False)


# In[6]:


business_data.dropna(axis = 'columns', how = 'all', inplace = True)
business_data.shape


# Chang the format of column names

# In[7]:


business_data.columns = business_data.columns.str.replace('.', '_').str.lower()
business_data.columns


# Drop not needed columns

# In[8]:


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

# In[9]:


business_data.drop(columns = ['hours_friday', 'hours_monday', 'hours_saturday', 'hours_sunday', 'hours_thursday', 'hours_tuesday', 'hours_wednesday'], inplace = True)
business_data.info()


# ### Load home prices index data (median list price all homes zillow)

# In[10]:


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


# Subset yelp dataset to use to only States (no territories or places in canada)

# In[16]:


us_data = pd.read_csv('territory_abbr.csv')


# In[17]:


us_data.columns = us_data.columns.str.lower()
us_data.rename(columns = {'state': 'longform', 'abbreviation': 'state'}, inplace = True)
us_data.head()


# In[18]:


business_data = business_data.merge(us_data, how = 'inner', on = 'state')
business_data['state'].nunique()


# ### Merge business data with home price data

# In[19]:


business_data = business_data.merge(home_prices, how='inner', on='city')


# Rank cities by list price

# In[20]:


business_data['list_price'].isna().sum()


# In[21]:


business_data = business_data[business_data['list_price'].notna()]


# In[22]:


business_data.sort_values(by='list_price', ascending = False).head()


# ### Use only food establishments

# In[ ]:





# In[23]:


food_establishments = business_data.copy()
food_establishments['categories'] = food_establishments['categories'].str.lower()
filt_food = food_establishments['categories'].str.contains(pat = r'dining|restaurant|fast food|food stands', regex = True) == True
food_establishments = food_establishments.loc[filt_food]
food_establishments['categories'].count()


# In[24]:


food_establishments.head()


# # Data Analysis

# ## Are higher rated restaurants the most reviewd?

# In[25]:


fig, ax = plt.subplots(figsize = (10,10))
ax.set_yscale('log')

sns.boxplot(data = food_establishments, x = 'stars', y = 'review_count', notch = True)
fig.suptitle('Relationship between Stars and No. of Reviews', fontsize = 25)
ax.set_ylabel('Number of reviews')


# ## Do food establishments in cities with higher listing prices have higher ratings?

# In[26]:


food_establishments.groupby(by=['list_price_range'])['stars'].agg(['count', 'mean', 'median', 'std']).round(2)


# ## Is Mexican food better rated in border states than the rest of the US?

# In[27]:


filt_mexican = food_establishments['categories'].str.contains(pat = r'mexican', regex = True) == True
mexican_establishments = food_establishments.loc[filt_mexican]


# In[28]:


len(mexican_establishments)


# In[29]:


border_state = ['CA', 'AZ', 'NM', 'TX']
mexican_establishments['border'] = np.where(mexican_establishments['state'].isin(border_state) , 1, 0)
mexican_establishments.sample(5)


# In[30]:


mexican_establishments['border'].value_counts()


# In[31]:


mexican_establishments.groupby(by=['border'])['stars'].agg(['count', 'mean', 'median', 'std']).round(2)


# ### Are mexican restaurants better rated in high list price cities or not?

# In[32]:


mexican_establishments.groupby(by='list_price_range')['stars'].agg(['count', 'mean', 'median', 'std']).round(2)


# ## Load Review data from the Yelp Academic Dataset

# In[33]:


review_data = pd.read_csv('yelp_academic_dataset_review.csv')
review_data.head()


# In[34]:


len(review_data)


# Subset to only mexican food establishments

# In[35]:


review_data = review_data.merge(mexican_establishments, on = 'business_id', how = 'inner')
len(review_data)


# In[36]:


review_data = review_data.merge(food_establishments, on = 'business_id', how = 'inner')
filt_review = review_data.groupby(['business_id']).agg({'review_id': 'count'})
food_review = food_establishments.merge(filt_review, on = 'business_id', how = 'inner')
food_review = food_review[['business_id', 'review_count', 'review_id']]
food_review.rename(columns = {'business_id': 'business_id', 'review_count': 'review_count', 'review_id': 'number_reviews'}, inplace = True)
food_review.tail()


# ### Text based analysis

# Are spicy,picante, caliente mexican restaurants better ranked?

# We first check if the restaurants reviews either have a synonym word for spicyness or not.

# In[37]:


palabra = review_data['text'].str.extract(pat = r'(spice|spicy|picante|fuego|caliente)')
palabra.head()


# Now we count the times those words are used in each review

# In[38]:


cuenta = review_data['text'].str.count(pat = r'(spice|spicy|picante|fuego|caliente)')


# In[39]:


cuenta = cuenta.to_frame()
cuenta.rename(columns={'text': 'count'}, inplace = True)
cuenta.head()


# In[41]:


picante = pd.concat([review_data, palabra, cuenta], axis = 'columns')
picante.head(3)


# As an example we will use review 16639

# In[44]:


picante.iloc[16639, -1]


# It has one of the picante words two times

# In[42]:


picante.iloc[16639].text


# It is correct, it uses picante and spicy.

# In[45]:


picante = picante[['stars', 0, 'count']]


# In[49]:


picante['picante'] = picante[0].str.len()
picante['picante'] = picante['picante'].fillna(0)
picante['has_picante'] = [False if n == 0 else True for n in picante['picante']]
picante.head()


# In[50]:


picante.sort_values(by='count', ascending = False)


# First we compare the results between the stars given to restaurants in which the review has one (or more) picante word and those that don't

# In[52]:


picante.groupby('has_picante').agg({'stars': ['mean', 'std', 'count']}).round(2)


# Now we runa ttest to see if the means are statistically the same or not

# In[57]:


has = picante[picante['has_picante'] == True].stars
doesnt = picante[picante['has_picante'] == False].stars


# In[58]:


stats.ttest_ind(has, doesnt, equal_var = False)


# We see that even though the difference is only 0.16 Stars. Because of the amount of reviews given we can say that they are not statistically the same. Mexican food establishments that are reviewed with at least one PICANTE word are rated higher than those that are not.

# But what is the sweet spot? A little mexican spiciness can be good, but to much perhaps isnt ideal for american palates. Now we use the count of those words to check for this.

# In[59]:


picante_agg = picante.groupby('count').agg(mean = ('stars', 'mean'), std = ('stars', 'std'), obs = ('stars', 'count')).round(2)
picante_agg


# In[62]:


picante_line = picante.groupby('count')['stars'].mean().round(2).reset_index()
plt.plot(picante_line['count'], picante_line['stars'], color = 'red', linewidth = 10)
plt.xlabel('Times picante word was used')
plt.ylabel('Stars')


# It appears that the highest rated restaurants were reviewed with these key words between 4 and 6 times. Too little spiciness or too much appear to be correlated with less stars given to a restaurant.

# In conclusion, add some PICANTE to your mexican food, but not too much.
