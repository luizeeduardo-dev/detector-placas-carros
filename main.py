from PIL import Image
import matplotlib.pyplot as plt

import sobel
import extrair
import converter
import histogramas

imagem = Image.open("resources/placa_veiculo.jpg")

# conversão para escala de conza
imagem_cinza = converter.converter_para_escala_cinza(imagem)

# equalizar histograma 
imagem_equalizada = histogramas.equalizar_histograma(imagem_cinza)

# realce de bordas 
bordas_realcadas = sobel.realcar_bordas(imagem_equalizada)

# Definiçã da imagem em pb
imagem_limiarizada = histogramas.limiarizacao_global(imagem, limiar=64)

# conversão da imagem em texto 
text = extrair.extrairTextoDaPlaca(imagem_limiarizada)
print("Placa do veiculo: ", text)

plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(imagem_equalizada, cmap='gray')
plt.title('Imagem Equalizada')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(bordas_realcadas, cmap='gray')
plt.title('Bordas Realçadas')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(imagem_limiarizada, cmap='gray')
plt.title('Imagem Limiarizada')
plt.axis('off')


plt.text(0.5, 0.5, "Placa do veiculo:\n"+text, color='black', fontsize=12, ha='center', va='center', transform=plt.gcf().transFigure)

plt.tight_layout()
plt.show()
