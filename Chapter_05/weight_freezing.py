# Разрушительное свойство нейросетей: у Вас может иметься мощный вход с большой предсказательной способностью, 
# однако если сеть случайно выяснит, как получить точный прогноз на обучающих данных без его участия,
# она никогда не научится включать его в прогноз

def neural_network(input, weights):
    out = 0
    for i in range(len(input)):
        out += (input[i] * weights[i])
    return out

def ele_mul(scalar, vector):
    out = [0,0,0]
    for i in range(len(out)):
        out[i] = vector[i] * scalar
    return out

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

win_or_lose_binary = [1, 0, 0, 1]
true = win_or_lose_binary[0]

alpha = 0.3
weights = [0.1, 0.2, -.1]
input = [toes[0], wlrec[0], nfans[0]]

for iter in range(3):
    pred = neural_network(input, weights)

    error = (pred - true) ** 2
    delta = pred - true

    weight_deltas = ele_mul(delta, input)
    weight_deltas[0] = 0

    print(f'Iteration: {str(iter+1)}\nPred: {round(pred, 4)}\nError: {round(error, 4)}\nDelta: {round(delta, 4)}\nWeights:\n{str(weights)}')
    print(f'Weight deltas: {str(weight_deltas)}\n-----')

    for i in range(len(weights)):
        weights[i] -= alpha*weight_deltas[i]