import os
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Ensure the data directory exists
data_dir = 'data'
model_dir = 'models'
os.makedirs(model_dir, exist_ok=True)

# Load the datasets
network_df = pd.read_csv(os.path.join(data_dir, 'network_traffic_logs.csv'))
user_df = pd.read_csv(os.path.join(data_dir, 'user_behavior_logs.csv'))
system_df = pd.read_csv(os.path.join(data_dir, 'system_logs.csv'))

# Combine datasets
combined_df = pd.concat([network_df, user_df, system_df], ignore_index=True)

# Prepare the features (X) and labels (y)
X = combined_df.drop(columns=['timestamp', 'anomaly_label'])
y = combined_df['anomaly_label']

# One-hot encode categorical variables
X = pd.get_dummies(X, drop_first=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the Isolation Forest model
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(X_train)

# Make predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Convert predictions from {-1, 1} to {0, 1}
y_pred_train = [1 if pred == -1 else 0 for pred in y_pred_train]
y_pred_test = [1 if pred == -1 else 0 for pred in y_pred_test]

# Evaluate the model
print("Training Data Evaluation:")
print(confusion_matrix(y_train, y_pred_train))
print(classification_report(y_train, y_pred_train))

print("\nTest Data Evaluation:")
print(confusion_matrix(y_test, y_pred_test))
print(classification_report(y_test, y_pred_test))

# Save the model to a file
import joblib
model_filename = os.path.join(model_dir, 'anomaly_detection_model.pkl')
joblib.dump(model, model_filename)
print(f"Model saved to {model_filename}")
