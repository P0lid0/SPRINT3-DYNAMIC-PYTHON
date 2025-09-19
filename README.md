Dynamic Programming — Controle de Insumos (Fila, Pilha, Buscas e Ordenações em Python)

Este projeto simula o consumo diário de insumos (reagentes e descartáveis) em unidades de diagnóstico e demonstra, de forma didática, o uso de estruturas de dados e algoritmos clássicos: Fila, Pilha, Buscas (Sequencial e Binária) e Ordenações (Merge Sort e Quick Sort).

Contexto: o consumo diário não é registrado com precisão, dificultando controle de estoque e previsão de reposição. Aqui, organizamos os dados e aplicamos algoritmos para consultar e ordenar os registros de consumo.

Objetivos de Aprendizagem

Modelar o consumo diário em ordem cronológica (Fila) e consulta inversa (Pilha).

Comparar busca sequencial e busca binária (pré-requisito: dados ordenados).

Implementar e entender Merge Sort (estável) e Quick Sort (rápido na prática).

Relacionar complexidade de tempo e espaço aos cenários do problema.

Estrutura do Projeto
/dynamic_programming_project
  ├── main.py     # Código completo com simulação, Fila, Pilha, Buscas e Ordenações
  └── README.md   # Este documento


Dependências: somente Python 3.10+ (sem bibliotecas externas).

Como Executar

(Opcional) Criar ambiente virtual

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate


Executar

python main.py


Os dados são aleatórios a cada execução. Para reprodutibilidade, você pode definir a semente no início do arquivo:
import random; random.seed(42)

Simulação dos Dados

Cada insumo é um dicionário com três campos:

{
  "nome": "Reagente A",      # identificação
  "quantidade": 17,          # quantidade consumida no dia
  "validade": 63             # dias restantes até vencer
}


A lista inicial (em main.py) é gerada com nomes fixos e valores aleatórios de quantidade e validade para simular diferentes cenários.

O que está implementado
Fila (Queue) — consumo diário em ordem cronológica

Classe: Fila

Operações: enfileirar(item), desenfileirar(), vazia(), mostrar()

Uso no contexto: registra os consumos na ordem que ocorrem, viabilizando processamento diário (o primeiro consumo registrado é o primeiro processado).

Complexidade:

append em lista: O(1) amortizado

pop(0) em lista: O(n) (cópia interna dos elementos)

Observação/Trade-off: para produção, use collections.deque (desenfileirar em O(1)). Mantivemos list por didática.

Pilha (Stack) — consulta inversa (últimos consumos primeiro)

Classe: Pilha

Operações: empilhar(item), desempilhar(), vazia(), mostrar()

Uso no contexto: inspecionar os consumos mais recentes primeiro (auditoria/checagem rápida do que aconteceu por último).

Complexidade: append/pop no final da lista são O(1) amortizado.

Buscas
Busca Sequencial

Função: busca_sequencial(lista, nome)

Cenário: lista não precisa estar ordenada.

Complexidade:

Melhor caso: O(1) (primeiro elemento).

Pior/Médio caso: O(n).

Uso no contexto: útil quando a lista é pequena ou quando não vale a pena ordenar antes.

Busca Binária

Função: busca_binaria(lista, nome)

Pré-requisito: lista ordenada por nome (ex.: sorted(insumos, key=lambda x: x["nome"])).

Complexidade: O(log n) comparações; espaço O(1).

Uso no contexto: ideal para procurar insumos por nome quando os registros já estão ordenados (consultas frequentes).

Ordenações
Merge Sort

Função: merge_sort(lista, chave)

Propriedades: estável (preserva ordem relativa de itens com a mesma chave).

Complexidade: O(n log n) tempo; O(n) espaço adicional.

Uso no contexto: ordenar por quantidade (priorizar reabastecimento) ou por validade (priorizar itens que vencem antes) mantendo estabilidade.

Quick Sort

Função: quick_sort(lista, chave)

Propriedades: não estável; pivot escolhido como primeiro elemento (simples e didático).

Complexidade:

Médio: O(n log n)

Pior: O(n²) (dados quase ordenados + pivot ruim)

Espaço: O(log n) devido à recursão

Mitigação (sugestões): pivot aleatório ou median-of-three para reduzir piores casos.

Fluxo Demonstrativo (o que o main.py faz)

Gera a lista de insumos (quantidade e validade aleatórias).

Enfileira todos os insumos (ordem cronológica) e mostra a fila.

Empilha os mesmos insumos e mostra a pilha (consulta inversa).

