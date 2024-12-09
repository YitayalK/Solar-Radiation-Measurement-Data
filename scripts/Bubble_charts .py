import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Step 1: Load the dataset
df = pd.read_csv("D:/File Pack/Courses/10Acadamey/Kifiya AIM Week 0/data/benin-malanville.csv") #  Load the dataset
# Create a bubble chart using Matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(df['GHI'], df['Tamb'], s=df['RH'] * 10, alpha=0.5)  # Adjust size factor as needed
plt.title('Bubble Chart: GHI vs. Tamb with Bubble Size as RH')
plt.xlabel('Global Horizontal Irradiance (GHI)')
plt.ylabel('Ambient Temperature (Tamb)')
plt.grid(True)
plt.show()