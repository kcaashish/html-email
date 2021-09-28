import pandas as pd

data = pd.read_csv('data/09172021_complete_data.csv', sep=",")

with open("data.json", "w") as f:
    f.write(data.to_json(orient='records'))