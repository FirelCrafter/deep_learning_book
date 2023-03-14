import numpy as np
np.random.seed(1)

def relu(x):
    return (x >= 0) * x

def relu2deriv(output):
    return output >= 0

batch_size = 100
alpha, iterations = (0.001, 300)
pixels_per_image, num_labels, hidden_size = (784, 10, 100)

