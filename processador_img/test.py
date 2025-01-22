import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from processador_img.utils import load_image
from processador_img.processando import combine_images, transform_image_by_color
import matplotlib.pyplot as plt

# Carregar as imagens 
image1 = load_image("processador_img/floresta.jpg")
image2 = load_image("processador_img/roxo.jpg")

# Chamar a função de combinação de imagens
combined_image = combine_images(image1, image2)

# Chamar a função de transformação de cores
transformed_image = transform_image_by_color(image1, image2)

# Agora você pode ver o resultado das funções. Exemplo de exibição:
plt.figure(figsize=(10, 5))

# Exibindo a imagem combinada
plt.subplot(1, 2, 1)
plt.imshow(combined_image)
plt.title("Imagem Combinada")
plt.axis('off')

# Exibindo a imagem transformada
plt.subplot(1, 2, 2)
plt.imshow(transformed_image)
plt.title("Imagem Transformada")
plt.axis('off')

plt.show()
