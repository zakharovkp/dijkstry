import matplotlib.pyplot as plt
import networkx as nx  # импортируем библиотеки

G = nx.Graph()         # создаем пустой граф
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # добавляем вершины в граф
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]) # добавляем ребра в граф
centrality = nx.eigenvector_centrality_numpy(G) # расчитываем меры центральности
for n in centrality:
    print("c(", n, ")=", centrality[n]) # выводим результаты расчета для каждого узла
nx.draw(G, node_size=300, with_labels=True, node_color='y') # визуализация графа
plt.savefig("g1.png") # сохранение графа как png файл
plt.show() # вывод картинки на экран
