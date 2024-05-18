import networkx as nx

n = 6 # кол-во вершин
p = 0.55 # вероятность появления случайного ребра

G = nx.erdos_renyi_graph(n, p) # построение графа в модели Эрдёша-Реньи

a = 0
for n in G.nodes():
    a = a + G.degree(n)

a_fact = float(a) / len(G.nodes()) #  средняя степень вершины
a_rasch = (n-1)*p # средняя степень вершины расчетная по формуле


st_dev = a_fact - a_rasch # сравнение значений
print("Средняя степень вершины (полученная) : ", round(a_fact, 3))
print("Средняя степень вершины (расчетная по формуле): ", a_rasch )
print("Разница значений: ",round(a_fact, 3), "-", a_rasch, "=",  round(st_dev, 3))