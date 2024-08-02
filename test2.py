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
    durations = [] 
    departments = ['A', 'B', 'C']
    products = [f'P{i}' for i in range(1, num_products + 1)]
    department_event_logs = {}

    for dept_name in departments:
        department = Department(dept_name)
        department_logs = []
        dept_durations = []  # Store durations for this department
        for product_name in products:
            for activity_info in department.execute_activities():
                timestamp, activity_name, department_name, complexity, execution_time = activity_info
                dept_durations.append(execution_time)
                department_logs.append((timestamp, product_name, activity_name, department_name, complexity, execution_time))
        department_event_logs[dept_name] = department_logs
        durations.append(dept_durations)  # Append durations for this department

        # Convert department event logs to CSV
        output_file_prefix = f'event_logs_{dept_name}'
        event_logs_to_csv(department_logs, output_file_prefix)

    return durations, department_event_logs

def event_logs_to_csv(event_logs, output_file_prefix):
    output_file = f'{output_file_prefix}.csv'
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Timestamp', 'Product', 'Activity', 'Department', 'Complexity', 'Duration']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for activity in event_logs:
            timestamp, product_name, activity_name, department_name, complexity, execution_time = activity
            timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # Format timestamp
            writer.writerow({'Timestamp': timestamp_str, 'Product': product_name, 'Activity': activity_name, 'Department': department_name, 'Complexity': complexity, 'Duration': execution_time})
    dataframe = pd.read_csv(output_file, sep=',')
    dataframe = pm4py.format_dataframe(dataframe, case_id='Product', activity_key='Activity', timestamp_key='Timestamp')
    event_log = pm4py.convert_to_event_log(dataframe)
    pm4py.write_xes(event_log, f'{output_file_prefix}.xes')

        # Perform Heuristic Mining
    log = pm4py.read_xes(f'{output_file_prefix}.xes')
    start_activity_name = f'{department_name}-1'  # Construct the start activity name
    filtered_log = pm4py.filter_start_activities(log, [start_activity_name])
    heu_net, initial_marking, final_marking = heuristics_miner.apply(filtered_log, parameters={heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.1})

        # Visualize the heuristic net
    try:
            gviz = hn_visualizer.apply(heu_net, initial_marking, final_marking, parameters={"format": "png"})
            hn_visualizer.view(gviz)
    except Exception as e:
            print(f"Error visualizing heuristic net for department {department_name}: {str(e)}")

        # Discover Directly-Follows Graph (DFG)
    dfg = dfg_discovery.apply(log, variant=dfg_discovery.Variants.PERFORMANCE)

        # Convert nanoseconds to milliseconds
    dfg_scaled = dfg.copy()  # Make a copy to avoid modifying the original DFG
    for edge in dfg_scaled:
            dfg_scaled[edge] /= 10**6  # Convert nanoseconds to milliseconds

        # Visualize DFG with time scaled to milliseconds
    try:
            gviz = dfg_visualization.apply(dfg_scaled, log=log, variant=dfg_visualization.Variants.PERFORMANCE)
            dfg_visualization.view(gviz)
    except Exception as e:
            print(f"Error visualizing DFG for department {department_name}: {str(e)}")

def generate_combined_event_log(num_products, durations):
    start_time = datetime.datetime.strptime("12:00", "%H:%M")
    combined_event_log = []

    activities = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    current_time = start_time  # Initialize current time variable

    for product_index in range(1, num_products + 1):
        for activity_index in range(9):
            department_index = activity_index // 3  # Determine department index (0 for A, 1 for B, 2 for C)
            duration = durations[department_index][activity_index % 3]  # Get duration from the durations list
            
            # Calculate the timestamp based on the current time and duration
            timestamp = current_time + datetime.timedelta(seconds=sum(durations[department_index][:activity_index % 3]))

            # Update current time for the next iteration
            current_time = timestamp

            combined_event_log.append((timestamp, f'P{product_index}', activities[activity_index], duration))

    return combined_event_log

