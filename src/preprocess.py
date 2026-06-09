import pandas as pd
from sklearn.preprocessing import LabelEncoder

raw_data = '../data/raw_data.csv'
df =pd.read_csv(raw_data,header=None)


le = LabelEncoder()

for col in df.columns:
    #if df[col].dtype == 'object':
    df[col] = le.fit_transform(df[col].astype(str))

df.to_csv('../data/processed_data.csv',index = False,header=False)

print(f"Success! Processed {len(df)} rows")
print(f"first row of data ",df.iloc[0].values)