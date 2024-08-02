import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Define the central server
server = KNeighborsClassifier(n_neighbors=2)

# Data and labels for clients
data1 = np.array([[1, 2], [2, 3], [3, 4]])
data2 = np.array([[4, 5], [5, 6], [6, 7]])
labels1 = np.array([0, 1, 0])
labels2 = np.array([1, 0, 1])

# Train KNN models on clients
knn1 = KNeighborsClassifier(n_neighbors=2)
knn1.fit(data1, labels1)

knn2 = KNeighborsClassifier(n_neighbors=2)
knn2.fit(data2, labels2)

# Share KNN models with the server (central aggregation)
server.fit(np.vstack((data1, data2)), np.hstack((labels1, labels2)))

# Federated inference on the server
def federated_knn(query):
    prediction = server.predict(query)
    return prediction

# Query the federated KNN model
query_data = np.array([[1, 2], [5, 6]])
result = federated_knn(query_data)

print("Predictions:", result)
