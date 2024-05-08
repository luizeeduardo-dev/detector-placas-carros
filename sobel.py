import numpy as np
import converter

# Filtro de realce de bordas (Sobel)
def realcar_bordas(imagem):
    filtro_sobel = np.array([[-1, 0, 1],
                             [-2, 0, 2],
                             [-1, 0, 1]])

    bordas = converter.convolucao(imagem, filtro_sobel)  
    bordas = np.abs(bordas)              #valor absoluto 
    bordas = (bordas - np.min(bordas)) * 255 / (np.max(bordas) - np.min(bordas))

    return bordas.astype(np.uint8)  # garante que sera truncado sinal de 8 bits