def event_log_to_csv(event_log, output_file_prefix):
    output_file = f'{output_file_prefix}.csv'
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Timestamp','Product', 'Activity', 'Duration']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in event_log:
            timestamp, product ,activity, duration = entry
            timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # Format timestamp
            writer.writerow({'Timestamp': timestamp_str, 'Duration': duration, 'Activity': activity, 'Product': product})

    dataframe = pd.read_csv(output_file, sep=',')
    dataframe = pm4py.format_dataframe(dataframe, case_id='Product', activity_key='Activity', timestamp_key='Timestamp')
    event_log = pm4py.convert_to_event_log(dataframe)
    pm4py.write_xes(event_log, f'{output_file_prefix}.xes')

        # Perform Heuristic Mining
    log = pm4py.read_xes(f'{output_file_prefix}.xes')
    start_activity_name = 'A-1'  # Construct the start activity name
    filtered_log = pm4py.filter_start_activities(log, [start_activity_name])
    parameters = {heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.1}  # Define parameters dictionary
    heu_net, initial_marking, final_marking = heuristics_miner.apply(log,parameters=parameters)

        # Visualize the heuristic net
    try:
            gviz = hn_visualizer.apply(heu_net, initial_marking, final_marking, parameters={"format": "png"})
            hn_visualizer.view(gviz)
    except Exception as e:
            print(f"Error visualizing heuristic net: {str(e)}")

        # Discover Directly-Follows Graph (DFG)
    dfg = dfg_discovery.apply(log, variant=dfg_discovery.Variants.PERFORMANCE)

        # Convert nanoseconds to milliseconds
    dfg_scaled = dfg.copy()  # Make a copy to avoid modifying the original DFG
    for edge in dfg_scaled:
            dfg_scaled[edge] /= 10**6  # Convert nanoseconds to milliseconds

        # Visualize DFG with time scaled to milliseconds
    try:
            gviz = dfg_visualization.apply(dfg_scaled, log=log, variant=dfg_visualization.Variants.PERFORMANCE)
            dfg_visualization.view(gviz)
    except Exception as e:
            print(f"Error visualizing DFG : {str(e)}")

'''def perform_heuristic_mining(log):
    start_activity_name = log[0][2]  # Extracting the activity name from the first entry in the log
    filtered_log = pm4py.filter_start_activities(log, [start_activity_name])
    heu_net, initial_marking, final_marking = heuristics_miner.apply(filtered_log, parameters={heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.1})

    # Visualize the heuristic net
    try:
        gviz = hn_visualizer.apply(heu_net, initial_marking, final_marking, parameters={"format": "png"})
        hn_visualizer.view(gviz)
    except Exception as e:
        print(f"Error visualizing heuristic net: {str(e)}")

    # Discover Directly-Follows Graph (DFG)
    dfg = dfg_discovery.apply(log, variant=dfg_discovery.Variants.PERFORMANCE)

    # Convert nanoseconds to milliseconds
    dfg_scaled = dfg.copy()  # Make a copy to avoid modifying the original DFG
    for edge in dfg_scaled:
        dfg_scaled[edge] /= 10**6  # Convert nanoseconds to milliseconds

    # Visualize DFG with time scaled to milliseconds
    try:
        gviz = dfg_visualization.apply(dfg_scaled, log=log, variant=dfg_visualization.Variants.PERFORMANCE)
        dfg_visualization.view(gviz)
    except Exception as e:
        print(f"Error visualizing DFG: {str(e)}")'''

# Generate event logs for each department
num_products = int(input("Enter the number of products: "))
durations, department_event_logs = generate_department_event_logs(num_products)

# Convert combined event log to CSV
combined_event_log = generate_combined_event_log(num_products, durations)
output_file_prefix = 'combined_event_logs'
event_log_to_csv(combined_event_log, output_file_prefix)

# Perform heuristic mining on department-wise event logs
#for department, event_log in department_event_logs.items():
   # perform_heuristic_mining(event_log)

# Perform heuristic mining on combined event log
#perform_heuristic_mining(combined_event_log)

print("CSV files generated successfully and heuristic mining performed.")
