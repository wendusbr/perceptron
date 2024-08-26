def treinaPerceptron(w, N, treino):
    ciclos = 0

    while(True):
        ciclos += 1
        print(f"Ciclo {ciclos}")

        repeat = False
        for i in range(len(treino)):

            somatorio = 0.0
            yd = treino[i][len(treino)-1]
            for j in range(len(w)):
                somatorio += w[j]*treino[i][j]
            
            # Considerar apenas duas casas decimais
            somatorio = float("{:.2f}".format(somatorio))

            if(somatorio >= 0):
                y = 1
            else:
                y = 0

            if(yd != y):
                repeat = True
                for j in range(len(w)):
                    w[j] = w[j] + N*treino[i][j]*(yd - y)

        print(w)
        if(not repeat):
            break
    
    print("Vetor w final:\n", w)

treinaPerceptron([0.1, 0.2, -0.2, -0.2, -0.3], 0.4, [[1, 1, 1, 0, 1, 0], [1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 0], [1 ,1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0]])