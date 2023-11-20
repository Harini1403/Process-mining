import pandas as pd

# Load the event log from CSV without column names
event_log = pd.read_csv("eventlog.csv", header=None, names=['caseID', 'activity','timestamp','duration','other'])

# Identify a unique start event for each case
start_events = event_log.groupby('caseID')['activity'].first().reset_index()

# Merge with the original event log to get all activities
filtered_log = pd.merge(event_log, start_events, on='caseID', how='inner')

# Save the filtered log to a new CSV file
filtered_log.to_csv("filtered_activity_log.csv", index=False)

# Display the filtered log
print(filtered_log)
