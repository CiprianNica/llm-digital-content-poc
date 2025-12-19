from back.llm_service import mock_image_generation, mock_llm_generator

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
    