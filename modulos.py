
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import turtle


dfDatos = pd.read_csv("Datos.csv")

# Función para borrar el contenido de la ventana
def borrarVentana(window):
    window.clear()
    
    print("INGRESE SU OPCIÓN AQUÍ EN CONSOLA")

def titulosPantallas(window,mouse,titulo,screen_width,screen_height,color):
    
    window.title("STUDIFY")
    window.bgcolor(color)
    texto_inicio = titulo
    mouse.hideturtle()
    font_size = 40
    mouse.color("#37323E")

    #Posicionamiento en el centro
    pos_x = screen_width / 2
    pos_y = screen_height / 2

    mouse.penup()
    mouse.goto(pos_x, pos_y)

    font = ("Comic Sans MS", font_size, "bold")
    mouse.write(texto_inicio, align="center", font=font)
        
 
    
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
def Registrarse(df,mouse,screen_width,screen_height): 
    #df = pd.DataFrame(columns=['Usuario', 'Contraseña'])  
    name = input("Ingrese el nombre de la cuenta: ")
    password = input("Ingrese la contraseña de la cuenta: ")

    addrow = pd.DataFrame({'Usuario': [name], 'Password': [password]})

    dfNew = pd.concat([df, addrow])
    dfNew.to_csv("Usuarios.csv", index=False)
    
    mouse.goto((screen_width/2)-10,(screen_height/2)-30)
    texto = "Buena elección: " + name + ", bienvenido!"
    mouse.write(texto,align="center", font=("Comic Sans MS", 24, "bold"))
    

    return dfNew

#FUNCION PARA REGISTRARSE CON EL USUARIO YA CREADO
def IniciarSesion(df,window,mouse,screen_width,screen_height):
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
            
            
            mouse.goto((screen_width/2)-10,(screen_height/2)-30)
            texto = "Bienvenido usuario: " + name
            mouse.write(texto,align="center", font=("Comic Sans MS", 24, "bold"))
            
            os.system("pause")
            os.system("cls")
            
            #FUNCIÓN PARA ACCEDER A LAS CATEGORIAS
            Categorias(window,mouse,screen_width,screen_height)
        
         
def CambiarDatos(df,mouse,screen_width,screen_height):
    # Solicitar nombre de usuario y contraseña
    name = input("Ingrese el usuario de su cuenta: ")
    password = input("Ingrese la contraseña de su cuenta: ")
    
    

    
    
    
    
    # Verificar coincidencia exacta de nombre de usuario y contraseña en el DataFrame
    maskName = df['Usuario'] == name
    maskPassword = df['Password'] == password
    
    if maskName.any() and maskPassword.any():
        
            
        mouse.goto((screen_width/2)-10,(screen_height/2)-30)
        texto = "Ingresado como: " + name
        mouse.write(texto,align="center", font=("Comic Sans MS", 24, "bold"))
        
        
        # Si hay coincidencia exacta, solicitar opción de modificación
        option = input("Seleccione una opción para modificación: \n1. Modificar nombre \n2. Modificar contraseña \n")
        
        if option.isdigit():
            option = int(option)
            
            if option == 1:
                # Modificar nombre de usuario
                newName = input("Ingrese el nuevo nombre de su cuenta: ")
                df.loc[maskName, 'Usuario'] = newName
                
                mouse.goto((screen_width/2)-10,(screen_height/2)-60)
                texto = "Usuario cambiado a: " + newName
                mouse.write(texto,align="center", font=("Comic Sans MS", 24, "bold"))
    

                
            elif option == 2:
                # Modificar contraseña
                newPassword = input("Ingrese la nueva contraseña de su cuenta: ")
                df.loc[maskPassword, 'Password'] = newPassword
                
                
                mouse.goto((screen_width/2)-10,(screen_height/2)-60)
                texto = "Contraseña cambiada a: " + newPassword
                mouse.write(texto,align="center", font=("Comic Sans MS", 24, "bold"))
    
                
            else:
                # Opción no válida
                print("Opción no válida, ingrese de nuevo")
                
        else:
            # Opción no válida
            print("Opción no válida, ingrese de nuevo")
            
    else:
        
        mouse.goto((screen_width/2)-10,(screen_height/2)-30)
        texto = "Error"
        mouse.write(texto,align="center", font=("Comic Sans MS", 24, "bold"))
        
        # No hay coincidencia exacta de nombre de usuario y contraseña
        print("Datos no proporcionados o agregados con anterioridad")
    
    # Guardar los cambios en el archivo CSV
    df.to_csv("Usuarios.csv", index=False)






