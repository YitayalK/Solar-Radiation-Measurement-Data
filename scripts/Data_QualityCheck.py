import pandas as pd # importing pandas

df = pd.read_csv("D:/File Pack/Courses/10Acadamey/Kifiya AIM Week 0/data/benin-malanville.csv") #  Load the dataset

missing_values = df.isnull().sum() #Check for missing values
print("Missing Values:\n", missing_values)