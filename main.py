# Algoritmos y Programacion Básica
# fecha: 14 de mayo de 2023
# Descripcion: Fase 3 Proyecto programado
# Ernesto David Ascencio Ramírez, Hugo Daniel Barillas Ajín, Esteban Enrique Cárcamo Urízar, Javier Alejando Chávez
# carné 23009, 23556, 23016, 23132

import pandas as pd
from modulos import *
import turtle

#variables del proyecto
ciclo = True
mouse = turtle.Turtle()
screen_width, screen_height = turtle.screensize()
window = turtle.Screen()

#Configuraciones de turlte
turtle.setup(width=0.5, height=0.6, startx=None, starty=None)
turtle.setworldcoordinates(0, 0, screen_width, screen_height)
mouse.speed(0)

def pantallaInicio():
    #Configuraciones de la ventana principal
    window.title("STUDIFY")
    window.bgcolor("#DE9E36")



    #Configuraciones del texto principal
    texto_inicio = "Bienvenidos a Studify"
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


    # Creación de los subtítulos
    subtitulos = ["1. Iniciar Sesión", "2. Registrarse", "3. Modificar Datos", "4. Mostrar Usuarios", "5. Mostrar gráficas", "6. Salir"]
    
    y_pos_sub = pos_y - 20  # Posición vertical inicial

    for subtitulo in subtitulos:
        mouse.goto(pos_x, y_pos_sub)
        mouse.write(subtitulo, align="center", font=("Arial", 16))
        y_pos_sub -= 30  # Desplazamiento vertical para el siguiente subtítulo


