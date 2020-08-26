# Transformacao de Imagens

### Requisitos
Para executar o projeto será necessário instalar:
- [Python 3](https://www.python.org/download/releases/3.0/)
- [OpenCV](https://opencv.org/releases/)
- [Numpy](https://numpy.org/install/)

### Build
Para executar o projeto, utilize o comando:
```shell
python3 main.py -i imagem_entrada -t operação -m tamanho_mascara
```
**imagem_entrada** é a imagem de entrada no formato png

**tamanho_mascara** é o tamanho da máscara utilizada na operação [3, 5, 7, 9, ...]

**operação** é o número da operação a ser executada:
- 1 para equalizar o histograma
- 2 para calcular o filtro da média
- 3 para calcular o filtro da mediana
- 4 para calcular o filtro gaussiano 

