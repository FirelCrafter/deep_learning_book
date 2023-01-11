# Для любых input и goal_pred точное отношение между error и weight определяется
# Комбинацией формул  прогнозирования и вычисления ошибки

weight, goal_pred, input = (0.0, 0.8, 0.5)

for iteration in range(20):
    pred = input * weight
    error = (pred - goal_pred) ** 2 # В данном примере в этой строке
    delta = pred - goal_pred
    weight_delta = delta * input
    weight = weight - weight_delta
    print("Error: ", round(error, 4), " Prediction: ", round(pred, 4))