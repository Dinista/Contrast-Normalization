import numpy as np
import os
import sys 
import cv2
from os import walk
from skimage.filters.rank import maximum, minimum


# Le as imagens presentes no diretorio raiz, e carrega a escolhida.
# Após isso seleciona o tamanho da máscara que será utilizada.

def select_img():
    print("===========================================")
    print("Digite o número correspondente a imagem que deseja carregar:\n")
    filenames = next(walk(os.path.dirname(__file__) + "/"), (None, None, []))[2]
    files = [ file for file in filenames if file.endswith((".jpg", ".JPG", ".PNG", ".png", ".tif", ".tiff", ".TIF")) ]
    
    if len(files) == 0:
        print("Não existe arquivos de imagem no diretório raiz.")
        sys.exit()
    
    for i in range(0, len(files)):
        print('[{}] {}'.format(i, files[i]))
    index = input()
    
    while not index.isdigit() or int(index) >= len(files) or int(index) < 0:
        print("\nEsta opção não existe, digite novamente.")
        index = input()
    
    imagem = cv2.imread(os.path.dirname(__file__) + "/" + files[int(index)], cv2.IMREAD_GRAYSCALE)
    
    print("\nDigite o tamanho da máscara que deseja utilizar:")
    mask_size = input()    
    
    while(not mask_size.isdigit()):
        print("\nValor inválido! Digite novamente:")
        mask_size = input()

    return imagem, int(mask_size), files[int(index)]
    

# Aplica a normalização

def normalizacao(img, mask_size):
    size = mask_size
    max = maximum(img, np.ones((size, size)))
    min = minimum(img, np.ones((size, size)))
    a = img - min
    b = max - min
    np.seterr(invalid ='ignore')
    result = np.true_divide(a, b) * 255
    return result
    


def main():
    imagem, mask_size, nome_arq = select_img()
    img_normalized = normalizacao(imagem, mask_size)
    print("\nFeche as janelas para continuar...")
    cv2.imshow('Imagem cinza', imagem)
    cv2.imshow('Imagem normalizada', img_normalized)
    cv2.waitKey(0)
    print("\nGostaria de salvar a imagem normalizada?\n[1] Sim\n[2] Não")
    op = input()
    while op != '1' or op != '2':
        if op == '2' or op == '1': break
        print("\nEsta opção não existe, tente novamente.")
        op = input()
    
    #salvando a imagem
    
    if op == '1':
        aux = nome_arq.split(".")
        cv2.imwrite(os.path.dirname(__file__) + "/" + str(mask_size) +"_"+ aux[0] +'.jpg', img_normalized)
        print("\nSalvo em:\n" + os.path.dirname(__file__))
    
    print("\nPrograma encerrado.")
if __name__ == "__main__":
    main()
