weight = 0.5
input = 0.5
goal_prediction = 0.8
lr = 0.001

def neural_network(input, weight):
    prediction = input * weight
    return prediction

for i in range(1101):
    prediction = neural_network(input, weight)
    error = (prediction - goal_prediction) ** 2

    up_prediction = input * (weight + lr)
    up_error = (goal_prediction - up_prediction) ** 2

    down_prediction = input * (weight + lr)
    down_error = (goal_prediction - down_prediction) ** 2

    if error != down_error or error != up_error:
        if up_error > down_error:
            weight -= lr
            if i % 50 == 0:
                print('{}{: >3}'.format(list[x].ljust(15, ' '), x))
                print('iteration #{: >3} | prediction = {: >3}\
                |updated weight = {: >3} | Error = {: >3} | Direction: DOWN'.format(i, round(up_prediction, 3), round(weight, 4), up_error))
                print(f'iteration #{i} | prediction = {round(down_prediction, 3)} |updated weight = {round(weight, 4)} | Error = {down_error} | Direction: DOWN')
        elif up_error <= down_error:
            weight += lr
            if i % 50 == 0: 
                print(f'iteration #{i} | prediction = {round(up_prediction, 3)} |updated weight = {round(weight, 4)} | Error = {up_error} | Direction: UP')

