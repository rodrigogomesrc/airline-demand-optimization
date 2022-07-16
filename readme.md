## Calculando a menor quantidade de rotas aéras para atender a maior demanda

### Calculado a partide de árvore geradora máxima usando o algoritmo de Kruskal

### Requisitos:

- Python3
- Pip3 (somente caso necessite instalar as bibliotecas adicionais, o que é opcional)

### Instalando Bibliotecas

(opcional para instalar bibliotecas opicionais para gerar gráfico com tempos de execução)

`pip3 install -r requirements.txt`

## Como usar

O programa usa como entrada grafos gerados [nesse site](https://algorithms.discrete.ma.tum.de/graph-algorithms/mst-kruskal/index_en.html). Ao criar um grafo de teste no site, baixe o arquivo e coloque na pasta __./test_cases__

### Executando algoritmo para um arquivo específico

Execute:

`python3 calculate_routes.py <file_name>.txt`

Ao ser executado o arquivo com o grafo resultante será salvo com o mesmo nome no diretório __./results__.

Um relatório de execução é gerado e salvo com o nome do arquivo na pasta __./stats__.

### Executando algoritmo para todos os arquivos

Execute:

`python3 calculate_routes.py --all`

Após a execução terminar, todos os resultados serão salvos na pasta de resultados. Um relatório de execução também pode ser encontrado na pasta __./stats__ com o tempo de execução de todos os casos de teste.

### Gerando gráfico com tempos de execução (opcional)

Execute:

`python3 calculate_routes.py --all --chart`

Após a execução, além do relatório de execução gerado anteriormente, um gráfico de linhas será gerado na pasta __./stats__. com os tempos de execução para cada caso de teste.

### Validando resultados

Não encontrei ferramenta para calcular árvore geradora máxima usando o algoritmo de Kruskal. Então, de modo a poder validar o resultado do programa, criei um script para converter os casos de teste para um problema de árvore geradora mínima e então poder ser executado no site descrito. 

Para converter um caso de teste específico execute:

`python3 convert_test_cases.py <file_name>.txt`

Para converter todos os casos de teste, execute:

`python3 convert_test_cases.py --all`

Os arquivos convertidos podem ser achados em __./converted_test_cases__.

Para validar os resultados usando o site basta fazer o upload dos arquivos convertidos e rodar o algoritmo de Kruskal do site. Ao fazer o upload dos resultados calculados pelo programa e salvos na pasta __./results__ e comparar ao resultado obtido ao executar no site os casos de teste convertido é possível notar que as arestas destacadas serão as únicas permanecentes no arquivo do resultado.


