import numpy.random as rd

def simulacao(xmin, xmax, ymin, ymax, pontos_total):
    pontos_circulo = 0
    for _ in range(pontos_total):
        x = rd.uniform(xmin, xmax)
        y = rd.uniform(ymin, ymax)

        if (x**2 + y**2) <= 1:
            pontos_circulo += 1
    valor_pi = (pontos_circulo / pontos_total) * 4

    return valor_pi



xmin, xmax = -1, 1
ymin, ymax = -1, 1
amostras_teste = [10, 20, 50, 100, 200, 500, 1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 10_000, 20_000, 50_000]

for n in amostras_teste:
    print(f'O valor aproximado de PI para {n} amostras é: {simulacao(xmin, xmax, ymin, ymax, n):.4f}')

    