import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib

dataset = pd.read_csv('Processed Dataset.csv')

X = dataset[['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']]
y = dataset['Calories']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(y_pred)

filename = 'calories_model.sav'
joblib.dump(model, filename)

# loaded_model = joblib.load(filename)
# result = loaded_model.score(X_test, y_test)
# print(result)
