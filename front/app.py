import streamlit as st
import sys, os
# Ajustar la ruta para importar el backend
#esto permite que 'front/app.py' pueda ver la carpeta 'back/
current_dir = os.path.dirname(os.path.abspath(__file__))#ruta /front
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))#ruta del projecto
sys.path.append(parent_dir) # añadimos la raiz del sistema

from back.generador import procesar_solicitud

# Configuración de la página
st.set_page_config(
    page_title="Generador de Contenido de Marketing",
    page_icon="📈",
    layout="wide",
)
#cabecera
st.title("📈 Generador de Contenido de Marketing para Redes Sociales")
st.markdown("""
Bienvenido al Generador de Contenido de Marketing para Redes Sociales.
Esta aplicación utiliza modelos de lenguaje y generación de imágenes 
para crear publicaciones atractivas adaptadas a diferentes plataformas y audiencias.
""")
st.markdown("---")

# layout principal(2 columnas)
col1, col2 = st.columns([1,2], gap="large")
with col1:
    st.header("1. Configuracion")
    with st.container(border=True):
        tema = st.text_input("¿Sobre que es el post?", placeholder = "Ej:Ciberseguridad en pimes")
        plataforma = st.selectbox("Plataforma de Redes Sociales", ["Instagram", "Facebook", "Twitter", "LinkedIn"])
        audiencia = st.text_input("Audiencia Objetivo", "Jóvenes Profesionales")

        st.write("")# Espacio en blanco
        generar_btn = st.button("Generar Contenido", type="primary", use_container_width=True)
    
with col2:
    st.header("2. Resultados")
    
    if generar_btn:
        if not tema or not audiencia:
            st.warning("Por favor, complete todos los campos antes de generar el contenido.")
        else:
            with st.spinner("Los Agentes de IA están trabajando..."):
                #llamada al backend
                resultado = procesar_solicitud(tema, plataforma, audiencia)
                #guardar en session para no perderlo si tocas algo
                st.session_state['resultado_actual'] = resultado
                
    # Mostrar resultados si existen en session_state(memoria)
    if 'resultado_actual' in st.session_state:
        res = st.session_state['resultado_actual']
        
        #mostrar imagen
        st.image(res["imagen_url"], caption="Imagen generada por IA", use_column_width=True)
        #mostrar texto
        st.subheader("Texto de la Publicación")
        st.text_area("Copia y edita tu post:", value=res["texto"], height=250)
        #mostrar metadatos
        with st.expander("Ver detalles tecnicos (Logs)"):
            st.json(res["meta"])
    else:
        st.info("Complete la configuración a la izquierda y haga clic en 'Generar Contenido' para ver los resultados aquí.")
        
