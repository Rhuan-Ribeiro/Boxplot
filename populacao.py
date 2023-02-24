#  Impotação das bibliotecas
import numpy as np
import matplotlib.pyplot as plot

#  Carregamento dos dados
populacao = [988.8, 556.9, 224.6, 210.9, 201.5, 187.7, 151.6, 135.8, 129.8, 119.4, 116.0, 102.3, 101.8, 92.4, 84.7,
             33.9, 80.2, 74.7, 72.7, 68.4, 66.8, 66.8, 63.7, 62.8, 61.9, 56.2, 54.1, 50.3, 49.7, 46.3]
sudeste = [988.8, 556.9, 210.9, 101.8, 92.4, 84.7, 33.9, 72.7, 68.4, 63.7, 62.8, 50.3, 49.7, 46.3]

#  Processamento dos dados GERAL
q1g = np.percentile(populacao, 25, method="averaged_inverted_cdf")
q2g = np.percentile(populacao, 50, method="averaged_inverted_cdf")
q3g = np.percentile(populacao, 75, method="averaged_inverted_cdf")

dqg = q3g - q1g

limite_inferiorg = np.fmax(min(populacao), q1g - 1.5 * dqg)
limite_superiorg = np.fmin(max(populacao), q3g + 1.5 * dqg)

#  Processamento dos dados SUDESTE
q1s = np.percentile(sudeste, 25, method="averaged_inverted_cdf")
q2s = np.percentile(sudeste, 50, method="averaged_inverted_cdf")
q3s = np.percentile(sudeste, 75, method="averaged_inverted_cdf")

dqs = q3s - q1s

limite_inferiors = np.fmax(min(sudeste), q1s - 1.5 * dqs)
limite_superiors = np.fmin(max(sudeste), q3s + 1.5 * dqs)

#  Apresentação dos dados GERAL
print('POPULAÇÃO GERAL')
print(f'Q1 = {q1g}')
print(f'Q2 = {q2g}')
print(f'Q3 = {q3g}')
print(f'Limite Superior = {limite_superiorg:.2f}')
print(f'Limite Inferior = {limite_inferiorg:.2f}')

#  Apresentação dos dados SUDESTE
print('POPULAÇÃO SUDESTE')
print(f'Q1 = {q1s}')
print(f'Q2 = {q2s}')
print(f'Q3 = {q3s}')
print(f'Limite Superior = {limite_superiors:.2f}')
print(f'Limite Inferior = {limite_inferiors:.2f}')

#  Criação do boxplot
diagramag = plot.boxplot(populacao, labels=["geral"], positions=[1])
diagramas = plot.boxplot(sudeste, labels=["sudeste"], positions=[2])

#  Janela do boxplot
plot.title("POPULAÇÔES")
plot.xlabel("total de população")
plot.ylabel("cidades")

plot.show()
