grafo = {}

while True:
    opc = input("Deseja adicionar uma aresta ao grafo? (S/N): ")
    if opc.lower() == "n":
        break
    
    v1 = input("Digite o primeiro vértice: ")
    v2 = input("Digite o segundo vértice: ")
    
    if v1 not in grafo:
        grafo[v1] = []
    if v2 not in grafo:
        grafo[v2] = []
    
    grafo[v1].append(v2)
    grafo[v2].append(v1)

print("Grafo:")
for v in grafo:
    print(v, "=", grafo[v])