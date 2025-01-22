import matplotlib.pyplot as plt

def plot_image(image):
    """
    Exibe uma única imagem.
    """
    plt.figure(figsize=(12, 4))
    plt.imshow(image)
    plt.axis('off')
    plt.show()

def plot_result(*args):
    """
    Exibe múltiplas imagens, lado a lado.
    """
    number_images = len(args)
    fig, ax = plt.subplots(1, number_images, figsize=(12, 4))
    for i, image in enumerate(args):
        ax[i].imshow(image)
        ax[i].axis('off')
    plt.show()
