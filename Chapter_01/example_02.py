# Принимает на вход несколько значений и возвращает одно значение
weights = [0.1, 0.2, 0]

def neural_network(input, weights):
    pred = w_sum(input, weights)
    return pred

def w_sum(a, b):
    assert(len(a) == len(b))

    output = 0

    for i in range(len(a)):
        output += (a[i] * b[i])

    return output

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wlrec[0], nfans[0]]

pred = neural_network(input, weights)
print(pred)