Python Pandas Tutorial by Corey Schafer
Part 1

pip install pandas

pip install jupyterlab

navigate to your directory with the folder containing the data that you want to analyze, then

jupyter notebook: fires up a jupyter tab

then you want to create a new python3 notebook. once done, you will see the folder containing the data you want to analyze

import pandas as pd

df = pd.read_csv('data/survey_results_public.csv')

df: prints out the data frame, note that you don't need the print function in jupyter, if table too big, concatenated, dimensions are shown at the bottom left

df.shape: not a method, no parentheses needed, gives dimension

* if there's any spacing issue, go to the Kernel tab and click, restart and run all, apparently it resets the In numbers too

df.info(): it's a method hence the parentheses, gives some info like data types, but view is kinda scuffed, can't see all the columns

pd.set_option('display.max_columns', 85): now you can view all 85 columns, just need to scroll 

schema_df = pd.read_csv('data/survey_results_schema.csv')

pd.set_option('display.max_rows', 85): increases max number of rows displayed to 85

df.head(): views first 5 rows of data, unless you pass a value into it
df.tail(): views last 5 rows of data, unless you pass a value into it

Part 2
DataFrame and Series Basics - Selecting Rows and Columns
use of dictionaries, keys as columns, and values as rows
to access dictionary containing lists as values,
people['email']

import pandas as pd: enables you to create data frame using dictionaries

df = pd.DataFrame(people): in this case 'people' is the name of the dictionary

df: you can see that it prints out the dictionary in the form of a data frame

how to access values of a single column?
df['email']: gives you all the emails 

data frame is much much more than a dictionary of lists

type(df['email']): gives you "pandas.core.series.Series", Series is a list of data, but a lot more functionality. definition: one-dimensional data, which means rows of data!

use of dot notation is possible:
df.email: gives you the same result!

brackets preferred, because 
- a chance one of your columns is names the same as one of your attributes/methods. if the same, it will access the method instead of column!

how to access multiple columns? use a list
df[['last', 'email']]: gives you both last name and email

you can grab columns only!
df.columns: gives you all the columns

how about grabbing rows?
use iloc and loc, ilo means integer location
df.iloc[0]: gives us first row, notice that it sets index to colum names

we can select multiple rows as well! say you want first and second rows
df.iloc[[0,1]]: notice that you get a data frame with multiple rows

df.iloc[[0,1], 2]: you'll get email addresses of the first 2 rows, row and column taken into account

what about loc? search by label, not integer location
df.loc[0]: looks similar to iloc as of now

df.loc[[0,1]]: gives you first and second row, also get data frame

df.loc[[0,1], 'email']: gives you first 2 rows of the email column! notice use of 'email'

df.loc[[0,1], ['email', 'last']]: get first two rows of the "email" and "last" columns, notice how the columns are arranged according to what you specify first, email then last


Now let's mess around with df
df['Hobbyist']: selects the column

df['Hobbyist'].value_counts(): gives tally of Yes and No! 

now let's grab first two rows of the Hobbyist column
df.loc[0]: gives you all the data in first row

just for Hobbyist?
df.loc[0, 'Hobbyist']: just the response for that row and column

remember, row first then column

df.loc[[0,1,2], 'Hobbyist']: gives you first three rows for Hobbyist column

you can slice too!
df.loc[0:2, 'Hobbyist']: much cleaner! same results

df.loc[0:2, 'Hobbyist':'Employment']: you can slice column names too! not just index, cuz it's by label

we'll learn more about advanced filtering, queries, data types


Part 3
Indexes - How to Set, Reset, and Use Indexes

pandas doesn't enfore indexes to be unique
what might be a better index? emails, cuz it's usually unique

df.set_index('email'): "sets" index as emails, but index is not actually changed, nice so we can experiment first before setting them as index for real

to change it for real:
df.set_index('mail', inplace=True)

df.index: gives you the index of the data frame

df.loc['CoreyMSchafer@gmail.com']: gives you the row for that email

df.loc['CoreyMSchafer@gmail.com', 'last']: gives you just the "last" column for Corey's email

if you wanna reset the index:
df.reset_index(inplace=True): inplace=True so changes carry over, default range index will be in place.

