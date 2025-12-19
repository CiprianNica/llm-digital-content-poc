'''
Docstring simulando IA 
'''
import random

def mock_llm_generator(prompt):
    '''
    Simula la llamada a un modelo de texto (Ollama/Llama3)
    '''
    return f"""Hola! Soy Llama 3 (Simulado). 
He analizado tu petición para crear contenido sobre el prompt recibido.
Aquí tienes una propuesta creativa basada en el análisis de tendencias recientes.
    
(Texto generado simulado de {len(prompt)} caracteres de longitud)."""

def mock_image_generation(prompt_imagen):
    '''
    Simula la generación de una imagen a partir de un prompt
    '''
    random_id = random.randint(1, 100)
    return f"https://picsum.photos/seed/{random_id}/800/400"
    