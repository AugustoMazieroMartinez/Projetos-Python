import pandas as pd

df = pd.DataFrame(pd.read_excel('videogamesales.xlsx'))

count = df['Platform'].value_counts().head(10)
print(count)