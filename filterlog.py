import pandas as pd

# Load the event log from CSV without column names
event_log = pd.read_csv("eventlog.csv", header=None, names=['caseID', 'activity','timestamp','duration','other'])

# Identify the start event
start_event = 'para_to_sent'

# Filter the log for instances where the start event occurs
filtered_log = event_log[event_log['activity'] == start_event]
filtered_log.to_csv("filtered_log.csv", index=False)
# Remove duplicates if any
filtered_log = filtered_log.drop_duplicates()

# Display the filtered log
print(filtered_log)
