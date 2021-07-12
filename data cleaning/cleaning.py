import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

calories = pd.read_csv('data/calories.csv')
exercise = pd.read_csv('data/exercise.csv')

#calories.head()
#exercise.head()

dataset = pd.DataFrame()
n = len(exercise['User_ID'])
print(n)
for i in range(n):
    if exercise['User_ID'][i] != calories['User_ID'][i]:
        print("mis match")

dataset['User_ID'] = exercise['User_ID']
dataset['Gender'] = exercise['Gender']
dataset['Age'] = exercise['Age']
dataset['Height'] = exercise['Height']
dataset['Weight'] = exercise['Weight']
dataset['Duration'] = exercise['Duration']
dataset['Heart_Rate'] = exercise['Heart_Rate']
dataset['Body_Temp'] = exercise['Body_Temp']
dataset['Calories'] = calories['Calories']

dataset['Gender'].replace(to_replace = 'female', value = 1, inplace = True)
dataset['Gender'].replace(to_replace = 'male', value = 0, inplace = True)

#dataset.head()

dataset.to_csv('Processed Dataset.csv')
