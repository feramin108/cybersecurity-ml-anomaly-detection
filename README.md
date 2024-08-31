



# Cybersecurity ML Anomaly Detection

This project demonstrates how to develop machine learning models for cybersecurity, focusing on anomaly detection and predictive analytics using synthetic data.

## Project Structure

- `data/`: Contains synthetic datasets for network traffic, user behavior, and system logs.
- `notebooks/`: Jupyter notebooks for data generation, model development, and analysis.
- `src/`: Python scripts for generating data, training models, and evaluating results.
- `requirements.txt`: List of Python dependencies required for the project.

![image](https://github.com/user-attachments/assets/9ebcd7c6-4e09-45e4-a384-d5a4f201c547)

## Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/cybersecurity-ml-anomaly-detection.git
cd cybersecurity-ml-anomaly-detection
```

### Step 2: Set Up the Environment
Create a virtual environment and install the required dependencies.
```bash

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

Step 3: Generate Synthetic Data
Generate fictional data for network traffic, user behavior, and system logs.

Option 1: Run the script directly.
```bash
python src/generate_data.py
```
Option 2: Use the Jupyter notebook.
```bash
jupyter notebook notebooks/01_generate_synthetic_data.ipynb
```
This will create three CSV files in the data/ directory.

