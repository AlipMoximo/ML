import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.ensemble import GradientBoostingClassifier
import joblib

# Load preprocessed data
preprocessed_data_path = 'Kenya_preprocessed_data.xlsx'
df = pd.read_excel(preprocessed_data_path)

# Define features (X) and target variable (y)
X = df.drop(columns=['ISO3', 'Type', 'Country/Region', 'UNICEF Region', 'Data source', 'Sex', 'Age','Value','Upper','Lower'])
y = df['Indicator']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load the trained model
model_file = 'trained_model.pkl'
model = joblib.load(model_file)

# Predict on the test set
y_pred = model.predict(X_test)

# Save predictions to an Excel file
predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
predictions_df.to_excel('Kenya_test_predictions.xlsx', index=False)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Print evaluation metrics
print(f"Accuracy: {accuracy:.4f}")
print(f"MSE: {mse:.4f}")
