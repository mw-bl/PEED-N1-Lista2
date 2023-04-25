grafo = {}

ver1 = input("Digite os vértices separando-os por espaços: ").split()

for ver2 in ver1:
    grafo[ver2] = []

arestas = input("Digite as arestas separadas por espaço (ex: a b, c d): ").split(",")

for aresta in arestas:
    v1, v2 = aresta.strip().split()
    grafo[v1].append(v2)
    grafo[v2].append(v1)

print("Grafo antes de remover a aresta:")
for ver2, adjacentes in grafo.items():
    print(ver2, adjacentes)

arestaRemove = input("Digite a aresta a ser removida (ex: a b): ").strip().split()
v1, v2 = arestaRemove

grafo[v1].remove(v2)
grafo[v2].remove(v1)

print("Grafo após remover a aresta:")
for ver2, adjacentes in grafo.items():
    print(ver2, adjacentes)