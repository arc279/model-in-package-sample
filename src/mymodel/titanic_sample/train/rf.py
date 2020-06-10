import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()

df = pd.read_csv("./data/input/train.csv")

from sklearn.preprocessing import LabelEncoder
encoder_sex = LabelEncoder()
df['Sex'] = encoder_sex.fit_transform(df['Sex'].values)

x = df[["Pclass", "Sex", "Fare"]]
y = df["Survived"]

model.fit(x, y)

import os
modelpath = f"data/models/{model.__class__.__name__}"
os.makedirs(modelpath, exist_ok=True)
with open(f"{modelpath}/model.pkl", 'wb') as fp:
    pickle.dump(model, fp)

with open(f"{modelpath}/__init__.py", 'w') as fp:
    pass

