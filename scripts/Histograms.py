import pandas as pd # importing pandas
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("D:/File Pack/Courses/10Acadamey/Kifiya AIM Week 0/data/benin-malanville.csv") #  Load the dataset

# Set up the figure and axes for  histograms
plt.figure(figsize=(15, 10))

# List of variables to plot
variables = ['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB']

# Loop through each variable and create a histogram
for i, var in enumerate(variables):
    plt.subplot(3, 2, i + 1)  # Create a grid of subplots
    plt.hist(df[var], bins=30, color='blue', alpha=0.7)  # Adjust bins as needed
    plt.title(f'Histogram of {var}')
    plt.xlabel(var)
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()