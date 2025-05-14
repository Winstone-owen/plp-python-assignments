# COVID-19 Global Data Tracker

# 📦 1. Data Collection
# Assuming 'owid-covid-data.csv' is already downloaded into the working directory

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set plot styles
sns.set(style="darkgrid")

# 📊 2. Data Loading & Exploration
df = pd.read_csv("owid-covid-data.csv")
print("Columns:", df.columns)
print(df.head())
print(df.isnull().sum())

# 🧹 3. Data Cleaning
# Focus on selected countries
countries = ["Kenya", "United States", "India"]
df = df[df['location'].isin(countries)]

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Fill missing values
cols_to_fill = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'total_vaccinations']
df[cols_to_fill] = df[cols_to_fill].fillna(method='ffill')
df[cols_to_fill] = df[cols_to_fill].fillna(0)

# 📈 4. Exploratory Data Analysis
# Line chart: total cases over time
plt.figure(figsize=(12,6))
for country in countries:
    sns.lineplot(data=df[df['location'] == country], x='date', y='total_cases', label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.ylabel("Total Cases")
plt.xlabel("Date")
plt.legend()
plt.show()

# Line chart: total deaths over time
plt.figure(figsize=(12,6))
for country in countries:
    sns.lineplot(data=df[df['location'] == country], x='date', y='total_deaths', label=country)
plt.title("Total COVID-19 Deaths Over Time")
plt.ylabel("Total Deaths")
plt.xlabel("Date")
plt.legend()
plt.show()

# Bar chart: Latest total cases by country
latest = df.groupby('location').apply(lambda x: x[x['date'] == x['date'].max()]).reset_index(drop=True)
plt.figure(figsize=(8,5))
sns.barplot(x='location', y='total_cases', data=latest)
plt.title("Total COVID-19 Cases (Latest)")
plt.ylabel("Cases")
plt.xlabel("Country")
plt.show()

# Calculate death rate
latest['death_rate'] = latest['total_deaths'] / latest['total_cases']
print(latest[['location', 'death_rate']])

# 📊 5. Visualizing Vaccination Progress
plt.figure(figsize=(12,6))
for country in countries:
    sns.lineplot(data=df[df['location'] == country], x='date', y='total_vaccinations', label=country)
plt.title("Cumulative COVID-19 Vaccinations Over Time")
plt.ylabel("Total Vaccinations")
plt.xlabel("Date")
plt.legend()
plt.show()

# 🗺️ 6. Optional: Choropleth Map using Plotly
# Use latest snapshot from OWID for iso_code and cases
choropleth_df = df[df['date'] == df['date'].max()][['iso_code', 'location', 'total_cases']]
choropleth_df = choropleth_df.dropna()
fig = px.choropleth(
    choropleth_df,
    locations="iso_code",
    color="total_cases",
    hover_name="location",
    color_continuous_scale="Reds",
    title="Global COVID-19 Total Cases"
)
fig.show()

# 📝 7. Insights & Reporting.
# Sample insights written as markdown:
# - The USA had the highest number of total cases among selected countries.
# - India's vaccination numbers ramped up steeply from early 2021.
# - Kenya showed a delayed but steady vaccination trend.
# - Death rate in the USA is higher than in India and Kenya.
# - Visual trends indicate waves of infections at different intervals.

# Save the cleaned dataset for future use
latest.to_csv("latest_covid_summary.csv", index=False)
