def perceptronTrain(w, n, x, yd):
    # w: Array de pesos [w0, w1, w2, ...]
    # n: Taxa de aprendizagem
    # x: Matriz de entradas[[x0, x1, x2, ...], [x0, x1, x2, ...], ...]
    # yd: Array de saídas esperadas

    cycles = 0

    while(True):
        cycles += 1

        repeat = False
        for i in range(len(x)):
            sum = 0.0

            for j in range(len(w)):
                sum += w[j]*x[i][j]
            
            sum = float("{:.2f}".format(sum)) # Considerar apenas duas casas decimais

            if(sum >= 0):
                y = 1
            else:
                y = 0

            if(yd[i] != y):
                repeat = True
                for j in range(len(w)):
                    w[j] = w[j] + n*x[i][j]*(yd[i] - y)

        if(not repeat):
            break
    
    print("Ciclos:", cycles)
    print("w:", w)

def perceptronOutput(w, x):
    # w: Array de pesos [w0, w1, w2, ...]
    # x: Linha de entradas [x0, x1, x2, ...]

    sum = 0.0
    for i in range(len(w)):
        sum += w[i]*x[i]
    
    sum = float("{:.2f}".format(sum)) # Considerar apenas duas casas decimais

    if(sum >= 0):
        y = 1
    else:
        y = 0
    
    print("Somatório:", sum)
    print("y:", y)

# Entradas
w = [0, 0, 0, 0]
n = 1
x = [[1, 0, 0, 1], [1, 1, 0, 1], [1, 0, 0, 0], [1, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0]]
yd = [0, 1, 0, 1, 0, 1]
inputs = [[1, 1, 1, 1], [1, 0, 1, 0]]

print("---Treinamento---")
perceptronTrain(w, n, x, yd)

print("\n---Novas Entradas---")
for i in inputs:
    perceptronOutput(w, i)