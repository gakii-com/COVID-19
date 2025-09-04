"""
COVID-19 Global Data Tracker
----------------------------
A Python script to analyze COVID-19 data using Pandas, Matplotlib, Seaborn, and Plotly.

Steps:
1. Load dataset
2. Clean data
3. Exploratory Data Analysis (EDA)
4. Country comparisons
5. Optional choropleth maps
6. Summarize insights
"""

# ------------------------------------------------------------
# 1. Import Libraries
# ------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Make plots look cleaner
plt.style.use("seaborn")

# ------------------------------------------------------------
# 2. Load Dataset
# ------------------------------------------------------------
# NOTE: Place owid-covid-data.csv in the same folder as this script
df = pd.read_csv("owid-covid-data.csv")

print("✅ Dataset loaded successfully!")
print("Rows & Columns:", df.shape)
print("\nFirst 5 rows:\n", df.head())

# ------------------------------------------------------------
# 3. Data Cleaning
# ------------------------------------------------------------
# Focus on selected countries
countries = ["Kenya", "United States", "India"]
df = df[df["location"].isin(countries)]

# Drop rows with missing date/location
df = df.dropna(subset=["date", "location"])

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Fill missing new cases/deaths with 0
df["new_cases"] = df["new_cases"].fillna(0)
df["new_deaths"] = df["new_deaths"].fillna(0)

# Interpolate vaccination data if available
if "total_vaccinations" in df.columns:
    df["total_vaccinations"] = df["total_vaccinations"].interpolate()

print("\n✅ Data cleaned. Ready for analysis!")

# ------------------------------------------------------------
# 4. Exploratory Data Analysis (EDA)
# ------------------------------------------------------------

# Total cases over time
plt.figure(figsize=(10,6))
for country in countries:
    data = df[df["location"] == country]
    plt.plot(data["date"], data["total_cases"], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.show()

# Total deaths over time
plt.figure(figsize=(10,6))
for country in countries:
    data = df[df["location"] == country]
    plt.plot(data["date"], data["total_deaths"], label=country)
plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.show()

# Daily new cases
plt.figure(figsize=(10,6))
for country in countries:
    data = df[df["location"] == country]
    plt.plot(data["date"], data["new_cases"], label=country)
plt.title("Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.show()

# Death rate calculation
df["death_rate"] = df["total_deaths"] / df["total_cases"]
death_rates = df.groupby("location")["death_rate"].max().sort_values(ascending=False)
print("\nTop Countries by Max Death Rate:\n", death_rates.head(10))

# Correlation heatmap
plt.figure(figsize=(8,6))
corr = df[["total_cases","total_deaths","new_cases","new_deaths","total_vaccinations"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ------------------------------------------------------------
# 5. Optional: Choropleth Map
# ------------------------------------------------------------
latest_data = df.sort_values("date").groupby("location").tail(1)

# Total cases choropleth
fig = px.choropleth(
    latest_data,
    locations="iso_code",
    color="total_cases",
    hover_name="location",
    color_continuous_scale="Reds",
    title="Total COVID-19 Cases by Country"
)
fig.show()

# Vaccination rate choropleth
if "people_fully_vaccinated_per_hundred" in latest_data.columns:
    fig = px.choropleth(
        latest_data,
        locations="iso_code",
        color="people_fully_vaccinated_per_hundred",
        hover_name="location",
        color_continuous_scale="Greens",
        title="Vaccination Rates (% Fully Vaccinated) by Country"
    )
    fig.show()

# ------------------------------------------------------------
# 6. Insights & Reporting
# ------------------------------------------------------------
print("\n📌 Sample Insights:")
print("1. India experienced the highest surge in daily new cases during 2021.")
print("2. The US had one of the fastest early vaccine rollouts but high death totals.")
print("3. Kenya showed lower case numbers but slower vaccination uptake.")
print("4. Death rates varied widely, partly due to differences in reporting.")
print("5. Vaccination rollout correlates with reduced new cases after mid-2021.")

print("\n✅ Analysis complete! View plots and interactive maps above.")
