
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt

dfDatos = pd.read_csv("Datos.csv")

#FUNCIÓN PARA PODER REGRESAR AL MENU O SALIR
def pregunta(estado):
    while True:
        opcion = input("Desea realizar otra operacion? Si/No: ")
        opcion = opcion.lower().replace('í', 'i')
        
        if opcion == 'si':
            estado = True
            os.system("pause")
            os.system("cls")
            break  # Salir del bucle si la opción es válida
        
        elif opcion == 'no':
            os.system("cls")
            print("Saliendo del programa...")
            estado = False
            sys.exit(0)
        
        else:
            print("Opción no válida, ingresar de nuevo")
    
    return estado

     
#FUNCION PARA REGISTRAR UN NUEVO USUARIO
def Registrarse(df): 
    #df = pd.DataFrame(columns=['Usuario', 'Contraseña'])  
    name = input("Ingrese el nombre de la cuenta: ")
    password = input("Ingrese la contraseña de la cuenta: ")

    addrow = pd.DataFrame({'Usuario': [name], 'Password': [password]})

    dfNew = pd.concat([df, addrow])
    dfNew.to_csv("Usuarios.csv", index=False)
    print(dfNew)

    return dfNew

#FUNCION PARA REGISTRARSE CON EL USUARIO YA CREADO
def IniciarSesion(df):
    logged_in = False  # Variable para controlar el inicio de sesión

    while not logged_in:  # Repetir hasta que se inicie sesión correctamente
        name = input("Ingrese el usuario de su cuenta: ")
        password = input("Ingrese la contraseña de su cuenta: ")
    
        maskName = df['Usuario'].str.contains(name)
        maskPassword = df['Password'].str.contains(password)
    
        if df[maskName & maskPassword].empty:  # Verificar si no hay coincidencias en los datos
            print("Usuario o contraseña no válida")
        else:
            print("Inicio de sesión exitoso")
            logged_in = True  # Actualizar el estado de inicio de sesión
            
            os.system("pause")
            os.system("cls")
            #FUNCIÓN PARA ACCEDER A LAS CATEGORIAS
            Categorias()
        
         
def CambiarDatos(df):
    # Solicitar nombre de usuario y contraseña
    name = input("Ingrese el usuario de su cuenta: ")
    password = input("Ingrese la contraseña de su cuenta: ")
    
    # Verificar coincidencia exacta de nombre de usuario y contraseña en el DataFrame
    maskName = df['Usuario'] == name
    maskPassword = df['Password'] == password
    
    if maskName.any() and maskPassword.any():
        # Si hay coincidencia exacta, solicitar opción de modificación
        option = input("Seleccione una opción para modificación: \n1. Modificar nombre \n2. Modificar contraseña \n")
        
        if option.isdigit():
            option = int(option)
            
            if option == 1:
                # Modificar nombre de usuario
                newName = input("Ingrese el nuevo nombre de su cuenta: ")
                df.loc[maskName, 'Usuario'] = newName
                
            elif option == 2:
                # Modificar contraseña
                newPassword = input("Ingrese la nueva contraseña de su cuenta: ")
                df.loc[maskPassword, 'Password'] = newPassword
                
            else:
                # Opción no válida
                print("Opción no válida, ingrese de nuevo")
                
        else:
            # Opción no válida
            print("Opción no válida, ingrese de nuevo")
            
    else:
        # No hay coincidencia exacta de nombre de usuario y contraseña
        print("Datos no proporcionados o agregados con anterioridad")
    
    # Guardar los cambios en el archivo CSV
    df.to_csv("Usuarios.csv", index=False)






def Categorias():
    while True:
        try:
            opCat = int(input("Elige una categoría \n 1. Arte \n 2. Numérico \n 3. Negocios \n 4. Idiomas \n 5. Ciencias \n 6. Tecnología \n Presiona 7 para salir. \n"))
        except ValueError:
            print("Opciones no válidas")
            os.system("pause")
            os.system("cls")
            continue

        if opCat < 1 or opCat > 7:
            print("Ingrese un número válido")
            os.system("pause")
            os.system("cls")
            continue
        
        os.system("pause")
        os.system("cls")
        #Menú cursos de arte
        if opCat == 1:
            InfoCategoria("Arte")
        #Menú cursos numéricos
        elif opCat == 2:
            InfoCategoria("Numerico")
        #Menú cursos de negocios
        elif opCat == 3:
            InfoCategoria("Emprendimiento")
        #Menú cursos de idiomas
        elif opCat == 4:
            InfoCategoria("Idiomas")
        #Menú cursos de ciencias    
        elif opCat == 5:
            InfoCategoria("Ciencia")
        #Menú cursos de tecnología
        elif opCat == 6:
            InfoCategoria("Computacional")
        else:
            print("Saliendo de las categorías.... \n Regresando al menú principal")

        break


