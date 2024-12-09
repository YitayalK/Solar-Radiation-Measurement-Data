import pandas as pd # importing pandas
import matplotlib.pyplot as plt #importing matploatlib
import seaborn as sns #importing seaborn

df = pd.read_csv("D:/File Pack/Courses/10Acadamey/Kifiya AIM Week 0/data/benin-malanville.csv", encoding='utf-8', parse_dates=['Timestamp']) #  Load the dataset
#print(df.head(5))
df.set_index('Timestamp', inplace=True)

monthly_data = df.resample('ME').mean() # Resampling to monthly frequency


plt.figure(figsize=(14, 8))

# Plot GHI
plt.subplot(2, 2, 1)
plt.plot(monthly_data.index, monthly_data['GHI'], marker='o', color='orange')
plt.title('Monthly Average GHI')
plt.xlabel('Date')
plt.ylabel('GHI (W/m²)')

# Plot DNI
plt.subplot(2, 2, 2)
plt.plot(monthly_data.index, monthly_data['DNI'], marker='o', color='blue')
plt.title('Monthly Average DNI')
plt.xlabel('Date')
plt.ylabel('DNI (W/m²)')

# Plot DHI
plt.subplot(2, 2, 3)
plt.plot(monthly_data.index, monthly_data['DHI'], marker='o', color='green')
plt.title('Monthly Average DHI')
plt.xlabel('Date')
plt.ylabel('DHI (W/m²)')

# Plot Tamb
plt.subplot(2, 2, 4)
plt.plot(monthly_data.index, monthly_data['Tamb'], marker='o', color='red')
plt.title('Monthly Average Temperature (Tamb)')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')

plt.tight_layout()
plt.show()
