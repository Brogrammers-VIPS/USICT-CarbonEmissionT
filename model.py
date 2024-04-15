import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans
df = pd.read_csv("CO2_Emissions_India.csv")
print(df)
a = df.isnull().sum()
print(a)
b = df.nunique()
print(b)
numerical_cols = ['Engine Size(L)', 'Cylinders', 'Fuel Consumption City (L/100 km)', 'Fuel Consumption Hwy (L/100 km)', 'Fuel Consumption Comb (L/100 km)', 'Fuel Consumption Comb (mpg)', 'CO2 Emissions(g/km)']
c = df[numerical_cols].describe()
print(c)
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Plot histograms for Engine Size, Fuel Consumption, and CO2 Emissions
axs[0].hist(df['Engine Size(L)'], bins=20, color='skyblue', edgecolor='black')
axs[0].set_title('Engine Size Distribution')
axs[0].set_xlabel('Engine Size (L)')
axs[0].set_ylabel('Frequency')

axs[1].hist(df['Fuel Consumption Comb (L/100 km)'], bins=20, color='salmon', edgecolor='black')
axs[1].set_title('Fuel Consumption Distribution')
axs[1].set_xlabel('Fuel Consumption Comb (L/100 km)')
axs[1].set_ylabel('Frequency')

axs[2].hist(df['CO2 Emissions(g/km)'], bins=20, color='lightgreen', edgecolor='black')
axs[2].set_title('CO2 Emissions Distribution')
axs[2].set_xlabel('CO2 Emissions (g/km)')
axs[2].set_ylabel('Frequency')


plt.figure(figsize=(8, 6))
plt.scatter(df['Engine Size(L)'], df['CO2 Emissions(g/km)'], color='green', alpha=0.5)
plt.title('Engine Size vs. CO2 Emissions')
plt.xlabel('Engine Size (L)')
plt.ylabel('CO2 Emissions (g/km)')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='Fuel Type', y='CO2 Emissions(g/km)', data=df)
plt.title('CO2 Emissions by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('CO2 Emissions (g/km)')
plt.show()

avg_fuel_consumption_class = df.groupby('Vehicle Class')['Fuel Consumption Comb (L/100 km)'].mean().reset_index()
avg_co2_emissions_class = df.groupby('Vehicle Class')['CO2 Emissions(g/km)'].mean().reset_index()

# Create bar plots for average fuel consumption and CO2 emissions by vehicle class using Seaborn
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.barplot(x='Vehicle Class', y='Fuel Consumption Comb (L/100 km)', data=avg_fuel_consumption_class, palette='Blues')
plt.title('Average Fuel Consumption by Vehicle Class')
plt.xlabel('Vehicle Class')
plt.ylabel('Average Fuel Consumption (L/100 km)')
plt.xticks(rotation=45)


plt.subplot(1, 2, 2)
sns.barplot(x='Vehicle Class', y='CO2 Emissions(g/km)', data=avg_co2_emissions_class, palette='Greens')
plt.title('Average CO2 Emissions by Vehicle Class')
plt.xlabel('Vehicle Class')
plt.ylabel('Average CO2 Emissions (g/km)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

correlation_cols = ['Engine Size(L)', 'Cylinders', 
                    'Fuel Consumption Comb (L/100 km)', 'CO2 Emissions(g/km)']

# Calculating Pearson correlation coefficients
correlation_matrix = df[correlation_cols].corr()
# Print correlation matrix
print("Pearson correlation coefficients:")
print(correlation_matrix)
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})
plt.title('Correlation Matrix')
plt.show()

numerical_cols = ['Engine Size(L)', 'Cylinders', 
                  'Fuel Consumption Comb (L/100 km)', 'CO2 Emissions(g/km)']

# Create pair plot
sns.pairplot(df[numerical_cols])
plt.suptitle('Pair Plot of Numerical Variables', y=1.02)
plt.show()

avg_fuel_consumption_class = df.groupby('Vehicle Class')['Fuel Consumption Comb (L/100 km)'].mean().reset_index()
avg_co2_emissions_class = df.groupby('Vehicle Class')['CO2 Emissions(g/km)'].mean().reset_index()

# Create bar plots for average fuel consumption and CO2 emissions by vehicle class
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.barplot(x='Vehicle Class', y='Fuel Consumption Comb (L/100 km)', data=avg_fuel_consumption_class, palette='Blues')
plt.title('Average Fuel Consumption by Vehicle Class')
plt.xlabel('Vehicle Class')
plt.ylabel('Average Fuel Consumption (L/100 km)')
plt.xticks(rotation=45)


plt.subplot(1, 2, 2)
sns.barplot(x='Vehicle Class', y='CO2 Emissions(g/km)', data=avg_co2_emissions_class, palette='Greens')
plt.title('Average CO2 Emissions by Vehicle Class')
plt.xlabel('Vehicle Class')
plt.ylabel('Average CO2 Emissions (g/km)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

d = df
print(d)

e  = df.nunique()
print(e)

from sklearn.preprocessing import LabelEncoder


columns_to_encode = ['Make','Vehicle Class','Transmission','Fuel Type']
label_encoders = {}

for column in columns_to_encode:

    label_encoder = LabelEncoder()
    df[column] = label_encoder.fit_transform(df[column])
    label_encoders[column] = label_encoder
df,label_encoders

X=df.drop(columns=['Model','CO2 Emissions(g/km)'])
y=df['CO2 Emissions(g/km)']

X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=2,test_size=0.2)

xgb=XGBRegressor()
xgb.fit(X_train,y_train)

y_pred=xgb.predict(X_test)

mse=mean_squared_error(y_test,y_pred)
r2s=r2_score(y_test,y_pred)
print("mean squared error : ", mse)
print("r2 score :", r2s)

import pickle

with open('xgb_model_6mse.pkl','wb') as file:
    pickle.dump(xgb,file)









