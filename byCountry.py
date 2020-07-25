import pandas as pd
df = pd.read_csv('GlobalLandTemperaturesByCountry.csv')

df_country = df.copy()
df_country = df_country.groupby(['Country']).count()
print(df_country)

#list of countries
countries = []
for country in df['Country'].unique():
    countries.append(country)
print("List of countries: ", countries)
print("Number of countries: ", len(countries))


#continents - csv file
df_continents = df.copy()
df_continents = df_continents[(df_continents.Country == 'Antarctica') | (df.Country == 'Africa') |
                            (df_continents.Country == 'Asia') | (df.Country == 'Australia') |
                            (df_continents.Country == 'Europe') | (df.Country == 'North America') |
                            (df.Country == 'South America')]
print(df_continents.groupby(['Country']).count())  #check




