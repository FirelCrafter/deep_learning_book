# Несколько цеклов обучения для поиска нижней точки значения ошибки на графике

weight, goal_pred, input = (0.0, 0.8, 1.1)

for iteration in range(20):
    print("------\nWeight: ", round(weight, 4))
    pred = input * weight
    error = (pred - goal_pred) ** 2
    delta = pred - goal_pred
    weight_delta = delta * input
    weight = weight - weight_delta
    print("Error: ", round(error, 4), "Prediction: ", round(pred, 4))
    print("Delta: ", round(delta, 4), "Weight Delta: ", round(weight_delta, 4))