import pandas as pd

df = pd.read_csv('D:/Usamaraza/Coding Practice/Python Libraries/Pandas Library/pokemon_data.csv')
#print(df.tail())
for col in df.columns:
    print(col)