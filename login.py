# Algoritmos y Programacion Básica
# fecha: 09 de febrero de 2023
# Descripcion: Ejercicio en clase
# Ernesto David Ascencio Ramírez, Hugo Daniel Barillas Ajín
# carné 23009
import pandas as pd
import os
import sys

def pregunta(estado):
    opcion = input("Desea realizar otra operacion? Si/No: ")
    opcion = opcion.lower().replace('í', 'i')
    if opcion == 'si':
        estado = True
        os.system("cls")
      
    elif opcion == 'no':
        os.system("cls")
        print("Saliendo del programa...")
        estado = False
        sys.exit(0)
    return estado 


df = pd.DataFrame(columns=['Usuario', 'Password'])  
def Registrarse(df):
    #df = pd.DataFrame(columns=['Usuario', 'Contraseña'])  
    name = input("Ingrese el nombre de la cuenta: ")
    password = input("Ingrese la contraseña de la cuenta: ")

    addrow = pd.DataFrame({'Usuario': [name], 'Password': [password]})

    df = pd.concat([df, addrow], ignore_index=True)

    print(df)

def IniciarSesion(df):
    
    name = input("Ingrese el usuario de su cuenta: ")
    password = input("Ingrese la contraseña de su cuenta: ")
    
    maskName = df['Usuario'].str.contains(name)
    maskPassword = df['Password'].str.contains(password)
    
    if (df[maskName].index == df[maskPassword].index):
        print("Exito en iniciar sesion")
        
    print(df[maskName].index)
             
def CambiarDatos(df):
    
    name = input("Ingrese el usuario de su cuenta: ")
    password = input("Ingrese la contraseña de su cuenta: ")
    
    maskName = df['Usuario'].str.contains(name)
    maskPassword = df['Password'].str.contains(password)
    
    if (df[maskName].index == df[maskPassword].index):
        option = int(input("Seleccione una opcion para modificacion \n 1. Modificar nombre \n 2. Modificar contraseña \n"))
        
        if(option == 1):
            newName = input("Ingrese el nuevo nombre de su cuenta: ")
            df.at[int(maskName.index.values), 'Usuario'] = newName
        if(option == 2):
            newPassword = input("Ingrese la nueva contraseña de su cuenta: ")
            df.iat[int(maskPassword.index.values), 'Password'] = newPassword
            

ciclo = True

while ciclo == True:
    print("Bienvenido a Stidify")
    print("1. Iniciar Sesion: \n2. Registrarse: \n3. Modificar Datos")
    opcion= int(input("Que decea hacer? "))
               
    if opcion == 1:
        IniciarSesion(df)
        ciclo = pregunta(ciclo)

    elif opcion == 2:
       
        print("Registrase")

        name = input("Ingrese el nombre de la cuenta: ")
        password = input("Ingrese la contraseña de la cuenta: ")

        addrow = pd.DataFrame({'Usuario': [name], 'Password': [password]})

        df = pd.concat([df, addrow], ignore_index=True)

        print(df)
 
        #Registrarse(df)
        ciclo = pregunta(ciclo)
        
    elif opcion == 3:
        CambiarDatos(df)
        
        ciclo = pregunta(ciclo)
         
    else:
        print("Saliendo del programa")
        break