df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent'): sets respondent as index when reading the csv file!

say if you want the first respondent
df.loc[1]: gives you first row

schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column'): sets Column as the index for the schema df as it's being read

schema_df.loc['Hobbyist']

schema_df.loc['MgrIdiot']: notice that the QuestionText is truncated, if you wanna see the FULL TEXT, pass in the column too, basically you just want to get one cell?

schema_df.loc['MgrIdiot', 'QuestionText']

now we wanna sort the index! makes searching easier
schema_df.sort_index(): sorts the index alphabetically!

schema_df.sort_index(ascending=False): to sort in descending order

*remember the result of the sort_index is not permanent until you have specified "inplace=True"

schema_df.sort_index(inplace=True)

now, schema_df is permanent sorted in ascending order!


Part 4
Filtering - Using Conditionals to Filter Rows and Columns

say you want everyone with the last name Doe
df['last'] == 'Doe': what you get is a series object, T F values, hence not this way

filt = (df['last'] == 'Doe')
df[filt]: returns the data frame back of people whose last name is Doe

df.loc[filt]: you will get the exact same thing

df.loc[filt, 'email']: narrows down to just the 'email' column

use & and | (or)

say you want first name John AND last name Doe
filt = (df['last'] == 'Doe') & (df['first'] == 'John')
df.loc[filt, 'email']

add TILDA in the beginning of the filter, it'll negate the filter and gives you the opposite of the results!
df.loc[~filt, 'email']

create a filter called high_salary
high_salary = (df['ConvertedComp'] > 7000)
df.loc[high_salary]

how to filter by columns?
too many columns though, narrow them down to just Country, LanguageWorkedWith and ConvertedComp, using a LIST
df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]

now narrow them down by only wanting specific rows of 'Country' column
first make a list called countries for countries you're interested in:
countries = ['United States', 'India', 'United Kingdom', 'Germany', 'Canada']
filt = df['Country'].isin(countries): column is in the list you made
df.loc[filt, 'Country']: filters the data using filt on 'Country' column

now we want to filter for people who has worked with Python
df['LanguageWorkedWith']: gives you that column, realize that there are many possible languages per row

filt = df['LanguageWorkedWith'].str.contains('Python', na=False): str.contains means, the string contains
df.loc[filt, 'LanguageWorkedWith']: gives you the result you want!

key takeaways, can do conditionals and assign them to a variable and then apply the variable as filters using .loc


Part 5: Updating Rows and Columns - Modifying Data Within DataFrames
learn to update columns first, then rows

snippet part

to rename columns
df.columns = ['first_name', 'last_name', 'email']

say you wanna uppercase all the column names:
df.columns = [x.upper() for x in df.columns]

if you wanna replace spaces with underscores
df.columns = df.columns.str.replace(' ', '_')

