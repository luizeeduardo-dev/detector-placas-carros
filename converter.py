import numpy as np
from PIL import Image

def convolucao(imagem, filtro):
    altura, largura = imagem.shape
    f_altura, f_largura = filtro.shape
    h_pad = f_altura // 2
    w_pad = f_largura // 2 
    imagem_pad = np.pad(imagem, ((h_pad, h_pad), (w_pad, w_pad)), mode='constant')
    resultado = np.zeros((altura, largura))

    for i in range(altura):
        for j in range(largura):
            resultado[i, j] = np.sum(imagem_pad[i:i+f_altura, j:j+f_largura] * filtro)

    return resultado

def converter_para_escala_cinza(imagem_entrada):
    largura, altura = imagem_entrada.size

    if imagem_entrada.mode != 'RGB':
        raise ValueError("A imagem de entrada deve ser em modo RGB")

    imagem_cinza = Image.new('L', (largura, altura))

    for y in range(altura):
        for x in range(largura):
            cor = imagem_entrada.getpixel((x, y)) 
            valor_cinza = int(0.299 * cor[0] + 0.587 * cor[1] + 0.114 * cor[2]) # atribui a escala de cinza a cada pixel
            imagem_cinza.putpixel((x, y), valor_cinza)                          #    multiplicando pelo peso correspondente

    return imagem_cinza

