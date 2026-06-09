import pickle
import pandas as pd

with open('../models/nids_model.pkl', 'rb') as f:
    trained_ai = pickle.load(f)

df = pd.read_csv('../data/processed_data.csv',skiprows=1,header=None)
df = df.apply(pd.to_numeric,errors='coerce').dropna()
sample_row = df.iloc[0:1,:-1]

prediction = trained_ai.predict(sample_row)

if prediction[0] == 1:
    print("ALERT: Hacking State detected!")
else:
    print("System Safe: Normal Traffic")