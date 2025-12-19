# 🚀 Digital Content Generator (PoC)

## 📋 Descripción del Proyecto
Este proyecto es una **Prueba de Concepto (PoC)** desarrollada para la empresa **Digital Content**. 

El objetivo es crear un sistema modular de **Inteligencia Artificial Generativa** capaz de automatizar la creación de contenido (texto e imágenes) para diversas plataformas sociales (LinkedIn, Twitter/X, Instagram y Blogs).

El sistema prioriza una arquitectura **extensible** y el uso de **recursos optimizados** (modelos locales o APIs gratuitas) para minimizar costes operativos durante la fase de validación.

---

## 🏗️ Arquitectura del Sistema
El proyecto sigue una arquitectura de **Monolito Modular**, separando claramente la interfaz de usuario, la lógica de negocio y los servicios de IA. Actualmente, el sistema utiliza una estrategia de **"Interface-First"**, empleando *mocking* (datos simulados) para validar el flujo de datos antes de conectar los LLMs reales.

### Estructura de Carpetas

```text
/digital-content-poc
│
├── venv/                 # Entorno virtual (Librerías y dependencias aisladas)
│
├── front/                # CAPA DE PRESENTACIÓN (Frontend)
│   └── app.py            # Interfaz de usuario construida con Streamlit via Python
│
├── back/                 # CAPA DE LÓGICA (Backend)
│   ├── __init__.py       # Convierte la carpeta en un paquete importable
│   ├── generador.py      # Orquestador: Recibe inputs del front y coordina la IA
│   └── llm_service.py    # Adaptador AI: Conexión con modelos (Ollama, APIs, etc.)
│
├── .gitignore            # Archivos que no se suben al repositorio (ej: venv)
├── requirements.txt      # Lista de dependencias del proyecto
└── README.md             # Documentación del proyecto
```

### 🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.x

Frontend: Streamlit (para prototipado rápido de UI)

Backend Logic: Python puro (modular)

IA (Simulada/Futura):

Texto: Llama 3 / Mistral (vía Ollama o Groq)

Imagen: Stable Diffusion / Flux

Orquestación: LangChain (planificado para fase 2)

### 🚀 Cómo ejecutar el proyecto
Sigue estos pasos para levantar la aplicación en tu entorno local:

Clona o descarga el repositorio y entra en la carpeta del proyecto.

Crear y activar el entorno virtual (ejemplos):

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación (Streamlit):

```bash
streamlit run front/app.py
```
🔮 Roadmap / Próximos Pasos

[x] Fase 1: Diseño de Arquitectura y UI (Interface-First).

[ ] Fase 2: Conexión con Ollama (Reemplazo de Mocks por Llama 3).

[ ] Fase 3: Implementación de Prompts Dinámicos según red social.

[ ] Fase 4: Integración de generación de imágenes real.


