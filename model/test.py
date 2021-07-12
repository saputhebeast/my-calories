import joblib

loaded_model = joblib.load("calories_model.sav")

x = loaded_model.predict([[0, 12, 56, 45, 35, 89, 78]])
print(x)