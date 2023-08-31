import sys
from tablero import Tablero
from pieza_explosiva import PiezaExplosiva
from imprimir_tablero import imprimir_tablero

if __name__ == "__main__":
    args_por_cons = sys.argv
    tablero_encontrado = False
    acceso = False
    usuario = args_por_cons[1]
    nombre_tablero = args_por_cons[2]
    with open('tableros.txt', 'r') as tableros_txt:
            data = tableros_txt.readlines()
            data_nuevo = []
            for n in range(len(data)):
                elemento = data[n].strip().split(',')
                data_nuevo.append(elemento)
            for elemento in data_nuevo:
                if nombre_tablero in elemento:
                    tablero_encontrado = True
    if len(usuario) >= 4 and usuario.isalpha() and tablero_encontrado == True:
        acceso = True
    elif (len(usuario) < 4 or usuario.isalpha() == False) and tablero_encontrado == True:
        print('El Usuario debe tener mínimo 4 caracteres y ser sólo letras del alfabeto')
    elif len(usuario) >= 4 and usuario.isalpha() and tablero_encontrado == False:
         print('No premiamos la creatividad, no inventes tableros. Selecciona uno que exista'
               ' por favor')
    elif (len(usuario) < 4 or usuario.isalpha() == False) and tablero_encontrado == False:
         print('Me entregaste el Usuario y el tablero mal :/')
    if acceso == True:
        tablero_a_usar = Tablero([[], []])
        tablero_a_usar.reemplazar(nombre_tablero)
        print(f'\nBienvenido/a querido/a {usuario}')
        print()
        print('------- Menú de opciones -------')
        print()
        print('(1) Mostrar tablero\n(2) Limpiar tablero\n(3) Solucionar tablero'
              '\n(4) Salir del programa\n')
        opcion = input('>> ¿Qué deseas hacer?: ')
        while opcion != '4':
            if opcion == '1':
                print()
                imprimir_tablero(tablero_a_usar.tablero)
            elif opcion == '2':
                tablero_a_usar.limpiar()
            elif opcion == '3':
                pass
            elif opcion == '4':
                pass
            else:
                print('\nLiteralmente es elegir un numero del 1 al 4, que decepcionante...\n')
            opcion = input('>> ¿Qué deseas hacer ahora?: ')