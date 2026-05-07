
import pandas as pd

data=pd.read_csv("Weather_Data.csv")

data

"""#how to analyze the data

"""

data.head(5)

data.shape

data.index

data.columns

data.dtypes

data['Weather'].unique()

data.nunique()

data.count()

data['Weather'].value_counts()  #unique values with their count

data.info()

"""#find all the unique wind speed values in the data

"""

data['Wind Speed_km/h'].nunique()

data['Wind Speed_km/h'].unique()

"""#find the number of times when the weather is exactly clear"""

data.Weather.value_counts()

data.Weather == 'Clear'

data[data.Weather == 'Clear']

data.groupby('Weather').get_group('Clear')

"""#find the number of times the speed of wind is actually 4km/h"""

data[data['Wind Speed_km/h']== 4]

"""#find out all the null values in the data"""

data.isnull().sum()

data.notnull().sum()

"""#rename the column name "weather" name to "weather condition"
"""

data.rename(columns={'Weather' : 'Weather Condition'}) #renames temporarily

data.rename(columns={'Weather' : 'Weather Condition'} , inplace='True') #replace permanently

"""#what is mean 'visibility'"""

data.Visibility_km.mean()

"""#standard deviation of 'pressure'"""

data.Press_kPa.std()

"""#relative humidity variance"""

data['Rel Hum_%'].var()

"""#find all instances when snow was recorded"""

data['Weather Condition'].value_counts()

data['Weather Condition'].mean()

data[data['Weather Condition']].mean(numeric_only=True)

data[data['Weather Condition'].str.contains('Snow')].head(10)

"""#find all instances of 'wind speed is above 24' and'visibility is 25'"""

data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)]

"""#mean value for each column against weather condition"""

data.groupby('Weather Condition').mean(numeric_only=True)

"""#min and max values of each column against weather data"""

data.groupby('Weather Condition').min()

data.groupby('Weather Condition').max()

"""#show all the records when the weather conditon is fog"""

data[data['Weather Condition'] == 'Fog']

"""#find all instances when weather is clear or visibility is above 40"""

data[(data['Weather Condition']== 'Clear') | (data['Visibility_km']> 40)].tail(5)

"""#find all instances when weather is clear and relative humidity is greater than 50
##or
#visibilty is above 40
"""

data.head(1)

data[((data['Weather Condition']=='Clear') &(data['Rel Hum_%']>50))| (data['Visibility_km']>40)]