if you wanna set the first_name or last_name back to original names, or any names you want to. notice you pass in dictionaries
df.rename(columns={'first_name': 'first', 'last_name': 'last}')
but changes aren't permanent until
df.rename(columns={'first_name': 'first', 'last_name': 'last}', inplace = True)

.rename() needs "inplace = True" to confirm changes

# to grab third row
df.loc[2]

# to change all the values in the row
df.loc[2] = ['John', 'Smith', 'JohnSmith@email.com']

# to just change the last name and email?
df.loc[2, ['last', 'email']] = ['Doe', 'JohnDoe@email.com']

# to just change one value
df.loc[2, 'last'] = 'Smith'

df.at[2, 'last'] = 'Smith' # does the same thing lol

one common mistake, people try to change values without using .loc or .at

filt = (df['email'] == 'JohnDoe@email.com')
df[filt] # returns a data frame 
# now grab single column from the data frame obtained
df[filt]['last'] 
# BUT you can't change a value by doing
df[filt]['last'] = 'Smith' # doesn't work

# remember, when setting values you gotta use .loc and .at
# this one will work:
df.loc[filt, 'last'] = 'Smith'

# how do we update multiple rows of data?
# say change all the email address to lower case

df['email'].str.lower() # change does not go through
# gotta do
df['email'] = df['email'].str.lower()

4 methods to change multiple values 
df['email'].apply(len) #grabs length of values, in that case length of each row in email column

def update_email(email):
	return email.upper() #usually to apply advanced updates

df['email'].apply(update_email) #finalizes the changes

# for 1 line code to do the same shit
df['email'] = df['email'].apply(lambda x: x.lower()) 

# so we've seen how apply works on a series
# now data frame time

df.apply(len) #gives you length of columns, not that of values in columns combined!

len(df['email'])

df.apply(pd.Series.min)
df.apply(lambda x: x.min())

running apply on a series: applies the function to every value in the series
running apply on a df: applies the function to every series in the df

applymap works on df nicely
df.applymap(len): now applying the length function to each value in the df

to apply lowercase on every value in the df
df.applymap(str.lower): if there's a number within the values, this won't work, error caused!

df['first'].map{'Corey': 'Chris', 'Jane': 'Mary'} # but this causes values not mentioned will be NaN

so you wanna do this!
df['first'].replace({'Corey': 'Chris', 'Jane': 'Mary'}) # remember, this ain't permanent!
so you gotta assign this whole code to df['first']

df['first'] = df['first'].replace({'Corey': 'Chris', 'Jane': 'Mary'})  # the change will then be transferred

remember when we use map, anything that is not in dictionary will be converted to NaN value!!
# use replace instead of map if you wanna leave other values untouched (if you don't want NaN, or if you don't know ALL the values of the column)


Part 6
Add/Remove Rows and Columns from DataFrames

# say you wanna combine the first and last column
df['first'] + ' ' + df['last']
df['full_name'] = df['first'] + ' ' + df['last']

# now you see that the df has full_name column with the expected values

# now let's look at removing columns
df.drop(columns=['first', 'last']) 
#notice we pass in a list whenever it's more than one item to
# make change permanent,
df.drop(columns=['first', 'last'], inplace=True)

df['full_name'].str.split(' ', expand=True)
# split split by spaces by default
# expand = True divides them into columns

df[['first', 'last']] = df['full_name'].str.split(' ', expand=True)

# how would you add a single row of data?
df.append({'first': 'Tony'}, ignore_index=True)

df.append(df2, ignore_index=True, sort=False) #sort=False, so columns are not sorted

df.drop(index=4)

df.drop(index=df[df['last'] == 'Doe'].index) # not that readable
# so pull conditional out as its own variable
filt = df['last'] == 'Doe'
df.drop(index=df[filt].index) # cleaner


# Part 7
# Sorting Data
# Snippets Part

# to sort 'last' column alphabetically
df.sort_values(by='last')

# for descending order
df.sort_values(by='last', ascending=False)

# sort on the last name first, and then first name, in the same order
df.sort_values(by='last', 'first', ascending=False)

# sort on last name first, then first name, but in two different orders
# respectively
df.sort_values(by='last', 'first', ascending=[False, True])

# to make changes permanent, 
df.sort_values(by='last', 'first', ascending=[False, True], 
	inplace = True)

df.sort_index() # sorts based on index

df['last'].sort_values() # sorts 'last' column 

df.sort_values(by='Country', inplace=True)
df['Country'].head(50) # see top 50 results of 'Country' column

df[['Country', 'ConvertedComp']].head(50)
df.sort_values(by='Country', 'ConvertedComp', 
	ascending=[True, False] inplace=True) 
# ascending sort for country and descending for salary

# see ten highest salaries for our survey
df['ConvertedComp'].nlargest(10) # just gives one column, other 
# columns missing

df.nlargest(10, 'ConvertedComp') #but this gives all columns based
# on the 10 highest salaries

df.nsmallest(10, 'ConvertedComp')


# Part 8
# Grouping and Aggregating - Analyzing and Exploring Your Data
# aggregation: combining multiple pieces of data into a single result
# e.g. mean, median

# what's a typical salary for developers taking the survey?
# check out ConvertedComp (salary) column
df['ConvertedComp'].head(15)

# to get median salary
df['ConvertedComp'].median()

# we can break down median salary by country

# grab median values of columns containing numerical values
df.median(): 

# to get statistical details, use describe method
df.describe() #gives stuff like mean, sd

# remember, mean is heavily affected by outliers
# count row is the number of NaN in a row

df['ConvertedComp'].count() 
# gets number of people who didn't answer the salary question
# basically NaN tally 

# now let's see how many peopl answer yes and no for hobbyist
# column
df['Hobbyist'].value_counts()

df['SocialMedia']

schema_df.loc['SocialMedia']

df['SocialMedia'].value_counts()

# you can normalize the tally!
df['SocialMedia'].value_counts(normalize=True)

# now break down popular social media sites by country
# steps: SPLIT, APPLY FUNCTION, COMBINE RESULTS!

df['Country'].value_counts()

# to group by country
country_grp = df.groupby(['Country'])
country_grp.get_group('United States')

filt = df['Country'] == 'United States'
df.loc[filt] # gives you the same result but

# groupby splits the data by country names!
df.loc[filt]['SocialMedia'].value_counts()
# results for United States only, how to get for all countries?

#groupby function helps you to get the data for all countris
country_grp['SocialMedia'].value_counts().head(50)
# returns a series, has multiple indexes (know how it works)
# in this case, country is the first index
# social media is the second index

country_grp['SocialMedia'].value_counts(normalize=True).loc['India']
# to grab just the data for India
# normalize=True gives you percentage if it makes more sense
# to you
# useful because then you just have to change the country name
# instead of changing the filter again and again

country_grp['ConvertedComp'].median()
# to see median salary for all the countries

#say you just want Germany, notice that index is country name
country_grp['ConvertedComp'].median().loc['Germany']

# to pass in more than one aggregate function
country_grp['ConvertedComp'].agg(['median', 'mean'])

# say if you wanna figure out how many people in each country
# uses Python

filt = df['Country'] == 'India'
df.loc[filt]
# let's use string methods
df.loc[filt]['LanguageWorkedWith'].str.contains('Python') 
# str.contains() returns true or false
# to actually count them, use sum()
# sum() also works on boolean!

df.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum()
# returns number of Trues i.e. number of respondents who use
# Python

country_grp['LanguageWorkedWith'].str.contains('Python').sum()
#returns error! because country_grp isn't just a series
# so we need the apply method

# note that lambda is gonna be a series
country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())

# THE BIG QUESTION
# how to figure out what % of people from each country know Python?

# first, find the total number of respondents from each country
country_respondents = df['Country'].value_counts()
country_respondents

country_uses_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
country_uses_python

# we can combine more than one series together using the pandas
# concat function
python_df = pd.concat([country_respondents, country_uses_python],
	axis = 'columns', sort=False)
# axis = 'columns' to concat by columns, default is rows
# sort=False needed

# now update the column names
python_df.rename(columns={'Country': 'NumRespondents', 
	'LanguageWorkedWith': 'NumKnowsPython'}, inplace=True)

#in order to create a new column, just assign it
python_df['PctKnowsPython'] = (python_df['NumKnowsPython']/python_df['NumRespondents'] * 100)

# to sort country based on largest percentage that know Python
python_df.sort_values(by='PctKnowsPython', ascending=False, inplace=True)

# to have an idea how how many respondents there are per country
python_df.head(50)
# basically, those with more respondents display more reliable data

# say you just wanna see Japan's statistics
python_df.loc['Japan']


# Part 9
# Cleaning Data - Casting Datatypes and Handling Missing Values

# first let's learn how to drop missing values
# snippets time
# notice that numpy has been imported as np

# to drop NA values
df.dropna()

df.dropna(axis='index', how='any') #default arguments
# axis can be set to either index or column (index means rows here)
# how: criteria it uses for dropping a row or column
# change any to all, drop rows when all the values are missing

df.dropna(axis='index', how='all')

# you can pass in a subset argument, in this case specifying
# the email column
df.dropna(axis='index', how='any', subset=['email'])

# either last name or email address, but don't need both
df.dropna(axis='index', how='all', subset=['last', 'email'])

# remember, need to add inplace argument to make the change permanent

# now let's deal with the custom missing values
# string of NA, string of Missing

# replace the values with proper numpy NaN value

df.replace('NA', np.nan, inplace=True)
# this replaces NA strings with NaN
df.replace('Missing', np.nan, inplace=True)

df.isna() #gives results on whether the values classify as NA values

df.fillna('MISSING')
# fills all the NA values with the string MISSING
# usually useful for numerical data
# you can fill NA values with numbers too

# how to cast datatypes?
# how to know the datatypes?
df.dtypes

df['age'].mean()
#NaN value is actually a float

type(np.nan) # result is float

df['age'] = df['age'].astype(int) # works fine if columns don't have
# missing values
# solve by: replacing missing values with 0 but not optimal,
# better to convert to float so NaN remains

df['age'] = df['age'].astype(float)
df.dtypes # now our age is of float type

df['age'].mean() # works!

# easier to handle missing value when loading a csv
na_vals = ['NA', 'Missing']
# add argument to pd.read_csv()
na_values = na_vals 

df['YearsCode'].head(10)
df['YearsCode'].head(10).mean() #doesn't work! cuz got missing vals
# solve by
df['YearsCode'] = df['YearsCode'].astype(float)
# doesn't work cuz there's a string 'Less than 1 year'
# let's see if there are more strings like this

df['YearsCode'].unique()
# identify that there are two string values
# now replace 'Less than 1 year' to 0
df['YearsCode'].replace('Less than 1 year', 0, inplace=True)
# then replace 'More than 50 years' with 51
df['YearsCode'].replace('More than 50 years', 51, inplace=True)

# noticed that dtype = object, so not float yet
# now convert to float
df['YearsCode'] = df['YearsCode'].astype(float)
# now we can grab the mean
df['YearsCode'].mean()
df['YearsCode'].median()


# Part 10
# Working With Dates and Time Series Data
# use 'ETH_1h.csv' as df

df.shape # shows number of rows and columns in df
df.loc[0, 'Date']

# convert the values in the column to date time
df['Date'] = pd.to_datetime(df['Date']) # doesn't work for the csv
# so do this
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
# specifies the order of datetime so pandas can interpret them
df.loc[0, 'Date'].day_name() # gives the result 'Friday' based
# on the date and time 

d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv('ETH_1h.csv', parse_dates=['Date'], 
	date_parser=d_parser) # sets the format of the datetime as csv
# file is being read

df['Date'].dt.day_name() # gives results of day names of the series

df['DayOfWeek'] = df['Date'].dt.day_name()
df # now you can see day of week column is added with the day names
# as values!

df['Date'].min() # gives earliest date in date column

# to view most recent date
df.['Date'].max()

# to get the amount of time between the two dates
df.['Date'].max() - df['Date'].min()

filt = (df['Date'] >= '2020')
df.loc[filt] # gives you values that are from 2020 and above

# if you want >= 2019 and <2020, use &
filt = (df['Date'] >= '2019') & (df['Date'] < '2020')

# instead of year, you can use datetimes
filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))
df.loc[filt]

