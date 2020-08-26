import argparse
import numpy as np
import cv2 as cv
import sys
from transform import *

# Interpreta os argumentos passados via terminal
parser = argparse.ArgumentParser()
parser.add_argument('-m', help='mask, m x m [3, 5, 7, 9, ...]', type=int)
parser.add_argument('-i', help='image in png format')
parser.add_argument('-t', help='operation number [1, 2, 3, 4]', type=int)

args = parser.parse_args()
image = args.i
m = args.m
op = args.t

# Abre a imagem em escala de cinza
img_file = cv.imread(image)
if img_file is None : 
    print('Não foi possível ler a imagem.')
    sys.exit(0)
else: 
    # Converte as cores originais da imagem para tons de cinza e salva a nova imagem em arquivo
    gray = cv.cvtColor(img_file, cv.COLOR_BGR2GRAY)
    
    if op == 1:
        # Equalização do histograma
        print('\nCalculando equalização do histograma...')
        eq = equaliza_histograma(gray.copy())
        nova_imagem('equalizacao', eq)

    elif op == 2:
        # Filtro da média
        print('\nCalculando filtro da média...')
        mask = np.ones([m, m])
        mean = convolucao(gray.copy(),mask,'mean')
        nova_imagem('media', mean)
    
    elif op == 3:
        # Filtro da mediana 
        print('\nCalculando filtro da mediana...')
        mask = np.ones([m,m])
        median = convolucao(gray.copy(), mask, 'median')
        nova_imagem('median', median)

    elif op == 4:
        # Filtro Gaussiano
        print('\nCalculando filtro gaussiano...')
        mask_1d = pascal_coef(m)
        mask_1d.shape=[m,1]
        mask = np.matmul(mask_1d, mask_1d.T)
        print('\nMáscara:')
        print(mask)
        gauss = convolucao(gray.copy(), mask, 'gaussian')
        nova_imagem('gaussian', gauss)

    else:
        print('Operação inválida.')
        sys.exit(0)
    