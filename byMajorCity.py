import pandas as pd
df = pd.read_csv('GlobalLandTemperaturesByMAjorCity.csv')

#list of cities
countries = []
for country in df['Country'].unique():
    countries.append(country)
print("List of countries: ", countries)
print("Number of countries: ", len(countries))

#cities in each country
df_cities = df.copy()
df_cities = df_cities.groupby(['Country', 'City']).count()
print("Cities in each country and number of dates (months): ")
print(df_cities[['dt']])