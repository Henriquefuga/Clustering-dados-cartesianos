# Clusterização de Pontos com Algoritmos Gulosos 

Este projeto aplica os algoritmos gulosos de Prim e Kruskal 
        para realizar a clusterização de pontos cartesianos, dividindo-os em k grupos 
        de maneira eficiente. Além de apresentar os agrupamentos no terminal, o programa gera uma 
        interface gráfica que facilita a visualização dos resultados.

<br>

## 📚 Tecnologias Utilizadas:
<img align="left" title="Python" alt="Python" height="37.5" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg">
<img align="left" title="NumPy" alt="NumPy" height="37.5" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg">

<br><br>

## 🔧 Como Executar:
### Clonar o Repositório:
1. Clone este repositório em sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/algoritmo-clusterizacao.git
   cd algoritmo-clusterizacao
2. Instale as bibliotecas necessárias:
   ```bash
     pip install numpy matplotlib
3. Execute o programa principal:
   ```bash
   python main.py

## 📝 Descrição do Projeto:
Este projeto implementa dois algoritmos clássicos de estratégias gulosas:

Prim: Constrói uma Árvore Geradora Mínima (MST) adicionando sempre a aresta de menor custo a partir de um nó inicial.

Kruskal: Constrói a MST conectando as arestas de menor custo, evitando ciclos.
O objetivo é dividir um conjunto de pontos cartesianos em k grupos, minimizando as distâncias internas de cada grupo. A visualização dos resultados é feita por uma interface gráfica para facilitar a interpretação.

## 🎯 Funcionalidades:
Leitura de pontos: Carrega coordenadas de um arquivo .txt.
Dois métodos de clusterização: Prim e Kruskal.
Interface gráfica interativa: Exibe os agrupamentos formados de maneira visual, utilizando diferentes cores para cada grupo.
Flexibilidade no número de grupos: O usuário pode definir o valor de k para ajustar o número de clusters desejados.

## 📄 Informações Adicionais
Este projeto faz parte de um trabalho acadêmico detalhado que inclui:

Análise assintótica dos algoritmos implementados.
Discussão sobre as estratégias gulosas e sua aplicação na clusterização.
Comparação entre os resultados de Prim e Kruskal para o problema proposto.

## O documento completo do trabalho, com todas as informações e análises, está disponível no arquivo PDF incluído no repositório.

## ✍️ Autores:
Henrique Fuga Gomes

Rafael Bernardes
