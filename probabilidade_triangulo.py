import numpy.random as rd

def simulacao(comprimento, tentativas):
    triangulos = 0
    
    for _ in range(tentativas):
        x = rd.uniform(0, comprimento)
        y = rd.uniform(0, comprimento)

        if x < comprimento /2:
            if y < comprimento /2:
                if x + y > comprimento /2:
                    triangulos +=1 
    
    porcentagem = (triangulos/tentativas) *100
    
    return porcentagem


iter = [10, 20, 50, 
              100, 200, 500, 
              1_000, 2_000, 5_000, 
              10_000, 20_000, 50_000]

length = 10

for i in iter:
    print(f'Com {i} valores amostrais as chances aproximadas são: {simulacao(length, i):.2f}%')