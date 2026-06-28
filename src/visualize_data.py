import os
print(os.getcwd())

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AI-Water-Usage/data/raw/gapminder.csv")
'''
continent_lifeExp = (
    df.groupby("continent")["lifeExp"]
    .mean()
    .sort_values(ascending = False)
)
plt.figure(figsize=(8,5))
continent_lifeExp.plot(kind = "bar")

plt.title("Avearge Life Expectancy by Continent")
plt.xlabel("Continent")
plt.ylabel("Life Expectancy")

plt.tight_layout()
plt.savefig("AI-Water-Usage/outputs/figures/life_expectancy_by_continent1.png")
plt.show()

average_lifeExp = (
    df.groupby("continent")["lifeExp"]
    .agg(["max","min","mean"])

)
print(average_lifeExp)


average_GDP = (
    df.groupby("continent")['gdpPercap']
    .mean()
    .sort_values(ascending = False)
)

print(average_GDP.head(10))
plt.figure(figsize=(8,5))
average_GDP.plot(kind = "bar")
plt.title("Average GDP Percapita by continent")
plt.xlabel("Continent")
plt.ylabel("Average GDP per capita")
plt.tight_layout()
plt.savefig(("AI-Water-Usage/outputs/figures/GDP_percapita_by_continent.png"))
plt.show()

#top 10 countries with the highest life expectency
top_10_lifeexp = (
    df.sort_values("lifeExp", ascending=False)
      [["country", "year", "lifeExp"]]
      .head(10)
)

print(top_10_lifeexp)

correlation=df["gdpPercap"].corr(df["lifeExp"])
print(correlation)

plt.figure(figsize=(8,5))

plt.scatter(
    df["gdpPercap"],
    df["lifeExp"]
)
plt.title("GDP per Capita vs Life Expectancy")
plt.xlabel("GDP per Capita")
plt.ylabel("Life Expectancy")

plt.show()

lifeExp_by_years = (
    df.groupby("year")["lifeExp"]
    .mean()
)
correlation = df["year"].corr(df["lifeExp"])
print(correlation)

plt.figure(figsize = (8,5))
plt.plot(
    lifeExp_by_years.index,
    lifeExp_by_years.values
)
plt.title("Average global life Expectancy Over Time")
plt.xlabel("Year")
plt.ylabel("Average Life Expectancy")

plt.tight_layout()
plt.show()
'''
continent_year = (
    df.groupby(["continent", "year"])["lifeExp"]
      .mean()
)

print(continent_year.head(20))
continent_year.unstack()