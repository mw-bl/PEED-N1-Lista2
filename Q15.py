grafo = {}

while True:
    vertice = input("Digite os vértices da aresta (ou 'sair' para encerrar): ")
    if vertice == 'sair':
        break
    ver1, ver2 = ver1.split()
    if ver1 not in g:
        g[ver1] = set()
    if ver2 not in g:
        g[ver2] = set()
    g[ver1].add(ver2)
    g[ver2].add(ver1)

if 'A' in g and 'C' in g['A']:
    print("A aresta ('A', 'C') está presente no grafo")
else:
    print("A aresta ('A', 'C') não está presente no grafo")