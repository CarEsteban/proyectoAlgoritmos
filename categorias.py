#Pantalla de categorías
#¡Nota! Los datos como nombres de los cursos, cantidad de suscriptores y calificaciones no son datos verdaderos, su único fin es ejemplificar cómo se verán en la pantalla de Turtle del programa final.
#Menú principal
#opCat sirve para elegir la categoría de los cursos
#opCur sirve para elegir el curso dentro de la categoría seleccionada
opCat=0
opCat=int(input("Elige una categoría \n 1. Arte \n 2. Numérico \n 3. Negocios \n 4. Idiomas \n 5. Ciencias \n 6. Tecnología \n Presiona 7 para salir. \n"))
#Menú cursos de arte
if opCat==1:
    print("Arte")
    print("¡En esta categoría podrás encontrar cursos de páginas web, blogs, tutoriales y bocetos de ejemplo que te ayudarán a dejar volar tu imaginación!")
    print("20000 personas se han interesado en esta categoría.")
    print("5342 personas se han suscrito a este curso desde Studify.")
    print("Esta categoría tiene una clasificación de ***** por parte de los suscriptores de Studify.")
    print("Estos son los cursos más populares de esta categoría: \n 1. Dibujo técnico. \n 2. Origami para principiantes. \n 3. Ilustración botánica con acuarelas. \n 4. Retrato realista con lápiz. \n 5. Manualidades")
    opCur=0
    opCur=int(input("¿Cuál de estos cursos te gustaría probar? Ingresa una opción entre 1 y 5. Presione 6 para salir.\n"))
    if opCur== 1:
        print("Dibujo técnico")
        print("Este curso tiene una calificación de **** por los suscriptores de Studify.")
        print("En este curso encontrarás tutoriales y plantillas para aprender distintas técnicas de dibujo.")
        print("648 personas se han inscrito a este curso.")
        print("557 personas se han inscrito a este curso desde Studify.")
    elif opCur== 2:
        print("Origami para principiantes")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("En este curso encontrarás todo tipo de material que te ayudará a volverte un experto en Origami desde 0.")
        print("1110 personas se han inscrito a este curso.")
        print("789 personas se han inscrito a este curso desde Studify.")
    elif opCur== 3:
        print("Ilustración botánica con acuarelas")
        print("Este curso tiene una calificación de *** por los suscriptores de Studify.")
        print("En este curso encontrarás consejos y material didáctico descargable para volverte todo un Picasso con acuarelas.")
        print("125 personas se han inscrito a este curso.")
        print("100 personas se han inscrito a este curso desde Studify.")
    elif opCur== 4:
        print("Retrato realista con lápiz")
        print("Este curso tiene una calificación de **** por los suscriptores de Studify.")
        print("Con un simple lápiz puedes dibujar rostros igual de realistas que una foto, en este curso aprenderás cómo.")
        print("200 personas se han inscrito a este curso.")
        print("50 personas se han inscrito a este curso desde Studify.")
    elif opCur== 5:
        print("Manualidades")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Tus manos son tu mayor herramienta, Aprende a hacer todo lo que se te ocurra con ellas.")
        print("784 personas se han inscrito a este curso.")
        print("593 personas se han inscrito a este curso desde Studify.")
#Menú cursos numéricos
elif opCat==2:
    print("Numérico")
    print("¡En esta categoría podrás encontrar cursos y material de apoyo sobre las áreas numéricas más importantes.")
    print("58723 personas se han interesado en esta categoría.")
    print("10135 personas se han suscrito a este curso desde Studify.")
    print("Esta categoría tiene una clasificación de ***** por parte de los suscriptores de Studify.")
    print("Estos son los cursos más populares de esta categoría: \n 1. Trigonometría \n 2. Física \n 3. Contabilidad \n 4. Geometría \n 5. Álgebra")
    opCur=int(input("¿Cuál de estos cursos te gustaría probar? Ingresa una opción entre 1 y 5. Presione 6 para salir.\n"))
    if opCur== 1:
        print("Trigonometría")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Todo lo necesario para cálculo 1 y cálculo 2 está disponible en este curso.")
        print("1260 personas se han inscrito a este curso.")
        print("557 personas se han inscrito a este curso desde Studify.")
    if opCur== 2:
        print("Física")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Todas las fórmulas que necesitas, con videos explicativos para entender las leyes de la física")
        print("1110 personas se han inscrito a este curso.")
        print("800 personas se han inscrito a este curso desde Studify.")
    if opCur== 3:
        print("Contabilidad")
        print("Este curso tiene una calificación de **** por los suscriptores de Studify.")
        print("Desde impuestos hasta cuadros de balance, todo lo que un contador necesita. Con plantillas en Excel disponibles.")
        print("525 personas se han inscrito a este curso.")
        print("327 personas se han inscrito a este curso desde Studify.")
    if opCur== 4:
        print("Geometría")
        print("Este curso tiene una calificación de **** por los suscriptores de Studify.")
        print("Tutoriales, imágenes y ejemplos para entender geometría básica.")
        print("256 personas se han inscrito a este curso.")
        print("142 personas se han inscrito a este curso desde Studify.")
    if opCur== 5:
        print("Álgebra")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Material de varios profesores para que puedas entender fácilmente sobre álgebra")
        print("784 personas se han inscrito a este curso.")
        print("593 personas se han inscrito a este curso desde Studify.")
