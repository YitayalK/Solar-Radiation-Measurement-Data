import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Step 1: Load the dataset
df = pd.read_csv("D:/File Pack/Courses/10Acadamey/Kifiya AIM Week 0/data/benin-malanville.csv") #  Load the dataset

# Display the first few rows of the DataFrame
print(df.head())

# Check for missing values and data types
print(df.info())

# Check for null values in each column
print(df.isnull().sum())
# Drop columns that are entirely null
df = df.drop('Comments', axis=1)