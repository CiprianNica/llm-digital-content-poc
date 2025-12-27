import streamlit as st
import sys, os

# --- GESTIÓN DE RUTAS ---
# Esto permite que 'front/app.py' pueda ver la carpeta 'back/'
current_dir = os.path.dirname(os.path.abspath(__file__)) # ruta /front
parent_dir = os.path.abspath(os.path.join(current_dir, '..')) # ruta del proyecto
sys.path.append(parent_dir) # añadimos la raíz del sistema

# --- IMPORTACIONES ---
# Solo importamos generar_contenido, procesar_solicitud lo quitamos por ahora
from back.generador import generar_contenido 

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Generador de Contenido AI",
    page_icon="🤖",
    layout="wide",
)

# --- CABECERA ---
st.title("🤖 Generador de Contenido Social Media (MVP)")
st.markdown("""
Herramienta potenciada por **Groq & Llama 3** para crear contenido de texto viral.
""")
st.markdown("---")

# --- LAYOUT PRINCIPAL ---
col1, col2 = st.columns([1, 2], gap="large")

# COLUMNA 1: CONFIGURACIÓN
with col1:
    st.header("1. Configuración")
    with st.container(border=True):
        tema = st.text_input("¿Sobre qué quieres escribir?", placeholder="Ej: Ciberseguridad en pymes")
        
        # Opciones alineadas con tu prompt_manager.py
        plataforma = st.selectbox(
            "Plataforma", 
            ["Twitter/X", "Blog Post", "Instagram", "SEO"]
        )
        
        audiencia = st.selectbox(
            "Audiencia Objetivo", 
            ["General", "Experto", "Infantil"]
        )

        st.write("") 
        generar_btn = st.button("✨ Generar Texto", type="primary", use_container_width=True)

# COLUMNA 2: RESULTADOS
with col2:
    st.header("2. Resultados")
    
    if generar_btn:
        if not tema:
            st.warning("⚠️ Por favor, escribe un tema antes de generar.")
        else:
            with st.spinner("🤖 La IA está pensando... (vía Groq)"):
                # Llamada al backend
                resultado_texto = generar_contenido(tema, plataforma, audiencia)
                
                # Guardar en session para no perderlo al interactuar
                st.session_state['resultado_texto'] = resultado_texto
                
    # Mostrar resultados si existen en memoria
    if 'resultado_texto' in st.session_state:
        texto_generado = st.session_state['resultado_texto']
        
        st.success("¡Contenido generado con éxito!")
        
        # Mostramos el texto directamente (ya no buscamos claves de diccionario)
        st.subheader(f"Borrador para {plataforma}")
        st.text_area("Copia tu contenido:", value=texto_generado, height=400)
        
        # Botón de descarga simple
        st.download_button(
            label="Descargar texto (.txt)",
            data=texto_generado,
            file_name="contenido_generado.txt",
            mime="text/plain"
        )
        
    else:
        st.info("Configura los parámetros a la izquierda y pulsa 'Generar'.")