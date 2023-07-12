# importe a biblioteca opencv
import cv2
import numpy as np

import tensorflow as tf

#Carregue o modelo


# defina um objeto de captura de vídeo
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture o vídeo quadro a quadro
    check, frame = vid.read()

    #Redimensione a imagem
    

    #Converta a imagem em um array Numpy e aumente a dimensão
    

    #Normalize a imagem
   

    #Preveja resultado
    prediction = model.predict(normalised_image)
    print("Previsão: ", prediction)
  
    # Exiba o quadro resultante
    cv2.imshow('quadro', frame)
      
    # Saia da tela com a barra de espaço
    key = cv2.waitKey(1)
    
    if key == 32: 
        print("Fechando")
        break
  
# Após o loop, libere o objeto capturado
vid.release()

# Destrua todas as janelas
cv2.destroyAllWindows()