while ciclo == True:
    borrarVentana(window)
    pantallaInicio()
    
    df = pd.read_csv("Usuarios.csv")
    
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
        
                
        borrarVentana(window)
        
        titulosPantallas(window,mouse,'Inicia Sesión con Studify',screen_width,screen_height,'#DEB841')
 
                
        IniciarSesion(df,window,mouse,screen_width,screen_height)
        
        
        #PREGUNTA PARA REPETIR EL CODIGO
        ciclo = pregunta(ciclo)

    elif opcion == 2:
       
        borrarVentana(window)
 
        
        titulosPantallas(window,mouse,'Registrate en Studify',screen_width,screen_height,'#DE9E36')
 
 
 
        Registrarse(df,mouse,screen_width,screen_height)
 
        #PREGUNTA PARA REPETIR EL CODIGO
        ciclo = pregunta(ciclo)
        
    elif opcion == 3:
        borrarVentana(window)
        
        titulosPantallas(window,mouse,'Modifica tus datos de Studify',screen_width,screen_height,'#BFBDC1')
 
        
        
        CambiarDatos(df,mouse,screen_width,screen_height)
        
        #PREGUNTA PARA REPETIR EL CODIGO
        ciclo = pregunta(ciclo)
        
    elif opcion == 4:

        borrarVentana(window)
        
        window.bgcolor("#DEB841")
        
        mouse.goto(-30,350)
        
        # Función para dibujar una celda de la tabla
        def dibujar_celda(texto):
            mouse.pendown()
            mouse.forward(40)
            mouse.write(texto, align="center", font=("Arial", 16))
            mouse.forward(40)
            mouse.penup()

        # Dibujar las etiquetas de columna
        etiquetas = df.columns.tolist()
        for etiqueta in etiquetas:
            dibujar_celda(etiqueta)
            
        mouse.goto(-30,330)
        # Dibujar las filas de datos
        for _, fila in df.iterrows():
            valores = fila.values.tolist()
            for valor in valores:
                dibujar_celda(str(valor))

            mouse.goto(-30, mouse.ycor() - 20)
        #PREGUNTA PARA REPETIR EL CODIGO
        ciclo = pregunta(ciclo)
        
        
    elif opcion == 5:
        borrarVentana(window)

        titulosPantallas(window, mouse, 'Gráficas estadíticas de Studify', screen_width, screen_height, '#DEB841')

        pos_x = screen_width / 2
        pos_y = screen_height / 2
        y_pos_sub = pos_y - 20  # Posición vertical inicial

        textos = ["1. Ver gráfica de rating", "2. Ver gráfica de interesados", "3. Ver gráfica de suscritos", "4. Estadísticas globales", "5. Estadísticas por categoría"]

        for texto in textos:
            mouse.goto(pos_x, y_pos_sub)
            mouse.write(texto, align="center", font=("Arial", 16))
            y_pos_sub -= 30  # Desplazamiento vertical para siguiente subtítulo

        opcGraficas = input("Que desea hacer? \n")
        if not opcGraficas.isdigit() or int(opcGraficas) < 1 or int(opcGraficas) > 5:
            print("Opcion no valida")
        else:
            opcGraficas = int(opcGraficas)
            if opcGraficas == 1:
                borrarVentana(window)
                titulosPantallas(window, mouse, 'Gráfica de Rating', screen_width, screen_height, '#6fd456')
                GraficaRatingPlataforma()
            elif opcGraficas == 2:
                borrarVentana(window)
                titulosPantallas(window, mouse, 'Gráfica de Interesados', screen_width, screen_height, '#6fd456')
                GraficaCategoriaInteresados()
            elif opcGraficas == 3:
                borrarVentana(window)
                titulosPantallas(window, mouse, 'Gráfica de suscritos', screen_width, screen_height, '#6fd456')
                GraficaCategoriaSuscritos()
            elif opcGraficas == 4:
                borrarVentana(window)
                titulosPantallas(window, mouse, 'Estadísticas globales', screen_width, screen_height, '#6fd456')
                EstadisticasGlobales()
            elif opcGraficas == 5:
                os.system("cls")
                borrarVentana(window)
                titulosPantallas(window, mouse, 'Gráficas Inscritos por Categoría', screen_width, screen_height, '#DEB841')

                textos = ["Arte", "Numérico", "Emprendimiento", "Idiomas", "Ciencias", "Tecnología"]

                mouse.goto(60, 115)

                for i in range(2):
                    for j in range(3):
                        index = i * 3 + j
                        mouse.write(str(index + 1) + ") " + textos[index], align="center", font=("Arial", 24, "bold"))
                        mouse.forward(125)

                    mouse.goto(60, mouse.ycor() - 50)

                opcCurso = input("Que desea hacer? \n")
                if not opcCurso.isdigit() or int(opcCurso) < 1 or int(opcCurso) > 6:
                    print("Opcion no valida")
                else:
                    opcCurso = int(opcCurso)
                    if opcCurso == 1:
                        print("-" * 100)
                        print("ESTADÍSTICAS")
                        EstadisticasCategoria('Arte')
                        print("-" * 100)
                        print("INFORMACIÓN")
                        GraficaCursoInscritos('Arte')
                        InformacionCursos('Arte')
                    elif opcCurso == 2:
                        print("-" * 100)
                        print("ESTADÍSTICAS")
                        EstadisticasCategoria('Numerico')
                        print("-" * 100)
                        print("INFORMACIÓN")
                        InformacionCursos('Numerico')
                        GraficaCursoInscritos('Numerico')
                    elif opcCurso == 3:
                        print("-" * 100)
                        print("ESTADÍSTICAS")
                        EstadisticasCategoria('Emprendimiento')
                        print("-" * 100)
                        print("INFORMACIÓN")
                        InformacionCursos('Emprendimiento')
                        GraficaCursoInscritos('Emprendimiento')
                    elif opcCurso == 4:
                        print("-" * 100)
                        print("ESTADÍSTICAS")
                        EstadisticasCategoria('Idiomas')
                        print("-" * 100)
                        print("INFORMACIÓN")
                        InformacionCursos('Idiomas')
                        GraficaCursoInscritos('Idiomas')
                    elif opcCurso == 5:
                        print("-" * 100)
                        print("ESTADÍSTICAS")
                        EstadisticasCategoria('Ciencias')
                        print("-" * 100)
                        print("INFORMACIÓN")
                        InformacionCursos('Ciencias')
                        GraficaCursoInscritos('Ciencias')
                    elif opcCurso == 6:
                        print("-" * 100)
                        print("ESTADÍSTICAS")
                        EstadisticasCategoria('Tecnología')
                        print("-" * 100)
                        print("INFORMACIÓN")
                        InformacionCursos('Tecnología')
                        GraficaCursoInscritos('Tecnología')

        # PREGUNTA PARA REPETIR EL CÓDIGO
        ciclo = pregunta(ciclo)

    
    elif opcion == 6:
        print("Saliendo del programa")
        break
    
    elif opcion > 6 or opcion <= 0:
        print("Estas opciones no existen")
        
        #PREGUNTA PARA REPETIR EL CODIGO
        ciclo = pregunta(ciclo)

print("Programa finalizado")