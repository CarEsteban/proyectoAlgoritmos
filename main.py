# Algoritmos y Programacion Básica
# fecha: 14 de mayo de 2023
# Descripcion: Fase 3 Proyecto programado
# Ernesto David Ascencio Ramírez, Hugo Daniel Barillas Ajín, Esteban Enrique Cárcamo Urízar, Javier Alejando Chávez
# carné 23009, 23556, 23016, 23132

import pandas as pd
import os
import sys
from modulos import *
 

df = pd.DataFrame(columns=['Usuario', 'Password'])  




ciclo = True

while ciclo == True:
    print("Bienvenido a Studify")
    print("1. Iniciar Sesion: \n2. Registrarse: \n3. Modificar Datos")
    opcion= int(input("Que decea hacer? "))
    os.system("pause")
    os.system("cls")
               
    if opcion == 1:
        print("BIENVENIDO AL INICIO DE SESIÓN")
        print("--------------------------------------")
        IniciarSesion(df)
        Categorias()
        
        
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
         
    else:
        print("Saliendo del programa")
        break