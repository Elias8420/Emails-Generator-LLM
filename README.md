# Emails-Generator-LLM

# Generador de Emails de Phishing con IA — Laboratorio de Ciberseguridad

Herramienta educativa que utiliza modelos LLM (Llama 3.3 vía Groq API) para generar correos de phishing realistas, diseñada para laboratorios de ciberseguridad donde los estudiantes aprenden a **identificar y analizar amenazas generadas con IA**.

> ⚠️ **Uso exclusivamente educativo.** Este proyecto fue desarrollado para un laboratorio de seguridad con el objetivo de entrenar a usuarios en la detección de phishing generado con inteligencia artificial.

## ¿Para qué sirve?

El phishing generado con IA es una amenaza creciente en entornos bancarios y corporativos. Esta herramienta permite:

- Generar ejemplos realistas de correos de phishing simulando empresas conocidas
- Ajustar la calidad del modelo según el nivel de realismo requerido
- Usar los correos generados como casos de estudio para entrenar equipos en detección de amenazas
- Analizar qué características hacen convincente a un correo malicioso

## Tecnologías

- **Groq API** — Acceso a modelos LLM de alta velocidad
- **Llama 3.3** (8B y 70B) — Modelos de lenguaje para generación de texto
- **Gradio** — Interfaz web interactiva
- **python-dotenv** — Manejo seguro de credenciales

## Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/Elias8420/Emails-Generator-LLM
cd phishing-llm-lab
```

### 2. Instalar dependencias
```bash
pip install groq gradio python-dotenv
```

### 3. Configurar la API Key
Creá un archivo `.env` en la raíz del proyecto:
```
GROQ_API_KEY=tu_api_key_aqui
```
Obtené tu API key gratuita en [console.groq.com](https://console.groq.com)

### 4. Ejecutar
```bash
python phishing_generator.py
```

## Modelos disponibles

| Alias | Modelo | Uso |
|-------|--------|-----|
| `rapido` | llama-3.3-8b-instant | Pruebas rápidas |
| `balanceado` | llama-3.3-70b-versatile | Uso general |
| `mejor` | llama-3.3-70b-versatile | Máximo realismo |

## Parámetros clave

- **`temperature: 0.85`** — Controla la creatividad del modelo. Valores más altos generan texto más variado y menos predecible
- **`max_tokens: 1000`** — Limita el largo de la respuesta (~750 palabras)
- **`system prompt`** — Define el rol del modelo como experto en ciberseguridad generando ejemplos de entrenamiento