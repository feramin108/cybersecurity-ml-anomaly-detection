import os
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib

def load_data(data_dir):
    """Load and combine datasets from the specified directory."""
    network_df = pd.read_csv(os.path.join(data_dir, 'network_traffic_logs.csv'))
    user_df = pd.read_csv(os.path.join(data_dir, 'user_behavior_logs.csv'))
    system_df = pd.read_csv(os.path.join(data_dir, 'system_logs.csv'))
    
    combined_df = pd.concat([network_df, user_df, system_df], ignore_index=True)
    return combined_df

def preprocess_data(df):
    """Preprocess the combined DataFrame."""
    X = df.drop(columns=['timestamp', 'anomaly_label'])
    y = df['anomaly_label']
    
    # One-hot encode categorical variables
    X = pd.get_dummies(X, drop_first=True)
    
    return X, y

def save_model(model, model_dir, filename):
    """Save the model to the specified directory."""
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, filename)
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

def load_model(model_dir, filename):
    """Load a model from the specified directory."""
    model_path = os.path.join(model_dir, filename)
    return joblib.load(model_path)
