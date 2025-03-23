# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 11:18:08 2024

@author: JexCher
"""

FILAS = 6
COLUMNAS = ['A', 'B']

asientos = {fila: {columna: "LIBRE" for columna in COLUMNAS} for fila in range(1, FILAS + 1)}

while True:
    print("LATAM AIRLINES VUELO LA1440")
    print("LE DA LA BIENVENIDA AL SISTEMA DE RESERVA DE ASIENTOS")
    print("\n1. Reservar un asiento")
    print("2. Mostrar asientos")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        while True:
            try:
                
                nombre = input("Ingrese el nombre del pasajero: ")
                fila = int(input("Ingrese la fila del asiento (1-6): "))
                columna = input("Ingrese la columna del asiento (A-B): ").upper()
                if fila < 1 or fila > FILAS or columna not in COLUMNAS:
                    print("Asiento fuera de rango. Intente nuevamente.")
                    continue
                if asientos[fila][columna] != "LIBRE":
                    print("Asiento ya reservado. Intente nuevamente.")
                    continue
                asientos[fila][columna] = nombre
                print("Asiento {fila}{columna} reservado para {nombre}.")
                print()
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese números válidos.")
    
    elif opcion == "2":
        print("\nMapa de Asientos:")
        for fila in range(1, FILAS + 1):
            for columna in COLUMNAS:
                print("{fila}{columna}: {asientos[fila][columna]}", end=" | ")
            print()
            print()
    
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")
