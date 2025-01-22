import numpy as np
from PIL import Image

def combine_images(*images):
    """
    Combina várias imagens em uma única imagem.
    Aqui, usamos a MÉDIA dos valores de pixels para combinar as imagens.
    As imagens devem ter o mesmo tamanho.
    """
    # Verifica se todas as imagens têm o mesmo tamanho
    sizes = [img.size for img in images]
    if len(set(sizes)) != 1:
        raise ValueError("Todas as imagens devem ter o mesmo tamanho! Por favor, tente novamente.")

    # Converte as imagens 
    images_arrays = [np.array(img) for img in images]

    # Calcula a média 
    combined_array = np.mean(images_arrays, axis=0).astype(np.uint8)

    # Converte o array de volta para uma imagem
    combined_image = Image.fromarray(combined_array)
    return combined_image
