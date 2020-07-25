import pandas as pd
df = pd.read_csv('GlobalLandTemperaturesByState.csv')

#countries which have states
df_countries = df.copy()
countries = []
for country in df_countries['Country'].unique():
    countries.append(country)
print("List of countries with states: ", countries)
print("Number of countries with states: ", len(countries))


#states in each country
df_states = df.copy()
df_states = df_states.groupby(['Country', 'State']).count()
print("States in each country and number of dates (months): ")
print(df_states[['dt']])


#only in Australia
df_australia = df.copy()
df_australia = df_australia[df_australia.Country == 'Australia']
print(df_australia.groupby(['Country', 'State']).count())  #check


#only in Brazil
df_brazil = df.copy()
df_brazil = df_brazil[df_brazil.Country == 'Brazil']
print(df_brazil.groupby(['Country', 'State']).count())  #check


#only in Canada
df_canada = df.copy()
df_canada = df_canada[df_canada.Country == 'Canada']
print(df_canada.groupby(['Country', 'State']).count())  #check


#only in China
df_china = df.copy()
df_china = df_china[df_china.Country == 'China']
print(df_china.groupby(['Country', 'State']).count())  #check


#only in India
df_india = df.copy()
df_india = df_india[df_india.Country == 'India']
print(df_india.groupby(['Country', 'State']).count())  #check


#only in Russia
df_russia = df.copy()
df_russia = df_russia[df_russia.Country == 'Russia']
print(df_russia.groupby(['Country', 'State']).count())  #check


#only in United States
df_us = df.copy()
df_us = df_us[df_us.Country == 'United States']
print(df_us.groupby(['Country', 'State']).count())  #check




