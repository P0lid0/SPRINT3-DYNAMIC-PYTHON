# :gráfico_de_barras: Dynamic Programming — Controle de Insumos 
Este projeto simula o **consumo diário de insumos** (reagentes e descartáveis) em unidades de diagnóstico e demonstra, de forma didática, o uso de **estruturas de dados** e **algoritmos clássicos** em Python: 
Fila 
Pilha 
Buscas (Sequencial e Binária) 
Ordenações (Merge Sort e Quick Sort) 
---
## :dardo_no_alvo: Contexto
O consumo diário de insumos nem sempre é registrado com precisão, o que dificulta o controle de estoque e a previsão de reposição. 
Neste projeto, os dados são organizados e consultados utilizando diferentes algoritmos, permitindo observar trade-offs de desempenho e aplicabilidade. 
---
## :tecnólogo_neutro: Objetivos de Aprendizagem
Modelar o consumo em **ordem cronológica** (Fila) e em **ordem inversa** (Pilha). 
Comparar **busca sequencial** e **busca binária**. 
Implementar e analisar **Merge Sort** (estável) e **Quick Sort** (rápido na prática). 
Relacionar a **complexidade de tempo e espaço** aos cenários do problema. 
---
## :pasta_aberta: Estrutura do Projeto
```
/dynamic_programming_project
├── main.py   # Código principal com simulação, Fila, Pilha, Buscas e Ordenações
└── README.md # Documentação
```
---
## :engrenagem: Dependências
Python **3.10+** 
Nenhuma biblioteca externa é utilizada 
---
## :seta_para_frente: Como Executar
### (Opcional) Criar ambiente virtual
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```
### Rodar a simulação
```bash
python main.py
```
Por padrão, os dados são aleatórios a cada execução. Para reprodutibilidade: 
```python
import random
random.seed(42)
```
---
## :tubo_de_ensaio: Estruturas e Algoritmos Implementados
### :sentido_anti_horário: Fila (Queue) 
Classe: `Fila` 
Operações: `enfileirar`, `desenfileirar`, `vazia`, `mostrar` 
Uso: registra consumos em ordem cronológica. 
### :giro_180_sentido_horário: Pilha (Stack) 
Classe: `Pilha` 
Operações: `empilhar`, `desempilhar`, `vazia`, `mostrar` 
Uso: consulta consumos mais recentes primeiro. 
### :lupa_direita: Buscas 
**Sequencial**: funciona em qualquer lista (`O(n)`). 
**Binária**: exige lista ordenada (`O(log n)`). 
### :folhas_marcadas: Ordenações 
**Merge Sort**: estável, `O(n log n)` tempo, `O(n)` espaço. 
**Quick Sort**: rápido na prática, mas pode chegar a `O(n²)` no pior caso. 
---
## :anotações: Exemplo de Saída
```
:pacote: Insumos simulados:
{'nome': 'Reagente A', 'quantidade': 23, 'validade': 78}
:prancheta: Fila (cronológica): [ ... ]
:prancheta: Pilha (inversa): [ ... ]
:lupa_direita: Busca Sequencial por 'Reagente B':
{'nome': 'Reagente B', 'quantidade': 12, 'validade': 45}
:lupa_direita: Busca Binária por 'Descartável X':
{'nome': 'Descartável X', 'quantidade': 34, 'validade': 22}
:gráfico_de_barras: Merge Sort por quantidade: [ ... ]
:gráfico_de_barras: Quick Sort por validade: [ ... ]
```
---
## :gráfico_tendência_subindo: Complexidade — Resumo Rápido
| Estrutura/Algoritmo | Melhor | Médio | Pior | Espaço | Observações |
|----------------------|--------|-------|------|--------|-------------|
| Fila (list + pop(0)) | O(1)   | O(n)  | O(n) | O(1)   | `deque` seria mais eficiente |
| Pilha (list)         | O(1)   | O(1)  | O(1) | O(1)   | `append`/`pop` no final |
| Busca Sequencial     | O(1)   | O(n)  | O(n) | O(1)   | Sem ordenação prévia |
| Busca Binária        | O(1)   | O(log n) | O(log n) | O(1) | Requer lista ordenada |
| Merge Sort           | O(n log n) | O(n log n) | O(n log n) | O(n) | Estável |
| Quick Sort           | O(n log n) | O(n log n) | O(n²) | O(log n) | Não estável |
---
## :foguete: Extensões Sugeridas
Substituir `list` por `deque` na Fila. 
Persistir dados em **CSV/JSON**. 
Implementar alerta para insumos com validade ≤ 7 dias. 
Explorar **programação dinâmica** para otimização de reposição (variação da Mochila 0/1). 
---
## :pergaminho: Licença
Projeto de caráter **didático**. Livre para uso acadêmico e adaptações.











Anote algo









