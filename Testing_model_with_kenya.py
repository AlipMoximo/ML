# import required libraries
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# Load excel file into panda dataframe
file_path = 'HIV_Epidemiology_Children_Adolescents_2023 (2).xlsx'
df = pd.read_excel(file_path, sheet_name='Data')

# Select data specific to Uganda and within the range of 2014 to 2024
uganda_df = df[(df['Country/Region'] == 'Kenya') & (df['Year'].between(2014, 2024))].copy()

# Visual EDA
# 1. Distribution of numerical features
numerical_columns = uganda_df.select_dtypes(include=['int64', 'float64']).columns.tolist()
uganda_df[numerical_columns].hist(bins=20, figsize=(12, 8))
plt.suptitle('Distribution of Numerical Features')
plt.show()

# 2. Correlation heatmap
correlation_matrix = uganda_df[numerical_columns].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()


# 3. Categorical feature counts
categorical_columns = ['ISO3', 'Type', 'Country/Region', 'UNICEF Region', 'Indicator', 'Data source', 'Sex', 'Age']
for col in categorical_columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=uganda_df, x=col)
    plt.title(f'Count of {col}')
    plt.xticks(rotation=45)
    plt.show()

# Data Preprocessing
# 1. Handle numerical data
numerical_columns = uganda_df.select_dtypes(include=['int64', 'float64']).columns.tolist()
scaler = StandardScaler()
scaled_values = scaler.fit_transform(uganda_df.loc[:, numerical_columns])
scaled_values = scaled_values.astype(int)  # Explicitly cast to integer
uganda_df.loc[:, numerical_columns] = scaled_values

# 2. Handle categorical data
label_encoder = LabelEncoder()
categorical_columns = ['ISO3', 'Type', 'Country/Region', 'UNICEF Region', 'Indicator', 'Data source', 'Sex', 'Age','Value','Upper','Lower']
for col in categorical_columns:
    uganda_df.loc[:, col] = label_encoder.fit_transform(uganda_df[col])

# Selecting the columns of interest
columns_of_interest = ['Age', 'Sex', 'Indicator']

# Calculating correlation matrix
correlation_matrix = uganda_df[columns_of_interest].corr()

# Plotting the correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Now, the numerical and categorical data in 'uganda_df' are normalized/standardized and encoded, respectively.
uganda_df.to_excel('Kenya_preprocessed_data.xlsx', index=False)

