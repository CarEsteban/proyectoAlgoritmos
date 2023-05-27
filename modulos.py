
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt

dfDatos = pd.read_csv("Datos.csv")

def Registrarse(df): 
    #df = pd.DataFrame(columns=['Usuario', 'Contraseña'])  
    name = input("Ingrese el nombre de la cuenta: ")
    password = input("Ingrese la contraseña de la cuenta: ")

    addrow = pd.DataFrame({'Usuario': [name], 'Password': [password]})

    dfNew = pd.concat([df, addrow])
    dfNew.to_csv("Usuarios.csv", index=False)
    print(dfNew)

    return dfNew



def pregunta(estado):
    opcion = input("Desea realizar otra operacion? Si/No: ")
    opcion = opcion.lower().replace('í', 'i')
    if opcion == 'si':
        estado = True
        os.system("pause")
        os.system("cls")
      
    elif opcion == 'no':
        os.system("cls")
        print("Saliendo del programa...")
        estado = False
        sys.exit(0)
    return estado 
     
def IniciarSesion(df):
    
    name = input("Ingrese el usuario de su cuenta: ")
    password = input("Ingrese la contraseña de su cuenta: ")
    
    maskName = df['Usuario'].str.contains(name)
    maskPassword = df['Password'].str.contains(password)
    
    if (df[maskName].index == df[maskPassword].index):
        print("Exito en iniciar sesion")
        
        os.system("pause")
        os.system("cls")
        Categorias()
        
    #print(df[maskName].index)
         
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
            df.at[int(maskPassword.index.values), 'Password'] = newPassword
    df.to_csv("Usuarios.csv", index=False)


def InfoCategoria(categoria):
    dfCategoria = dfDatos[dfDatos["courseCategory"] == categoria]
    interesados = dfCategoria["interestCategory"].values[0]
    suscriptores = dfCategoria["suscribersCategory"].values[0]
    calificacionCategoria = dfCategoria["platformRating"].values[0]
    dfCursos = dfCategoria["course"].values
    i = 1
    print(f"{categoria}")
    #print("¡En esta categoría podrás encontrar cursos de páginas web, blogs, tutoriales y bocetos de ejemplo que te ayudarán a dejar volar tu imaginación!") 
    #PARA QUE EL CÓDIGO DE ARRIBA FUNCIONE SE DEBE AÑADIR UNA NUEVA COLUMNA AL DATAFRAME "dfDatos", cambio en espera
    print(f"{interesados} personas se han interesado en esta categoría.")
    print(f"{suscriptores} personas se han suscrito a este curso desde Studify.")
    print(f"Esta categoría tiene una clasificación de {calificacionCategoria} por parte de los suscriptores de Studify.")
    print("Estos son los cursos más populares de esta categoría: ")
    for curso in dfCursos:   
        print(f"{i}. {curso}")
        i += 1

    print("¿Te gustaría ver la información de alguno de estos cursos?")
    opcion = int(input("\n 1. Si \n 2. No \n"))

    if opcion == 1:
        opCur = int(input("¿Cuál de estos cursos te gustaría probar? Ingresa una opción entre 1 y 6. Presione 7 para salir.\n"))
        index = opCur - 1
        InfoCursos(index, dfCategoria)
    elif opcion == 2:
        print("Regresando al menu principal")
    else:
        print("Opcion ingresada inváldia")

def InfoCursos(index, dfCategoria):

    calificacion= dfCategoria["userRating"].values[index]
    descripcion = dfCategoria["Descripcion"].values[index]
    inscrito = dfCategoria["userEnrolled"].values[index]
    curso = dfCategoria["course"].values[index]
    print(f"{curso}")
    print(f"Este curso tiene una calificación de {calificacion} por los suscriptores de Studify.")
    print(f"{descripcion}")
    print(f"{inscrito} personas se han inscrito a este curso desde Studify.")

def Categorias():
#Pantalla de categorías
#¡Nota! Los datos como nombres de los cursos, cantidad de suscriptores y calificaciones no son datos verdaderos, su único fin es ejemplificar cómo se verán en la pantalla de Turtle del programa final.
#Menú principal
#opCat sirve para elegir la categoría de los cursos
#opCur sirve para elegir el curso dentro de la categoría seleccionada

    opCat=0
    opCat=int(input("Elige una categoría \n 1. Arte \n 2. Numérico \n 3. Negocios \n 4. Idiomas \n 5. Ciencias \n 6. Tecnología \n Presiona 7 para salir. \n"))
    #Menú cursos de arte
    os.system("pause")
    os.system("cls")
    if opCat==1:
        InfoCategoria("Arte")
            
    #Menú cursos numéricos
    elif opCat==2:
        InfoCategoria("Numerico")
    #Menú cursos de negocios
    elif opCat==3:
        InfoCategoria("Emprendimiento")
    #Menú cursos de idiomas
    elif opCat==4:
        InfoCategoria("Idiomas")
    #Menú cursos de ciencias
    elif opCat==5:
        InfoCategoria("Ciencia")
    #Menú cursos de tecnología
    elif opCat==6:
        InfoCategoria("Computacional")
    else:
        print("Elige una opción válida.")

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


#Categorias()
#GraficaRatingPlataforma()
#GraficaCategoriaInteresados()
#GraficaCursoInscritos("Arte")
#EstadisticasCategoria("Arte")
InformacionCursos("Arte")


