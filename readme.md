## Calculando a menor quantidade de rotas aéras para atender a maior demanda

### Calculado a partide de árvore geradora máxima usando o algoritmo de Kruskal

### Requisitos:

- Python3
- Pip3 

### Instalando Bibliotecas

`pip3 install -r requirements.txt`

## Como usar

O programa usa como entrada grafos gerados no site...

### Executando algoritmo para um arquivo específico

Para serem executados os arquivos devem estar dentro da 
pasta __./test_cases__.

Execute:

`python3 calculate_routes.py <file_name>.txt`

Ao ser executado o arquivo com o grado resultante será salvo com o mesmo nome no diretório __./results__.

### Executando algoritmo para todos os arquivos

Execute:

`python3 calculate_routes.py --all`

Após todos os casos de teste terem sido executados é possível achar um gráfico de linha com os tempos de execução para cada caso de teste em __./stats__

### Validando resultados

Não encontrei ferramenta para calcular árvore geradora máxima usando o algoritmo de Kruskal. Então, de modo a poder validar o resultado do programa, criei um script para converter os casos de teste para um problema de árvore geradora mínima e então poder ser executado no site descrito. 

Para converter um caso de teste específico execute:

`python3 convert_test_cases.py <file_name>.txt`

Para converter todos os casos de teste, execute:

`python3 convert_test_cases.py --all`

Os arquivos convertidos podem ser achados em __./converted_test_cases__.


