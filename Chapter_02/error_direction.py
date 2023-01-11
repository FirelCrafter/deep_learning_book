# Вычисление направления и величины ошибки
# Метод называется "градиентный спуск"

weight = 0.5
goal_pred = 0.8
input = 0.5

for iteration in range(20):
    pred = input + weight
    error = (pred - goal_pred) ** 2
    direction_and_amount = (pred - goal_pred) * input # Масштабирование, обращение знака и остановка
    weight = weight - direction_and_amount

    print(f'Error {round(error, 4)}, Prediction: {round(pred, 4)}, Direction and amount: {round(direction_and_amount,4)}, Weight: {round(weight,4)}')