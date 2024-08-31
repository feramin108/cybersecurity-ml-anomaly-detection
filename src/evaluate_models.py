from sklearn.metrics import classification_report, confusion_matrix
from utils import load_data, preprocess_data, load_model

def evaluate_model(data_dir, model_dir, model_filename):
    """Load and evaluate the model."""
    # Load and preprocess data
    df = load_data(data_dir)
    X, y = preprocess_data(df)
    
    # Split data into training and testing sets
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Load the trained model
    model = load_model(model_dir, model_filename)
    
    # Evaluate the model
    y_pred_test = model.predict(X_test)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred_test))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred_test))

if __name__ == "__main__":
    data_dir = 'data'
    model_dir = 'models'
    model_filename = 'predictive_model.pkl'
    evaluate_model(data_dir, model_dir, model_filename)
