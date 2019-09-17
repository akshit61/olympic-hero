# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace = True)
data.head(10)


# --------------
#Code starts here




data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer',(np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both')))
print(data.head())
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here




top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries.drop(index = top_countries.index[-1],inplace =True)
top_countries.head()

def top_ten(dataframe,col_name):
    country_list= list(dataframe.nlargest(n=10,columns = col_name)['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
#print(top_10)

common = [x for x in top_10 if (x in top_10_summer and x in top_10_winter)]
print(common)


# --------------
#Code starts here
#data.head()
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

figure = plt.subplots(nrows = 1,ncols = 3 ,figsize = (12,4))
plt.subplot(1,3,1)
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.xticks(rotation = 90)

plt.subplot(1,3,2)
plt.bar(summer_df['Country_Name'],summer_df['Total_Winter'])
plt.xticks(rotation = 90)

plt.subplot(1,3,3)
plt.bar(summer_df['Country_Name'],summer_df['Total_Medals'])
plt.xticks(rotation = 90)
plt.show()



# --------------
#Code starts here
#.sort_values(by = 'Golden_Ratio',ascending = False)


summer_df.eval('Golden_Ratio = Gold_Summer/Total_Summer',inplace = True)
summer_df.sort_values(by = 'Golden_Ratio',ascending = False,inplace = True)
summer_max_ratio = summer_df['Golden_Ratio'].iloc[0]
print(summer_max_ratio)
summer_country_gold = summer_df['Country_Name'].iloc[0]
print(summer_country_gold)

winter_df.eval('Golden_Ratio = Gold_Winter/Total_Winter',inplace = True)
winter_df.sort_values(by = 'Golden_Ratio',ascending = False,inplace = True)
winter_max_ratio = winter_df['Golden_Ratio'].iloc[0]
print(winter_max_ratio)
winter_country_gold = winter_df['Country_Name'].iloc[0]
print(winter_country_gold)

top_df.eval('Golden_Ratio = Gold_Total/Total_Medals',inplace = True)
top_df.sort_values(by = 'Golden_Ratio',ascending = False,inplace = True)
top_max_ratio = top_df['Golden_Ratio'].iloc[0]
print(top_max_ratio)
top_country_gold = top_df['Country_Name'].iloc[0]
print(top_country_gold)



# --------------
#Code starts here

data_1 = data[:-1]
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']
#data_1.sort_values(by= 'Total_Points',ascending = False,inplace = True)
#most_points = data_1['Total_Points'].iloc[0]
most_points = data_1['Total_Points'].max()
print('Most Points : ' ,most_points)
#best_country = data_1['Country_Name'].iloc[0]
best_country = data_1[data_1['Total_Points'] == data_1['Total_Points'].max()].iloc[0,0]
print('Best Country : ',best_country)


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.info()

best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)
plt.show()