def InfoCategoria(categoria):
    dfCategoria = dfDatos[dfDatos["courseCategory"] == categoria]
    
    # Cálculo de interesados
    interesados = dfCategoria["interestCategory"].sum()
    
    # Cálculo de suscriptores
    suscriptores = dfCategoria["suscribersCategory"].sum()
    
    # Cálculo de calificación promedio de la categoría
    calificacionCategoria = dfCategoria["platformRating"].mean()
    
    dfCursos = dfCategoria["course"].values
    
    print(f"{categoria}")
    print(f"{interesados} personas se han interesado en esta categoría.")
    print(f"{suscriptores} personas se han suscrito a este curso desde Studify.")
    print(f"Esta categoría tiene una clasificación de {calificacionCategoria} por parte de los suscriptores de Studify.")
    print("Estos son los cursos más populares de esta categoría: ")
    
    i = 1
    for curso in dfCursos:   
        print(f"{i}. {curso}")
        i += 1
    
    while True:
        # Pregunta al usuario si desea ver la información de alguno de los cursos
        opcion = input("¿Te gustaría ver la información de alguno de estos cursos? (Si/No): ").lower()
        
        if opcion == "si":
            while True:
                try:
                    # Pregunta al usuario qué curso desea ver
                    opCur = int(input("¿Cuál de estos cursos te gustaría probar? Ingresa una opción entre 1 y 6. Presione 7 para salir: "))
                    
                    if opCur < 1 or opCur > 6:
                        print("Ingrese un número válido")
                        continue
                    
                    os.system("pause")
                    os.system("cls")
                    InfoCursos(opCur - 1, dfCategoria)
                    
                except ValueError:
                    print("Opción no válida")
                    continue
                
                break
                
        elif opcion == "no":
            print("Regresando al menú principal")
            break
            
        else:
            print("Opción no válida")


def InfoCursos(index, dfCategoria):

    calificacion= dfCategoria["userRating"].values[index]
    descripcion = dfCategoria["Descripcion"].values[index]
    inscrito = dfCategoria["userEnrolled"].values[index]
    curso = dfCategoria["course"].values[index]
    print(f"{curso}")
    print(f"Este curso tiene una calificación de {calificacion} por los suscriptores de Studify.")
    print(f"{descripcion}")
    print(f"{inscrito} personas se han inscrito a este curso desde Studify.")

def GraficaRatingPlataforma():
    dfInfo = dfDatos[["platform", "platformRating"]]
    dfGrafica = dfInfo.drop_duplicates(keep='first')
    dfGrafica.plot(x="platform", y="platformRating",kind="bar")
    plt.title("Plataforma")
    plt.xlabel("Rating")
    plt.xticks(rotation=0)
    plt.show()

def GraficaCategoriaInteresados():
    dfInfo = dfDatos[["courseCategory", "interestCategory"]]
    dfGrafica = dfInfo.drop_duplicates(keep='first')
    dfGrafica.plot(x="courseCategory", y="interestCategory",kind="bar")
    plt.title("Categoria")
    plt.xlabel("Interesados")
    plt.xticks(rotation=0)
    plt.show()

def GraficaCategoriaSuscritos():
    dfInfo = dfDatos[["courseCategory", "suscribersCategory"]]
    dfGrafica = dfInfo.drop_duplicates(keep='first')
    dfGrafica.plot(x="courseCategory", y="suscribersCategory",kind="bar")
    plt.title("Categoria")
    plt.xlabel("Suscritos")
    plt.xticks(rotation=0)
    plt.show()

def GraficaCursoInscritos(categoria):
    dfCategoria = dfDatos[dfDatos["courseCategory"] == categoria]
    dfGrafica = dfCategoria[["course", "userEnrolled"]]
    dfGrafica.plot(x="course", y="userEnrolled",kind="bar")
    plt.title("Curso")
    plt.xlabel("Inscritos")
    plt.xticks(rotation=0)
    plt.show()

def EstadisticasGlobales():
    print(dfDatos.describe())

def EstadisticasCategoria(categoria):
    dfEstadistica = dfDatos[dfDatos["courseCategory"] == categoria]
    print(dfEstadistica.describe())

def InformacionCursos(categoria):
    dfCursos = dfDatos[dfDatos["courseCategory"] == categoria]
    print(dfCursos)


