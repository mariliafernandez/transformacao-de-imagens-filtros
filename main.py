import argparse
import numpy as np
import cv2 as cv
import sys

def calcula_probabilidade(hist):
    prob = np.zeros( len(hist) )
    prob = hist/np.sum(hist)
    return prob

def dist_acumulada(prob):
    dist = np.zeros( len(prob) )
    for i in range( len(prob) ):
        dist[i] = np.sum( prob[0:i+1] )
    return dist

def equaliza_histograma(img):
    n_pixels = np.zeros(256)
    n_min = np.min(img)
    n_max = np.max(img)
    for i in range(n_min, n_max+1):
        n_pixels[i] = np.sum( img == i )
    p = calcula_probabilidade(n_pixels)
    d = dist_acumulada(p)
    new_values = np.round(d * (len(d)-1) )
    for i in range( len(new_values) ):
        img[img == i] = new_values[i]
    return img

# Interpreta os argumentos passados via terminal
parser = argparse.ArgumentParser()
parser.add_argument('-t', help='option [1, 2, 3, 4]', type=int)
parser.add_argument('-m', help='mask [3, 5]', type=int)
parser.add_argument('-i', help='image in png format')
args = parser.parse_args()
option = args.t
image = args.i

# Abre a imagem em escala de cinza
img_file = cv.imread(image)
if img_file is None : 
    print('Não foi possível ler a imagem.')
    sys.exit(0)
else: 
    # Converte as cores originais da imagem para tons de cinza e salva a nova imagem em arquivo
    gray = cv.cvtColor(img_file, cv.COLOR_BGR2GRAY)
    cv.imwrite('input_tons_de_cinza.png', gray)

    if option == 1:
        result = equaliza_histograma(gray)
    # elif option == 2:

    cv.imshow('Result', result)
    cv.waitKey(0)

# hist={0:1314, 1:3837, 2:5820, 3:4110, 4:2374, 5:921, 6:629, 7:516}
# hist=np.array([ 1314, 3837, 5820, 4110, 2374, 921, 629, 516 ])