Busca Sequencial por um nome (ex.: "Reagente B").

Ordena por nome e faz Busca Binária (ex.: "Descartável X").

Ordena por quantidade usando Merge Sort.

Ordena por validade usando Quick Sort.

Exemplo de saída (ilustrativo):

📦 Insumos simulados:
{'nome': 'Reagente A', 'quantidade': 23, 'validade': 78}
...

📋 Fila (ordem cronológica): [ ... ]
📋 Pilha (últimos consumos primeiro): [ ... ]

🔎 Busca Sequencial por 'Reagente B': {'nome': 'Reagente B', 'quantidade': 12, 'validade': 45}
🔎 Busca Binária por 'Descartável X': {'nome': 'Descartável X', 'quantidade': 34, 'validade': 22}

📊 Merge Sort por quantidade: [ ... ordenado crescente por quantidade ... ]
📊 Quick Sort por validade: [ ... ordenado crescente por validade ... ]

Decisões de Projeto & Trade-offs

Lista como Fila/Pilha: simples para aprendizado. Nota: pop(0) é O(n); em produção use deque para O(1).

Registros como dicionários: prático e legível. Em projetos maiores, dataclasses tornam o código mais seguro e claro.

Pivot do Quick Sort: fixo no primeiro elemento para didática; versões robustas usam pivot aleatório/median-of-three.

Ordenar por nome antes da busca binária: pré-condição obrigatória e explicitada no código.

Complexidade — Resumo Rápido
Estrutura/Algoritmo	Melhor	Médio	Pior	Espaço	Observações
Fila (list + pop(0))	O(1)	O(n)	O(n)	O(1)	Use deque p/ O(1) dequeuing
Pilha (list)	O(1)	O(1)	O(1)	O(1)	append/pop no fim
Busca Sequencial	O(1)	O(n)	O(n)	O(1)	Sem ordenação prévia
Busca Binária	O(1)	O(log n)	O(log n)	O(1)	Exige lista ordenada
Merge Sort	—	O(n log n)	O(n log n)	O(n)	Estável
Quick Sort	—	O(n log n)	O(n²)	O(log n)	Não estável
Como cada parte atende aos requisitos da atividade

Fila e Pilha (30 pts): classes Fila e Pilha implementadas e demonstradas no main.py.

Estruturas de Busca (20 pts): busca_sequencial e busca_binaria implementadas; binária com pré-ordenamento por nome.

Ordenação (30 pts): merge_sort (estável) e quick_sort (rápido na prática) implementados e usados para quantidade e validade.

Relatório (20 pts): este README explica como e por quê cada estrutura/algoritmo foi usado no contexto do problema.

Testes Rápidos (checklist)

 Executar python main.py e verificar impressão da Fila e Pilha.

 Confirmar Busca Sequencial retorna um dicionário quando o nome existe; None quando não.

 Ordenar por nome e testar Busca Binária para um item presente e um ausente.

 Verificar listas ordenadas por quantidade (Merge Sort) e por validade (Quick Sort) em ordem crescente.

Extensões Sugeridas (opcional / bônus)

Fila com deque: substituir a implementação para desempenho O(1) em desenfileirar.

Persistência: salvar/ler consumos em CSV/JSON; gerar relatório diário.

Validade crítica: filtrar insumos com validade <= 7 para reposição prioritária.

Programação Dinâmica (bônus acadêmico): modelar um plano de reposição sob orçamento limitado (variação da Mochila 0/1): maximizar cobertura de consumo/criticidade com custo limitado, decidindo quais insumos repor agora.

Estado: dp[i][b] = melhor benefício usando primeiros i insumos com orçamento b.

Transição: dp[i][b] = max(dp[i-1][b], beneficio[i] + dp[i-1][b-custo[i]]) se custo[i] <= b.

Observação: a atividade foca em estruturas e ordenações; a seção de programação dinâmica acima é um extra que conecta o tema da disciplina ao contexto do estoque.

Boas Práticas para a Apresentação

Explique o porquê de cada algoritmo no contexto (ex.: “Fila para manter a cronologia do consumo”, “Pilha para auditoria do mais recente”).

Mostre a diferença prática entre buscas (ordenar antes permite usar binária com O(log n)).

Destaque estabilidade do Merge Sort vs. velocidade média do Quick Sort.

Comente o trade-off do pop(0) e cite deque como otimização.

Licença e Uso Acadêmico

Este projeto é didático. Utilize, cite e adapte conforme as diretrizes da sua instituição.
Contribuições e melhorias são bem-vindas.