def Categorias(window,mouse,screen_width,screen_height):
    borrarVentana(window)
    
    window.title("CATEGORÍAS")
    window.bgcolor("#DE9E36")
    texto_inicio = "Selecciona su categoría a ver"
    mouse.hideturtle()
    font_size = 40
    mouse.color("#37323E")

    #Posicionamiento en el centro
    pos_x = screen_width / 2
    pos_y = screen_height / 1.5

    mouse.penup()
    mouse.goto(pos_x, pos_y)

    font = ("Comic Sans MS", font_size, "bold")
    mouse.write(texto_inicio, align="center", font=font)
    
            
    # Lista de los títulos
    lista_titulos = ["Arte", "Numérico", "Emprendimiento", "Idiomas", "Ciencias", "Tecnología"]

    mouse.goto(60, 125)
    
    # Ciclo para mostrar los títulos en dos filas de tres columnas
    for i in range(2):
        for j in range(3):
            # Obtener el índice del título correspondiente
            index = i * 3 + j
            # Mostrar el título en la posición actual
            mouse.write(str(index+1)+") "+lista_titulos[index], align="center", font=("Arial", 24, "bold"))
            mouse.forward(125)

        # Mover a la siguiente línea
        mouse.goto(60, mouse.ycor() - 50)





    while True:
        try:
            opCat = int(input("Ingrese el número de su opción según la interfaz gráfica \nSi desea salir presione 7\n"))
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
            InfoCategoria("Arte",mouse,window,screen_width,screen_height)
        #Menú cursos numéricos
        elif opCat == 2:
            InfoCategoria("Numerico",mouse,window,screen_width,screen_height)
        #Menú cursos de Emprendimiento
        elif opCat == 3:
            InfoCategoria("Emprendimiento",mouse,window,screen_width,screen_height)
        #Menú cursos de idiomas
        elif opCat == 4:
            InfoCategoria("Idiomas",mouse,window,screen_width,screen_height)
        #Menú cursos de ciencias    
        elif opCat == 5:
            InfoCategoria("Ciencia",mouse,window,screen_width,screen_height)
        #Menú cursos de tecnología
        elif opCat == 6:
            InfoCategoria("Computacional",mouse,window,screen_width,screen_height)
        else:
            print("Saliendo de las categorías.... \n Regresando al menú principal")

        break


def InfoCategoria(categoria,mouse,window,screen_width,screen_height):
    dfCategoria = dfDatos[dfDatos["courseCategory"] == categoria]
    
    # Cálculo de interesados
    interesados = dfCategoria["interestCategory"].sum()
    
    # Cálculo de suscriptores
    suscriptores = dfCategoria["suscribersCategory"].sum()
    
    # Cálculo de calificación promedio de la categoría
    calificacionCategoria = dfCategoria["platformRating"].mean().round(2)
    
    dfCursos = dfCategoria["course"].values
    
    
    borrarVentana(window)
    
    window.title(categoria)
    window.bgcolor("#2b2e74")
    texto_inicio = categoria
    mouse.hideturtle()
    font_size = 40
    mouse.color("#FFF")

    #Posicionamiento en el centro
    pos_x = screen_width / 2
    pos_y = screen_height / 1.3

    mouse.penup()
    mouse.goto(pos_x, pos_y)

    font = ("Comic Sans MS", font_size, "bold")
    mouse.write(texto_inicio, align="center", font=font)
    
    
    interesadosText = str(interesados) + " personas se han interesado en esta categoría."
    suscriptoresText = str(suscriptores) + " personas se han suscrito a este curso desde Studify."
    calificacionText = "Esta categoría tiene una clasificación de " + str(calificacionCategoria) + " por parte de los suscriptores de Studify."
    cursosText = "Estos son los cursos más populares de esta categoría: "
    
    textosEscribir = [interesadosText,suscriptoresText,calificacionText,cursosText]
    mouse.goto(200,200)
    for i in range(len(textosEscribir)):
        mouse.goto(200,200-(i*20))
        mouse.write(textosEscribir[i], align="center", font=("Arial", 16))
        
    mouse.goto(200,120)
    mouse.write("-"*150, align="center", font=("Arial", 16))
    cursos = []
    i = 1
    for curso in dfCursos:   
        cursos.append(curso)
        i += 1
        
        
    mouse.goto(200,100)
    for i in range(len(cursos)):
        mouse.goto(200,100-(i*20))
        mouse.write(str(i+1)+") "+cursos[i], align="center", font=("Arial", 16))
    

    
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
                    InfoCursos(opCur - 1, dfCategoria,mouse,window,screen_width,screen_height)
                    
                except ValueError:
                    print("Opción no válida")
                    continue
                
                break
                
        elif opcion == "no":
            print("Regresando al menú principal")
            break
            
        else:
            print("Opción no válida")


def InfoCursos(index, dfCategoria,mouse,window,screen_width,screen_height):

    calificacion= dfCategoria["userRating"].values[index]
    descripcion = dfCategoria["Descripcion"].values[index]
    inscrito = dfCategoria["userEnrolled"].values[index]
    curso = dfCategoria["course"].values[index]
    
    
    borrarVentana(window)
    
    window.title(curso)
    window.bgcolor("#05604E")
    texto_inicio = curso
    mouse.hideturtle()
    font_size = 20
    mouse.color("#FFF")

    #Posicionamiento en el centro
    pos_x = screen_width / 2
    pos_y = screen_height / 1.3

    mouse.penup()
    mouse.goto(pos_x, pos_y)

    font = ("Comic Sans MS", font_size, "bold")
    mouse.write(texto_inicio, align="center", font=font)
    
    calificacionText = "Este curso tiene una calificación de "+ str(calificacion)+" por los suscriptores de Studify."
    descripcionText = descripcion
    inscritosText = str(inscrito) + " personas se han inscrito a este curso desde Studify."
    
    textosEscribir = [calificacionText,inscritosText,descripcionText]
    mouse.goto(200,200)
    for i in range(len(textosEscribir)):
        mouse.goto(200,200-(i*20))
        
        
        mouse.write(textosEscribir[i], align="center", font=("Arial", 16))
        
    os.system("pause")
    os.system("cls")
        
    

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
    plt.xticks(rotation=90)
    plt.show()

def EstadisticasGlobales():
    print(dfDatos.describe())

def EstadisticasCategoria(categoria):
    dfEstadistica = dfDatos[dfDatos["courseCategory"] == categoria]
    print(dfEstadistica.describe())

def InformacionCursos(categoria):
    dfCursos = dfDatos[dfDatos["courseCategory"] == categoria]
    print(dfCursos)