#Menú cursos de negocios
elif opCat==3:
    print("Negocios")
    print("¡En esta categoría podrás encontrar cursos, videos y libros con tips para volverte un mejor negociante.")
    print("10723 personas se han interesado en esta categoría.")
    print("751 personas se han suscrito a este curso desde Studify.")
    print("Esta categoría tiene una clasificación de **** por parte de los suscriptores de Studify.")
    print("Estos son los cursos más populares de esta categoría: \n 1. Coaching \n 2. Inversiones \n 3. ¿Qué son las criptomonedas? \n 4. Comercio exterior \n 5. Logística internacional")
    opCur=int(input("¿Cuál de estos cursos te gustaría probar? Ingresa una opción entre 1 y 5. Presione 6 para salir.\n"))
    if opCur== 1:
        print("Coaching")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Consejos útiles que te ayudarán a mejorar tus hábitos como comerciante.")
        print("1260 personas se han inscrito a este curso.")
        print("557 personas se han inscrito a este curso desde Studify.")
    if opCur== 2:
        print("Inversiones")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Los conceptos más importantes sobre el trading e inversiones en la bolsa y criptomonedas.")
        print("4568 personas se han inscrito a este curso.")
        print("485 personas se han inscrito a este curso desde Studify.")
    if opCur== 3:
        print("¿Qué son las criptomonedas?")
        print("Este curso tiene una calificación de **** por los suscriptores de Studify.")
        print("Breve historia de las criptomonedas y videos explicativos sobre ellas.")
        print("12348 personas se han inscrito a este curso.")
        print("6871 personas se han inscrito a este curso desde Studify.")
    if opCur== 4:
        print("Comercio exterior")
        print("Este curso tiene una calificación de **** por los suscriptores de Studify.")
        print("Todo lo necesario para volverte un negociante experto y llegar más lejos.")
        print("734 personas se han inscrito a este curso.")
        print("569 personas se han inscrito a este curso desde Studify.")
    if opCur== 5:
        print("Logística internacional")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Aprende cómo funcionan los negocios en otras partes del mundo.")
        print("784 personas se han inscrito a este curso.")
        print("593 personas se han inscrito a este curso desde Studify.")
#Menú cursos de idiomas
elif opCat==4:
    print("Idiomas")
    print("¡En esta categoría podrás encontrar cursos, videos y ejercicios para aprender idiomas fácilmente.")
    print("10723 personas se han interesado en esta categoría.")
    print("751 personas se han suscrito a este curso desde Studify.")
    print("Esta categoría tiene una clasificación de **** por parte de los suscriptores de Studify.")
    print("Estos son los cursos más populares de esta categoría: \n 1. Inglés \n 2. Francés \n 3. Alemán \n 4. Mandarín \n 5. Japonés")
    opCur=int(input("¿Cuál de estos cursos te gustaría probar? Ingresa una opción entre 1 y 5. \n"))
    if opCur== 1:
        print("Inglés")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Aprende inglés desde 0.")
        print("1265 personas se han inscrito a este curso.")
        print("547 personas se han inscrito a este curso desde Studify.")
    if opCur== 2:
        print("Francés")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Aprende francés desde 0.")
        print("4568 personas se han inscrito a este curso.")
        print("485 personas se han inscrito a este curso desde Studify.")
    if opCur== 3:
        print("Alemán")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Aprende alemán desde 0.")
        print("482 personas se han inscrito a este curso.")
        print("123 personas se han inscrito a este curso desde Studify.")
    if opCur== 4:
        print("Mandarín")
        print("Este curso tiene una calificación de **** por los suscriptores de Studify.")
        print("Aprende mandarín desde 0.")
        print("1000 personas se han inscrito a este curso.")
        print("568 personas se han inscrito a este curso desde Studify.")
    if opCur== 5:
        print("Japonés")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Aprende japonés desde 0.")
        print("784 personas se han inscrito a este curso.")
        print("524 personas se han inscrito a este curso desde Studify.")
