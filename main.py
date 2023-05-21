import cv2
import matplotlib.pyplot as plt
import os

def plot_histogram(image):
    # Carrega a imagem usando o OpenCV
    img = cv2.imread(image, 0)

    # Calcula o histograma usando o OpenCV
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    # Plota o histograma
    plt.plot(hist)
    plt.xlabel('Níveis de intensidade')
    plt.ylabel('Número de pixels')
    plt.title('Histograma de Pixels')
    plt.show()


def show_rgb_channels(image):
    # Carrega a imagem usando o OpenCV
    img = cv2.imread(image)

    # Separa as três matrizes de cores (R, G, B)
    b, g, r = cv2.split(img)

    # Cria uma figura com três subplots para exibir as matrizes de cores
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))

    # Exibe a matriz de cores R
    axes[0].imshow(r, cmap='Reds')
    axes[0].set_title('Matriz de Cores R')

    # Exibe a matriz de cores G
    axes[1].imshow(g, cmap='Greens')
    axes[1].set_title('Matriz de Cores G')

    # Exibe a matriz de cores B
    axes[2].imshow(b, cmap='Blues')
    axes[2].set_title('Matriz de Cores B')

    # Ajusta os espaçamentos entre os subplots
    plt.tight_layout()

    # Exibe a figura
    plt.show()


def convert_to_grayscale(image):
    # Carrega a imagem usando o OpenCV
    img = cv2.imread(image)

    # Calcula a nova largura e altura da imagem com base na escala desejada
    width = int(img.shape[1] * 20 / 100)
    height = int(img.shape[0] * 20 / 100)

    # Redimensiona a imagem para a nova escala
    resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

    # Converte a imagem redimensionada para tons de cinza
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    # Retorna a imagem em tons de cinza
    return gray_img


def verify_if_image_exists():
    img_name = input("\nDigite o nome da imagem que será processada: ")

    if not os.path.exists(f'images/{img_name}.jpg'):
        print("A imagem não existe ou o caminho é inválido")
        return verify_if_image_exists()

    return f'images/{img_name}.jpg'


while True:
    option = int(input("\nEscolha a função que deseja executar. Insira o número correspondente:\n\n1 - Histograma dos pixels\n2 - Banda de Cores (RGB)\n3 - Converter para tons de cinza\n4 - Sair\n"))

    if option == 4:
        break

    image_path = verify_if_image_exists()

    if option == 1:
        # Chama a função para plotar o histograma
        plot_histogram(image_path)
    elif option == 2:
        # Chama a função para exibir as matrizes de cores RGB da figura
        show_rgb_channels(image_path)
    elif option == 3:
        # Chama a função que converte a imagem para tons de cinza
        gray_image = convert_to_grayscale(image_path)
        cv2.imshow('Imagem em Tons de Cinza', gray_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Opção inválida!")

exit()