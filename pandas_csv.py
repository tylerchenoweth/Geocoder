import pandas as pd

# Load CSV into a DataFrame
df = pd.read_csv("locations.csv")


for row in df.iloc: 
    print(row['somethingzip'])
