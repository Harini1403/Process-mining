import random
import datetime
import csv
import pandas as pd
import pm4py

class Activity:
    def __init__(self, name):
        self.name = name

    def execute(self):
        # Simulate activity execution time
        execution_time = random.uniform(1, 5)  # Adjust range based on complexity
        return execution_time

class Department:
    def __init__(self, name):
        self.name = name
        self.complexity = random.choice(['Low', 'Medium', 'High'])
        self.activities = [Activity(f'{self.name}-{i}') for i in range(1, 4)]

    def execute_activities(self):
        for activity in self.activities:
            execution_time = activity.execute()
            yield activity.name, self.name, self.complexity, execution_time

def generate_event_logs(num_products):
    event_logs_all_products = {}

    for product_num in range(1, num_products + 1):
        product_name = f"Product_{product_num}"
        departments = ['A', 'B', 'C']

        event_logs = {}

        for dept_name in departments:
            department = Department(dept_name)
            event_logs[dept_name] = []
            for activity_info in department.execute_activities():
                event_logs[dept_name].append((datetime.datetime.now(), product_name, *activity_info))

        event_logs_all_products[product_name] = event_logs

    return event_logs_all_products

def event_logs_to_csv(event_logs, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Product', 'Activity', 'Timestamp', 'Duration', 'Complexity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for product, logs in event_logs.items():
            for department, activities in logs.items():
                for activity in activities:
                    timestamp, product_name, activity_name, department_name, complexity, execution_time = activity
                    timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # Format timestamp
                    writer.writerow({'Product': product_name, 'Activity': activity_name, 'Timestamp': timestamp_str, 'Duration': execution_time, 'Complexity': complexity})

# Generate event logs for 1 product
num_products = 30
product_event_logs = generate_event_logs(num_products)
for product, event_logs in product_event_logs.items():
    for department, logs in event_logs.items():
        for log in logs:
            print(log)
        print()
    print()
# Convert event logs to CSV
output_file = 'event_logs.csv'
event_logs_to_csv(product_event_logs, output_file)

dataframe = pd.read_csv('event_logs.csv', sep=',')
dataframe = pm4py.format_dataframe(dataframe, case_id='Product', activity_key='Activity', timestamp_key='Timestamp')
event_log = pm4py.convert_to_event_log(dataframe)
pm4py.write_xes(event_log, 'exported.xes')

print(event_log)
