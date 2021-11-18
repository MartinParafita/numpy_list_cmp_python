# Numpy [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Black jack! [o algo parecido :)]

El objetivo es realizar una aproximación al juego de black jack,
el objetivo es generar una lista de 2 números aleatorios
entre 1 al 10 inclusive, y mostrar los "números" al usuario.

El usuario debe indicar al sistema si desea sacar más
números para sumarlo a la lista o no sacar más

A medida que el usuario vaya sacando números aleatorios que se suman
a su lista se debe ir mostrando en pantalla la suma total
de los números hasta el momento.

Cuando el usuario no desee sacar más números o cuando el usuario
haya superado los 21 (como la suma de todos) se termina la jugada
y se presenta el resultado en pantalla

BONUS Track: Realizar las modificaciones necesarias para que jueguen
dos jugadores y compitan para ver quien sacá la suma de números
más cercanos a 21 sin pasarse!
'''

import random

import numpy as np


if __name__ == '__main__':
    print("Ahora sí! buena suerte :)")
    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda

    jugador_1 = [random.randint(1,10) for x in range(2)]
    print('Las cartas del jugador 1 son: ',jugador_1)

    jugador_2 = [random.randint(1,10) for x in range(2)]
    print('Las cartas del jugador 2 son: ',jugador_2)

    suma1 = np.sum(jugador_1)
    print('Tenes', suma1)
    if suma1 < 21:
        while suma1 <= 21:
            carta1 = int(input('Queres otra carta? 1) Si. 2) No \n'))
        
        
            if carta1 == 1:
                otra_carta = [random.randint(1,10)]
                jugador_1 += otra_carta
                suma1 = np.sum(jugador_1)
                print('Ahora tus cartas son: ',jugador_1, 'un total de: ',suma1)
            else:    
                print('Jugador 1 se planta con: ',suma1)
                break
    elif suma1 == 21:
        print('BLACK JACK!')
    else:
        print('Perdiste')
    
    suma2 = np.sum(jugador_2)
    print('Tenes', suma2)
    if suma2 < 21:
        while suma2 < 21:
            carta2 = int(input('Queres otra carta? 1) Si. 2) No \n'))
        
        
            if carta2 == 1:
                otra_carta2 = [random.randint(1,10)]
                jugador_2 += otra_carta2
                suma2 = np.sum(jugador_2)
                print('Ahora tus cartas son: ',jugador_2, 'un total de: ',suma2)
            else:    
                print('Jugador 2 se planta con: ',suma2)
                break
    elif suma2 == 21:
        print('BLACK JACK!')
    else:
        print('Perdiste')

    if suma1 > suma2 and suma1 <= 21:
        print('Gano el jugador 1')
    elif suma2 > suma1 and suma2 <= 21:
        print('Gano el jugador 2')
    
    print("terminamos")