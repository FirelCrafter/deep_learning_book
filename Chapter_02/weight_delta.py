weight = 0.0
goal_pred = 0.8
input = 1.1

for iteration in range(50):
    pred = input * weight
    error = (pred - goal_pred) ** 2
    delta = pred - goal_pred
    weight_delta = delta * input
    weight = weight - weight_delta

    print(f'Error: {round(error, 4)}, Prediction {round(pred, 4)}')