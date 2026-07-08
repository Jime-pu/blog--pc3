# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta o abrimos el folder desde visual Studio Code 

# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Opcional: Activaremos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1 (no instalar)

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu ordenador.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu ordenador.
# OJO: Debes antes tener instalado Streamlit en tu ordenador, 
## también debes antes definir la ruta de tus archivos y 
## tener un script de Python (nombre_de_tu_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC3.py
# python -m streamlit run nombre_de_tu_script.py

# Librería principal para desarrollar aplicaciones web con Streamlit.
import streamlit as st
# Herramienta para crear menús de navegación personalizados en Streamlit.
from streamlit_option_menu import option_menu
# Este módulo permite incrustar componentes personalizados escritos en HTML, CSS y JavaScript dentro de una aplicación.
# components.html() permite mostrar código HTML interactivo directamente en la interfaz.
import streamlit.components.v1 as components

# Menú vertical en una barra lateral
# Crea una barra lateral (sidebar) en la aplicación.
with st.sidebar:
    opciones = option_menu("Selecciona una sección: ",['Inicio', 'Experiencia', 'Gráficos'] , 
        icons=['hearts','flower1', 'cookie'], menu_icon="Flower1", default_index=0)
    # Crea un menú de opciones dentro de la barra lateral -> option_menu(...)
    # Título que se mostrará encima del menú -> "Selecciona una sección: "
    # Lista de opciones disponibles para navegar -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['0-circle','1-circle', '2-circle']
    # Icono principal que aparece junto al título del menú -> menu_icon="filetype-py"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0

# Menú horizontal en una barra horizontal
# OJO: Se puede eliminar el título del menú con None
# Crea un menú de navegación horizontal y guarda la opción seleccionada por el usuario en la variable 'selected'
#selected = option_menu(
   # menu_title="Selecciona una sección: ", 
    #options=['Inicio', 'Experiencia', 'Gráficos'], 
   # icons=['person-heart', 'globe-americas', 'pencil-square'], 
    #menu_icon="cast", default_index=0, orientation="horizontal")
    # Título que aparece antes de las opciones del menú -> menu_title="Selecciona una sección: "
    # Lista de opciones que estarán disponibles en el menú -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['person-heart', 'globe-americas', 'pencil-square']
    # Icono principal que aparece junto al título del menú -> menu_icon="cast"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0
    # Hace que el menú se muestre horizontalmente en lugar de verticalmente -> orientation="horizontal"

# Verifica si el usuario ha seleccionado la opción "Inicio" en el menú de navegación horizontal.
# OJO: En caso que elijas el menú de la barra lateral (sidebar) debes cambiar "selected" por "opciones"
if opciones == 'Inicio':
    st.markdown("<h1 style='text-align: center;'>⋆˚꩜｡Mi primer blog⋆˚꩜｡</h1>", unsafe_allow_html=True)
    # Muestra un título principal utilizando HTML -> st.markdown("...", unsafe_allow_html=True)
    # La etiqueta <h1> define un encabezado de nivel 1 -> "<h1 ...>...</h1>"
    # El estilo CSS 'text-align: center' centra el texto -> style='text-align: center;'
    # unsafe_allow_html=True permite que Streamlit interprete y renderice el código HTML incluido en la cadena

    # Crea dos columnas de igual tamaño para organizar el contenido de forma horizontal en la aplicación.
    col1, col2 = st.columns(2)

    # Muestra una imagen en la primera columna
    col1.image("foto.jpg", caption='Yo', width=300)
    # "ellie.png" es el archivo de imagen que se visualizará -> Aquí debes reemplazar por tu foto de perfil
    # El texto "Ellie" aparecerá como descripción de la imagen
    # width=300 establece el ancho de la imagen en 300 píxeles

    # Define una cadena de texto multilínea que contiene una guía para redactar una presentación personal.
    texto = """
     ────୨ৎ────
    ˚˖𓍢ִ໋❀
    Soy un estudiante de Comunicacion Audiovisual, me gusta escribir y narrar historias, me gusta el cine y la moda, ademas me gusta comer todo tipo de comida, mi color favorito es el color verde y mi plato favorito es la causa de atún
    Yo nací y crecí en Lima, sin embargo mis papá son migrantes 
    Actualmente me encuentro en el quinto ciclo de la facultad de Ciencias y Artes de la Comunicación de la Pontificia Universidad Catolica del Perú 
    Lo que me gusta de mi carrera es que me da la posibilidad de crear, las producciones audiovisuales estan en todas partes y ser comunicador te permite trabajar en lugares de manera muy versatil  
    Me gustaría trabajar en el área documental, aunque tambien en cualquier nota cultural, probablemente tal vez trabajar en la produccion de una película, mi sueño dorado sería trabajar en Aarmand Studios, ya que es mi estudio de animación predilecto, ya que me gusta mucho el stop motion
    Algo que me gusta tambien es el maquillaje, me gustan los maquillajes creativos o extravagantes ademas de los accesorios de gran tamañano
    ────୨ৎ──── 
    """

    # Muestra el texto en la segunda columna utilizando HTML
    col2.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto}</div>", unsafe_allow_html=True)
    # El estilo CSS justifica el texto y establece un tamaño de fuente de 18 píxeles
    # f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>"
    # unsafe_allow_html=True permite que Streamlit interprete las etiquetas HTML incluidas en la cadena

