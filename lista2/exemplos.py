import matplotlib.pyplot as plt
 
# Dados das avaliações
muito_ruim = 5
ruim = 12
regular = 20
bom = 30
muito_bom = 33
 
# Criando o gráfico de linhas
labels = ['Muito Ruim', 'Ruim', 'Regular', 'Bom', 'Muito Bom']
values = [muito_ruim, ruim, regular, bom, muito_bom]
 
plt.plot(labels, values)
plt.title('Avaliações 360')
plt.xlabel('Métricas')
plt.ylabel('Quantidade')

# Dados das avaliações
muito_ruim = 5
ruim = 12
regular = 20
bom = 30
muito_bom = 33
 
# Criando o gráfico de pizza
labels = ['Muito Ruim', 'Ruim', 'Regular', 'Bom', 'Muito Bom']
values = [muito_ruim, ruim, regular, bom, muito_bom]
 
plt.pie(values, labels=labels)
plt.title('Avaliações 360')
plt.show()
