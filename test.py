import random
import datetime
import csv
import pandas as pd
import pm4py
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.visualization.dfg import visualizer as dfg_visualization

class Activity:
    def __init__(self, name):
        self.name = name

    def execute(self):
        # Simulate activity execution time
        execution_time = random.uniform(1, 25)  # Adjust range based on complexity
        return execution_time

class Department:
    def __init__(self, name):
        self.name = name
        self.complexities = ['Low', 'Medium', 'High']
        random.shuffle(self.complexities)  # Shuffle the complexities list
        self.activities = [Activity(f'{self.name}-{i}') for i in range(1, 4)]

    def execute_activities(self):
        prev_timestamp = datetime.datetime.now()
        for activity in self.activities:
            if not self.complexities:
                self.complexities = ['Low', 'Medium', 'High']
                random.shuffle(self.complexities)
            execution_time = activity.execute()
            timestamp = prev_timestamp + datetime.timedelta(seconds=execution_time)
            prev_timestamp = timestamp
            complexity = self.complexities.pop(0)  # Pop the first element from shuffled list
            yield timestamp, activity.name, self.name, complexity, execution_time

def generate_department_event_logs(num_products):
    departments = ['A', 'B', 'C']
    department_event_logs = {}

    for dept_name in departments:
        department = Department(dept_name)
        department_logs = []
        for product_index in range(1, num_products + 1):
            for activity_info in department.execute_activities():
                timestamp, activity_name, department_name, complexity, execution_time = activity_info
                department_logs.append((timestamp, f'P{product_index}', activity_name, department_name, complexity, execution_time))
        department_event_logs[dept_name] = department_logs

        # Convert department event logs to CSV
        output_file_prefix = f'{dept_name}_event_logs'
        event_logs_to_csv(department_logs, output_file_prefix)

    return department_event_logs

def event_logs_to_csv(event_logs, output_file_prefix):
    output_file = f'{output_file_prefix}.csv'
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Timestamp', 'Product', 'Activity', 'Department', 'Complexity', 'Duration']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in event_logs:
            timestamp, product, activity, department, complexity, duration = entry
            timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # Format timestamp
            writer.writerow({'Timestamp': timestamp_str, 'Product': product, 'Activity': activity, 'Department': department, 'Complexity': complexity, 'Duration': duration})

    # Group by complexity and write to separate CSV files
    complexity_files = {}
    for complexity in ['Low', 'Medium', 'High']:
        complexity_files[complexity] = []

    for entry in event_logs:
        _, _, _, _, complexity, _ = entry
        complexity_files[complexity].append(entry)

    for complexity, entries in complexity_files.items():
        output_file = f'{output_file_prefix}_{complexity.lower()}.csv'
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for entry in entries:
                timestamp, product, activity, department, _, duration = entry
                timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # Format timestamp
                writer.writerow({'Timestamp': timestamp_str, 'Product': product, 'Activity': activity, 'Department': department, 'Complexity': complexity, 'Duration': duration})

        # Generate XES file
        dataframe = pd.read_csv(output_file, sep=',')
        dataframe = pm4py.format_dataframe(dataframe, case_id='Product', activity_key='Activity', timestamp_key='Timestamp')
        event_log = pm4py.convert_to_event_log(dataframe)
        pm4py.write_xes(event_log, f'{output_file_prefix}_{complexity.lower()}.xes')

        # Generate DFG graph
        log = pm4py.read_xes(f'{output_file_prefix}_{complexity.lower()}.xes')
        dfg = dfg_discovery.apply(log, variant=dfg_discovery.Variants.PERFORMANCE)

        # Convert nanoseconds to milliseconds
        dfg_scaled = dfg.copy()  # Make a copy to avoid modifying the original DFG
        for edge in dfg_scaled:
            dfg_scaled[edge] /= 10**6  # Convert nanoseconds to milliseconds

        # Visualize DFG with time scaled to milliseconds
        try:
            gviz = dfg_visualization.apply(dfg_scaled, log=log, variant=dfg_visualization.Variants.PERFORMANCE.value)
            dfg_visualization.view(gviz)
        except Exception as e:
            print(f"Error visualizing DFG for {output_file}: {str(e)}")

# Generate event logs for each department
num_products = int(input("Enter the number of products: "))
department_event_logs = generate_department_event_logs(num_products)

print("Department-wise event logs generated and saved as CSV files.")