elif opciones == 'Experiencia':
    st.markdown("<h1 style='text-align: center;'>Mis experiencias con Python                                                                                🪼⋆.ೃ࿔*:･ 💻</h1>", unsafe_allow_html=True)

    # Agregar un  texto para la respuesta
    texto_2 = """
    ִֶָ. ..𓂃 ࣪ ִֶָ🪽་༘࿐ Python me esta enseñando a entender y crear diversas formas de presentar y organizar información. 
    Me senti bastante preocupada ya que era algo que nunca había intentado antes y temia que no pudiese llegar a entenderlo.
    Lo que me gusta de programar es que puedo modificar absolutamente cualquier caracteristica, dandome mas libertad conforme siga aprendiendo mas capacidades de codificar.
    Me gustaría llevar mas cursos afines de programación con este tipo de lenguaje de solo texto, es útil para poder complejizar algun proyecto o ejercitar mi mente 
    Se relaciona ya que es importante para un comunicador tener conocimientos diversificados además del manejo de datos, como las comunicaciones son interdisciplinarias y la programación te da casi completa libertad a la hora de crear los contenidos siento que puede ser un gran complemento.‧₊˚♪ 𝄞₊˚⊹
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # Formato A
    # Agregamos todo los videos realizados en las prácticas anteriores
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video 1 - PC1: explicando conceptos")
    # Inserta un video de YouTube directamente en la aplicación.
    # El usuario puede reproducirlo sin salir de Streamlit.
    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/1qwvVTVM1Y7_Cqc3XwP85bW4dVBHY8z7h/view?usp=sharing"
    )
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presenta información sobre los operadores booleanos, de pertenencia y comparativos  "
 
    )
    # Agrega una breve descripción del video.
    # Formato B
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video 2 -PC2: ")
    # Crea un botón que redirige al usuario a un video alojado en Google Drive. 
    # Al hacer clic, el video se abrirá en una nueva pestaña del navegador.
    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/1W7e9qJoF2EL9eK6kfONFxVYGaqoMw5N2/view?usp=sharing"
        )
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presenta información sobre las condicionales if, elif y else y como se utilizan"
        )
    st.subheader("🎥 Video 3 - Trabajo final")
    
    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/1zzYindZsC3KHWvYOKne7OG6VW9Swhpjb/view?usp=sharing")
    st.caption(
        "En este video se presenta información sobre el trabajo grupal sobre idols de kpop"
        )
elif opciones == 'Gráficos':
    st.markdown("<h2 style='text-align: center;'>Gráficos ദ്ദി •⩊• </h2>", unsafe_allow_html=True)

    graficos = ['Gráfico_1', 'Gráfico_2', 'Mapa_1']

    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico_1':
        # Título de la sección
        st.subheader("📊 Gráfico: Nube de palabras del texto de Harry Potter")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            Este es un grafico que desarrollamos de un fragmento del texto de harry potter previamente eliminando las palabras repetidas.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen utilizando tres columnas
        col3, col4, col5 = st.columns([1, 5, 1])

        with col4:
            st.image(
                "pepinillo.png",
                width=800
            )

    # Mostramos el gráfico seleccionado
    elif grafico_seleccionado == 'Gráfico_1':
        # Título de la sección
        st.subheader("📊 Gráfico: Nube de palabras del texto de Harry Potter")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            Este es un grafico que desarrollamos de un fragmento del texto de harry potter previamente eliminando las palabras repetidas.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen utilizando tres columnas
        col3, col4, col5 = st.columns([1, 5, 1])

        with col4:
            st.image(
                "pepinillo(1).png",
                width=800
            )

            )
    elif grafico_seleccionado == 'Mapa_1':
        # Título de la sección
        st.subheader("🗺️ Mapa 1: Distribución geográfica")

        # Interpretación del mapa
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Aquí debe ir una breve interpretación del mapa.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Cargar el mapa HTML generado previamente
        with open("mapa.html", "r", encoding="utf-8") as f:
            html_content = f.read()
            """
            Este mapa fue creado apartir de un top de 5 peliculas ubicadas en su lugar geografico con datos como:Año de creación, género, director y coordenadas.
            """,
        # Mostrar el mapa interactivo
        components.html(
            html_content,
            height=600
        )
