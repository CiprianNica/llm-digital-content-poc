import os
from dotenv import load_dotenv
from openai import OpenAI
from back.llm_service import mock_image_generation, mock_llm_generator
from back.prompt_manager import construir_prompt


# Cargar variables de entorno
load_dotenv()

# Cliente OpenAI (inicialización perezosa)
_client = None

def _init_client():
    global _client
    if _client is not None:
        return _client
    
    api_key=os.getenv("GROQ_API_KEY")
    if not api_key:
        print("GROQ_API_KEY no está configurada. Usando generador simulado (mock).")
        _client = None
        return None
    try:
        _client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1",
        )
        return _client
    except Exception as e:
        print(f"OpenAI client init error: {e}. Falling back to mock generator.")
        return None

def generar_contenido(tema, plataforma, audiencia):
    prompt = construir_prompt(tema, plataforma, audiencia)

    # Intentar inicializar el cliente si es necesario
    client = _init_client()
    
    if client is None:
        # Fallback al mock si no hay cliente disponible
        print("Usando generador simulado (mock) porque el cliente OpenAI no está disponible.")
        return mock_llm_generator(prompt)

    try:
        print(f"DEBUG: Enviando a Groq: {prompt}")
        respuesta = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": f"Eres un asistente de redaccion util y creativo."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7,
        )
        texto_generado = respuesta.choices[0].message.content
        return texto_generado
    
    except Exception as e:
        print(f"Error al generar contenido con Groq: {str(e)}. Usando mock en su lugar.")
        return mock_llm_generator(prompt)

# Mock
def procesar_solicitud(tema, plataforma, audiencia):
    '''
    funcion que llama el front
    '''
    prompt_sistema = f"Eres un experto en Marketing Digital para {plataforma}."
    prompt_usuario = f"Genera una publicación creativa sobre '{tema}' dirigida a '{audiencia}'."
    prompt_completo = f"{prompt_sistema}\n{prompt_usuario}"
    
    # Llamadas simuladas a los servicios de LLM e imagen
    texto_generado = mock_llm_generator(prompt_completo)
    imagen_generada = mock_image_generation(tema)
    
    return {
        "texto": texto_generado,
        "imagen_url": imagen_generada,
        "meta": {
            "modelo": "Llama_3_Simulado",
            "modelo_img": "Picsum_Photos_Simulado",
            "plataforma": plataforma
        }
    }
    