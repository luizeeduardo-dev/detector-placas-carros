from PIL import Image
import numpy as np
import converter

def calcular_histograma(imagem, num_bins=256):  # Basicamente calcula a distribuição de pixels por toda a imagem
    imagem_array = np.array(imagem)
    histograma = np.zeros(num_bins, dtype=np.int32)
    for pixel in imagem_array.flatten():
        histograma[pixel] += 1 
    return histograma

# Calcular o histograma normalizado
def equalizar_histograma(imagem):
    histograma = calcular_histograma(imagem)
    imagem_array = np.array(imagem) 
    num_pixels = imagem_array.size
    hist_normalizado = histograma / num_pixels
    cdf = cumsum(hist_normalizado)
    cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min()) # faz a normalização para valores do CDF entre 0 e 255
    imagem_equalizada = cdf_normalized[imagem_array.flatten()].reshape(imagem_array.shape)
    return imagem_equalizada.astype(np.uint8)


def limiarizacao_global(imagem, limiar):
    imagem_array = np.array(imagem)

    # Converter para escala de cinza caso não seja
    if len(imagem_array.shape) > 2:
        imagem_pil = Image.fromarray(imagem_array)
        imagem_cinza_pil = converter.converter_para_escala_cinza(imagem_pil)  
        imagem_array = np.array(imagem_cinza_pil)  

    altura, largura = imagem_array.shape
    imagem_limiarizada = np.zeros_like(imagem_array)

    for i in range(altura):
        for j in range(largura):
            if imagem_array[i, j] >= limiar:
                imagem_limiarizada[i, j] = 255  # Pixel branco (primeiro plano)
            else:
                imagem_limiarizada[i, j] = 0  # Pixel preto (plano de fundo)

    return imagem_limiarizada

def cumsum(array): #soma cumulariva
    cumulative_sum = []
    current_sum = 0
    for element in array:
        current_sum += element
        cumulative_sum.append(current_sum)
    return np.array(cumulative_sum)

