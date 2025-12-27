# prompt_manager.py

def construir_prompt(tema, plataforma, audiencia):
    """
    Genera un prompt estructurado basado en los parámetros del usuario.
    """
    
    # 1. Definir perfiles de audiencia (Tono y Estilo)
    perfiles = {
        "Infantil": "Usa un tono alegre, simplifica conceptos complejos, usa analogías divertidas y emojis.",
        "Experto": "Usa terminología técnica precisa, ve al grano, prioriza datos y análisis profundo.",
        "General": "Usa un tono cercano pero informativo, accesible para cualquier persona, evita jerga complicada."
    }
    
    # 2. Definir restricciones de plataforma (Formato y Estructura)
    formatos = {
        "Twitter/X": "Crea un hilo de 3 a 5 tweets. Sé provocativo, usa ganchos al inicio y hashtags relevantes al final.",
        "Blog Post": "Escribe un artículo estructurado con introducción, subtítulos (H2) y conclusión. Mínimo 500 palabras. Optimizado para lectura en web.",
        "Instagram": "Escribe un pie de foto (caption) atractivo. Usa saltos de línea para que sea legible. Incluye una llamada a la acción (CTA) y 10 hashtags estratégicos.",
        "SEO": "Redacta un texto enfocado en posicionamiento. Incluye la palabra clave principal en el primer párrafo. Estructura clara para snippets de Google."
    }

    # 3. Selección segura (fallback por si falla algo)
    estilo_audiencia = perfiles.get(audiencia, perfiles["General"])
    instrucciones_plataforma = formatos.get(plataforma, formatos["Blog Post"])

    # 4. Construcción del Prompt Final (System Prompt + User Prompt)
    prompt_sistema = f"""
    Actúa como un experto creador de contenido digital y copywriter de clase mundial.
    Tu objetivo es redactar contenido sobre el tema: '{tema}'.
    
    AUDIENCIA OBJETIVO: {audiencia}.
    Directriz de estilo: {estilo_audiencia}
    
    PLATAFORMA: {plataforma}.
    Directrices de formato: {instrucciones_plataforma}
    """

    return prompt_sistema