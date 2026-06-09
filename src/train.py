import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('../data/processed_data.csv',skiprows=1,header=None)

df_numeric = df.apply(pd.to_numeric,errors='coerce')
df_clean = df_numeric.dropna()
if len(df_clean) ==0:
    print("ERROR : Data is empty or all text. Check preprocess.py")
else:
    print(f"SUCCESS! Training {len(df_clean)}  rows for pure numbers")

X =df_clean.iloc[:,:-1]
y = df_clean.iloc[:,-1]

model = RandomForestClassifier(n_estimators=100)
model.fit(X,y)

with open('../models/nids_model.pkl','wb') as f:
    pickle.dump(model,f)

print("Success: AI model trained and saved to models/nids_model.pkl")
