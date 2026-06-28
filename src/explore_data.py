import pandas as pd

df = pd.read_csv("data/raw/gapminder.csv")

print(df.groupby("continent")["lifeExp"].mean().sort_values(ascending = False))