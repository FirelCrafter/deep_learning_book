# при большой разнице input и weight нужно использовать коэффициент alpha, что бы предотвратить расхождение

weight = 0.5
goal_pred = 0.8
input = 2
alpha = 0.1

for iteration in range(20):
    pred = input * weight
    error = (pred - goal_pred) ** 2
    derivative = input * (pred - goal_pred)
    weight = weight - (alpha * derivative)

    print(f'Error: {round(error, 4)}, Prediction {round(pred, 4)}')