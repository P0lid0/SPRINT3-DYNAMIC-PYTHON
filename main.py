import random

# -----------------------------
# Simulação de dados
# -----------------------------
# Cada insumo será um dicionário:
# {"nome": str, "quantidade": int, "validade": int (dias para vencer)}

insumos = [
    {"nome": "Reagente A", "quantidade": random.randint(5, 50), "validade": random.randint(5, 100)},
    {"nome": "Reagente B", "quantidade": random.randint(5, 50), "validade": random.randint(5, 100)},
    {"nome": "Descartável X", "quantidade": random.randint(5, 50), "validade": random.randint(5, 100)},
    {"nome": "Descartável Y", "quantidade": random.randint(5, 50), "validade": random.randint(5, 100)},
    {"nome": "Reagente C", "quantidade": random.randint(5, 50), "validade": random.randint(5, 100)},
]

# -----------------------------
# FILA (Queue) - Consumo diário
# -----------------------------
class Fila:
    def __init__(self):
        self.items = []

    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if not self.vazia():
            return self.items.pop(0)
        return None

    def vazia(self):
        return len(self.items) == 0

    def mostrar(self):
        return self.items

# -----------------------------
# PILHA (Stack) - Consulta inversa
# -----------------------------
class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.items.pop()
        return None

    def vazia(self):
        return len(self.items) == 0

    def mostrar(self):
        return self.items

# -----------------------------
# BUSCA SEQUENCIAL
# -----------------------------
def busca_sequencial(lista, nome):
    for insumo in lista:
        if insumo["nome"] == nome:
            return insumo
    return None

# -----------------------------
# BUSCA BINÁRIA
# (lista deve estar ordenada por nome antes!)
# -----------------------------
def busca_binaria(lista, nome):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio]["nome"] == nome:
            return lista[meio]
        elif lista[meio]["nome"] < nome:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None

# -----------------------------
# MERGE SORT
# -----------------------------
def merge_sort(lista, chave):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda, chave)
        merge_sort(direita, chave)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i][chave] < direita[j][chave]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
    return lista

# -----------------------------
# QUICK SORT
# -----------------------------
def quick_sort(lista, chave):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x[chave] <= pivo[chave]]
        maiores = [x for x in lista[1:] if x[chave] > pivo[chave]]
        return quick_sort(menores, chave) + [pivo] + quick_sort(maiores, chave)

# -----------------------------
# Demonstração
# -----------------------------
if __name__ == "__main__":
    print("📦 Insumos simulados:")
    for insumo in insumos:
        print(insumo)

    # FILA
    fila = Fila()
    for insumo in insumos:
        fila.enfileirar(insumo)
    print("\n📋 Fila (ordem cronológica):", fila.mostrar())

    # PILHA
    pilha = Pilha()
    for insumo in insumos:
        pilha.empilhar(insumo)
    print("\n📋 Pilha (últimos consumos primeiro):", pilha.mostrar())

    # BUSCAS
    print("\n🔎 Busca Sequencial por 'Reagente B':", busca_sequencial(insumos, "Reagente B"))

    # Ordenar insumos por nome antes da busca binária
    insumos_ordenados = sorted(insumos, key=lambda x: x["nome"])
    print("🔎 Busca Binária por 'Descartável X':", busca_binaria(insumos_ordenados, "Descartável X"))

    # ORDENAÇÃO
    print("\n📊 Merge Sort por quantidade:", merge_sort(insumos.copy(), "quantidade"))
    print("📊 Quick Sort por validade:", quick_sort(insumos.copy(), "validade"))
