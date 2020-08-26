import numpy as np
import cv2 as cv

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

# Mostra o resultado e salva a imagem na pasta
def nova_imagem(title, img):
    cv.imwrite( 'output-'+ title + '.png', img )
    cv.imshow(title, img/256 )
    print('Pressione qualquer tecla para finalizar')
    cv.waitKey(0)

# Retorna a linha do triangulo de Pascal de tamanho=n_coef
def pascal_coef(n_coef):
    coefs = np.ones(n_coef)
    if n_coef == 1: return coefs
    else:
        prev_row = pascal_coef(n_coef-1)
        for i in range( len(prev_row)-1 ):
            coefs[i+1] = (prev_row[i] + prev_row[i+1])
    return coefs

def convolucao(img, M, option):
    img2 = np.ones(img.shape)
    row = img.shape[0]
    col = img.shape[1]
    M_sum = np.sum(M)
    sample = np.ones(M.shape)

    for x in range(row):
        for y in range(col):
            x1 = int(M.shape[0]/2)
            x2 = int(M.shape[0]/2)
            y1 = int(M.shape[1]/2)
            y2 = int(M.shape[1]/2)

            # Se o pixel estiver localizado na borda da imagem altera a dimensão da máscara
            if x - x1 < 0: 
                x1 = x
            elif x + x2 > row-1: 
                x2 = row-1-x
            if y - y1 < 0: 
                y1 = y
            elif y + y2 > col-1:
                y2 = col-1-y

            # Região de interesse contendo os pixels vizinhos 
            sample = img[ x-x1:x+x2, y-y1:y+y2 ]
            meio = int(M.shape[0]/2)
            M_sample = M[ meio-x1:meio+x2, meio-y1:meio+y2]

            if option == 'mean' or option == 'gaussian':
                # Multiplica a região pela máscara, pixel a pixel, calcula a média e atribui ao pixel correspondente
                img2[x,y] = np.sum( sample * M_sample )/ np.sum(M_sample)

            elif option == 'median':
                # Calcula a mediana da região e atribui ao pixel correspondente
                img2[x,y] = np.median( sample )

    return np.rint(img2)