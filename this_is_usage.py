#!/usr/bin/env python

import pandas as pd
import mymodel.titanic_sample.models.SVC

print(mymodel.__version__)
model = mymodel.load_model(mymodel.titanic_sample.models.SVC)
print(model)

df = pd.read_csv("src/mymodel/titanic_sample/train/data/input/test.csv")
from sklearn.preprocessing import LabelEncoder
encoder_sex = LabelEncoder()
df['Sex'] = encoder_sex.fit_transform(df['Sex'].values)

x_test = df[["Pclass", "Sex", "Fare"]].dropna()
y_test = model.predict(x_test)
print(y_test)