df.set_index('Date') # index will be based on Date

# to make the change permanent,
df.set_index('Date', inplace=True)

df['2019'] 

# you can use slicing
df['2020-01':'2020-02'] # inclusive for both

df['2020-01':'2020-02']['Close'] # to get closing price for those dates
# to get the mean,
df['2020-01':'2020-02']['Close'].mean()

df['2020-01':'2020-02'].head(24) # get top 24 results for the dates

# let's now grab a single day
df['2020-01-01']['High'] 
# we want to grab the highest point for that one day so, use .max()
df['2020-01-01']['High'].max()

# notice that the day is broken down by hourly basis
# now let's make it so that it's broken down by days

df['High'].resample('D').max() # 'D' of daily basis
# this gives us a series as highest values for each date

# now assign that series to a variable
highs = df['High'].resample('D').max()
highs['2020-01-01'] 

# let's do a very simple plot with this information
%matplotlib inline
highs.plot() 

# what if we wanna resample for more than one column? or 
# the ENTIRE df
df.resample('W').mean() # resample by week 
# this is gonna give you the mean values for all the columns
# mean doesn't really make sense for some columns

# so we need to use multiple aggregation methods for different columns
# key is to use agg() method

# pass in a dictionary
df.resample('W').agg({'Close': 'mean', 'High': 'max', 
	'Low': 'min', 'Volume': 'sum'})
# result is the aggregate functions being applied to their respective
# columns!


















