#Menú cursos de ciencias
elif opCat==5:
    print("Ciencias")
    print("¡En esta categoría podrás encontrar el material que necesitas para todas las áreas científicas.")
    print("6823 personas se han interesado en esta categoría.")
    print("1158 personas se han suscrito a este curso desde Studify.")
    print("Esta categoría tiene una clasificación de **** por parte de los suscriptores de Studify.")
    print("Estos son los cursos más populares de esta categoría: \n 1. Ciencias sociales \n 2. Biología \n 3. Química \n 4. Astronomía \n 5. Física avanzada")
    opCur=int(input("¿Cuál de estos cursos te gustaría probar? Ingresa una opción entre 1 y 5. Presione 6 para salir.\n"))
    if opCur== 1:
        print("Ciencias sociales")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Todo sobre las distintas ciencias que estudian a nuestra sociedad")
        print("1545 personas se han inscrito a este curso.")
        print("647 personas se han inscrito a este curso desde Studify.")
    if opCur== 2:
        print("Biología")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Todo lo necesario para comprender a los seres vivos.")
        print("485 personas se han inscrito a este curso.")
        print("315 personas se han inscrito a este curso desde Studify.")
    if opCur== 3:
        print("Química")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Videos y presentaciones con formularios y definiciones.")
        print("500 personas se han inscrito a este curso.")
        print("134 personas se han inscrito a este curso desde Studify.")
    if opCur== 4:
        print("Astronomía")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Aprende a explorar el espacio con las distintas herramientas de exploración.")
        print("225 personas se han inscrito a este curso.")
        print("120 personas se han inscrito a este curso desde Studify.")
    if opCur== 5:
        print("Física avanzada")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Eleva tu conocimiento sobre física al más alto nivel. Física cuántica, termodinámica avanzada, todo está aquí.")
        print("465 personas se han inscrito a este curso.")
        print("513 personas se han inscrito a este curso desde Studify.")
#Menú cursos de tecnología
elif opCat==6:
    print("Tecnología")
    print("Aprende todo sobre las computadoras.")
    print("20688 personas se han interesado en esta categoría.")
    print("15401 personas se han suscrito a este curso desde Studify.")
    print("Esta categoría tiene una clasificación de **** por parte de los suscriptores de Studify.")
    print("Estos son los cursos más populares de esta categoría: \n 1. Hardware \n 2. IA \n 3. Programación \n 4. Electrónica \n 5. Ética")
    opCur=int(input("¿Cuál de estos cursos te gustaría probar? Ingresa una opción entre 1 y 5. Presione 6 para salir.\n"))
    if opCur== 1:
        print("Hardware")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Descubre para qué sirve cada parte de una computadora y cómo armarlas.")
        print("15454 personas se han inscrito a este curso.")
        print("8792 personas se han inscrito a este curso desde Studify.")
    if opCur== 2:
        print("IA")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Desde qué es una IA, hasta cómo sacarle el máximo provecho y obtener resultados satisfactorios.")
        print("4858 personas se han inscrito a este curso.")
        print("3153 personas se han inscrito a este curso desde Studify.")
    if opCur== 3:
        print("Programación")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Información, documentación y tutoriales para los lenguajes de programación más solicitados del momento.")
        print("7958 personas se han inscrito a este curso.")
        print("3458 personas se han inscrito a este curso desde Studify.")
    if opCur== 4:
        print("Electrónica")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Conceptos básicos sobre la electrónica, con herramientas online para practicar.")
        print("2250 personas se han inscrito a este curso.")
        print("1496 personas se han inscrito a este curso desde Studify.")
    if opCur== 5:
        print("Ética")
        print("Este curso tiene una calificación de ***** por los suscriptores de Studify.")
        print("Es importante conocer los riesgos de la tecnología, y utilizarla correctamente.")
        print("893 personas se han inscrito a este curso.")
        print("572 personas se han inscrito a este curso desde Studify.")  
elif opCat>7:
    print("Elige una opción válida.")