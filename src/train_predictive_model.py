from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from utils import load_data, preprocess_data, save_model

def train_predictive_model(data_dir, model_dir):
    """Train a predictive model using RandomForest."""
    # Load and preprocess data
    df = load_data(data_dir)
    X, y = preprocess_data(df)
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model on the training set
    print("Training set evaluation:")
    y_pred_train = model.predict(X_train)
    print(classification_report(y_train, y_pred_train))
    
    # Evaluate the model on the test set
    print("Test set evaluation:")
    y_pred_test = model.predict(X_test)
    print(classification_report(y_test, y_pred_test))
    
    # Save the trained model
    save_model(model, model_dir, 'predictive_model.pkl')

if __name__ == "__main__":
    data_dir = 'data'
    model_dir = 'models'
    train_predictive_model(data_dir, model_dir)
