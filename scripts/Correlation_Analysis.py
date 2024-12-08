import pandas as pd # importing pandas
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("D:/File Pack/Courses/10Acadamey/Kifiya AIM Week 0/data/benin-malanville.csv") #  Load the dataset

# Step 2: Calculate correlation matrix for relevant columns
correlation_columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust', 'WD']
correlation_matrix = df[correlation_columns].corr()

# Step 3: Visualize the correlation matrix using a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Matrix')
plt.show()

# Step 4: Pair plot for solar radiation and temperature measures
sns.pairplot(df[["GHI", "DNI", "DHI", "TModA", "TModB"]])
plt.suptitle('Pair Plot of Solar Radiation Components and Temperature Measures', y=1.02)
plt.show()

# Step 5: Scatter matrix for wind conditions and solar irradiance
scatter_columns = ['WS', 'WSgust', 'WD', 'GHI', 'DNI', 'DHI']
pd.plotting.scatter_matrix(df[scatter_columns], figsize=(12, 12), alpha=0.8)
plt.suptitle('Scatter Matrix of Wind Conditions and Solar Irradiance')
