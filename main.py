# Algoritmos y Programacion Básica
# fecha: 14 de mayo de 2023
# Descripcion: Fase 3 Proyecto programado
# Ernesto David Ascencio Ramírez, Hugo Daniel Barillas Ajín, Esteban Enrique Cárcamo Urízar, Javier Alejando Chávez
# carné 23009, 23556, 23016, 23132

import pandas as pd
from modulos import *
 
ciclo = True



while ciclo == True:
    df = pd.read_csv("Usuarios.csv")
    print("Bienvenido a Studify")
    print("1. Iniciar Sesion: \n2. Registrarse: \n3. Modificar Datos \n4. Mostrar usuarios \n5. Salir")
    
    try:
        opcion = int(input("Que desea hacer? "))
    except ValueError:
        print("Solo se admiten numeros del 1 al 5")
        
        os.system("pause")
        os.system("cls")
        
        continue
    
    os.system("pause")
    os.system("cls")
               
    if opcion == 1:
        print("BIENVENIDO AL INICIO DE SESIÓN")
        print("--------------------------------------")
        IniciarSesion(df)
        
        
        #PREGUNTA PARA REPETIR EL CODIGO
        ciclo = pregunta(ciclo)

    elif opcion == 2:
       
        print("BIENVENIDO AL REGISTRO")
        print("--------------------------------------")
 
        Registrarse(df)
 
        #PREGUNTA PARA REPETIR EL CODIGO
        ciclo = pregunta(ciclo)
        
    elif opcion == 3:
        print("BIENVENIDO A LA MODIFICACIÓN DE DATOS")
        print("--------------------------------------")
        
        CambiarDatos(df)
        
        #PREGUNTA PARA REPETIR EL CODIGO
        ciclo = pregunta(ciclo)
        
    elif opcion == 4:
        
        print(df)
        #PREGUNTA PARA REPETIR EL CODIGO
        ciclo = pregunta(ciclo)
        
         
    elif opcion == 5:
        print("Saliendo del programa")
        break
    

    elif opcion > 5 or opcion <= 0:
        print("Estas opciones no existen")
        
        #PREGUNTA PARA REPETIR EL CODIGO
        ciclo = pregunta(ciclo)

print("Programa finalizado")