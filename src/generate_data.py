
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Parameters for data generation
num_records = 10000
start_time = datetime(2024, 8, 1)
end_time = datetime(2024, 8, 31)

def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def generate_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

def generate_protocol():
    return random.choice(['TCP', 'UDP', 'ICMP'])

def generate_resource():
    return random.choice(['/home/user/documents', '/var/log/system.log', '/etc/passwd'])

def generate_event_type():
    return random.choice(['process_start', 'file_modification', 'user_creation'])

# Generate network traffic logs
network_data = {
    'timestamp': [random_date(start_time, end_time) for _ in range(num_records)],
    'source_ip': [generate_ip() for _ in range(num_records)],
    'destination_ip': [generate_ip() for _ in range(num_records)],
    'source_port': [random.randint(1024, 65535) for _ in range(num_records)],
    'destination_port': [random.randint(1024, 65535) for _ in range(num_records)],
    'protocol': [generate_protocol() for _ in range(num_records)],
    'bytes_transferred': [random.randint(40, 15000) for _ in range(num_records)],
    'anomaly_label': [random.choices([0, 1], weights=[0.95, 0.05])[0] for _ in range(num_records)]
}

network_df = pd.DataFrame(network_data)
network_df.to_csv('data/network_traffic_logs.csv', index=False)

# Generate user behavior logs
user_data = {
    'timestamp': [random_date(start_time, end_time) for _ in range(num_records)],
    'user_id': [random.randint(1, 100) for _ in range(num_records)],
    'login_success': [random.choice([True, False]) for _ in range(num_records)],
    'accessed_resource': [generate_resource() for _ in range(num_records)],
    'activity_type': [random.choice(['login', 'file_access', 'db_query']) for _ in range(num_records)],
    'anomaly_label': [random.choices([0, 1], weights=[0.97, 0.03])[0] for _ in range(num_records)]
}

user_df = pd.DataFrame(user_data)
user_df.to_csv('data/user_behavior_logs.csv', index=False)

# Generate system logs
system_data = {
    'timestamp': [random_date(start_time, end_time) for _ in range(num_records)],
    'event_type': [generate_event_type() for _ in range(num_records)],
    'source': [random.choice(['application', 'system', 'user']) for _ in range(num_records)],
    'severity_level': [random.choice(['low', 'medium', 'high']) for _ in range(num_records)],
    'anomaly_label': [random.choices([0, 1], weights=[0.98, 0.02])[0] for _ in range(num_records)]
}

system_df = pd.DataFrame(system_data)
system_df.to_csv('data/system_logs.csv', index=False)
