import numpy as np

# Define a simple linear regression model
def linear_regression(X, weights):
    return np.dot(X, weights)

# Generate synthetic data for two clients
client1_data = np.array([[1.0], [2.0], [3.0]])
client2_data = np.array([[4.0], [5.0], [6.0]])
client1_target = np.array([2.0, 3.0, 4.0])
client2_target = np.array([5.0, 6.0, 7.0])

# Initialize model parameters for each client
client1_weights = np.random.rand(1)
client2_weights = np.random.rand(1)

# Perform federated learning iterations
learning_rate = 0.01
num_iterations = 100

for _ in range(num_iterations):
    # Client 1
    client1_predictions = linear_regression(client1_data, client1_weights)
    client1_error = client1_target - client1_predictions
    client1_weights += learning_rate * np.dot(client1_data.T, client1_error)

    # Client 2
    client2_predictions = linear_regression(client2_data, client2_weights)
    client2_error = client2_target - client2_predictions
    client2_weights += learning_rate * np.dot(client2_data.T, client2_error)

# Perform federated aggregation (simple average in this case)
final_weights = (client1_weights + client2_weights) / 2

# The final weights represent the global model learned from federated data

print("Final Model Weights:", final_weights)
