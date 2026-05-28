import gradio as gr
import os
from dotenv import load_dotenv
# groq es el servicio de API para usar modelos LLM
from groq import Groq

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY") # Reemplazar con la API Key generada
# Configure Groq client
client = Groq(api_key=API_KEY)

# Clase para generar emails usando Groq, para solo acceder directamente con
#el nombre
# de la funcion que se quiere usar
class GeneradorEmailsGroq:
 # Esta funcion es solo para seleccionar el modelo que se quiere usar
 def __init__(self, api_key: str):
  self.client = Groq(api_key=api_key)
  self.modelos = {
  "rapido": "llama-3.3-8b-instant",
  "balanceado": "llama-3.3-70b-versatile",
  "mejor": "llama-3.3-70b-versatile"
  }

 # Esta es la funcion que concina el correo
 def generar_email(
 self,
 tipo: str,
 categoria: str = "phishing",
 calidad: str = "balanceado"
 ) -> str:

  if categoria == "phishing":
    #Le dice al modelo en que se tiene que basar para hacer las
    #respuestas
    system = "Eres experto en ciberseguridad generando ejemplos realistas de phishing para entrenamiento."
    #Aqui esta el prompot que se hace, cambialo si quioeres que haga
    #algo extra op si queres que omita alguna parte
    prompt = f"""Actúa como un experto en ciberseguridad creando un
    ejemplo realista de phishing.
    Genera un email de phishing simulando ser {tipo} que sea tan convincente que
    parezca completamente real.
    El email debe:
    - Tener un asunto que haga que alguien quiera abrirlo inmediatamente
    - Explicar un problema urgente con {tipo}, ya sea una cuenta comprometida, un
    pago fallido, o una actualización necesaria
    - Incluir números de caso, fechas, y referencias que suenen oficiales
    - Si incluyes algun plan o que involucre dinero, utiliza montos o
    suscripciones que maneja {tipo}
    - No incluyas datos como 12345, utiliza numeros que sean creibles y utiliza
    fechas que sean cercanas a octubre del 2025
    - Decir exactamente qué deben hacer (verificar, actualizar, etc.)
    - Usar https://home-stats-pi.vercel.app/ donde normalmente irían los links
    maliciosos
    - Terminar con una firma profesional de {tipo} con teléfono de soporte si
    tiene contacto de soporte, caso contrario. no incluir la linea de numero de
    contacto de soporte
    El tono debe ser: profesional, urgente sin ser alarmista, y completamente
    creíble.
    Genera el email completo sin explicaciones adicionales."""
  else:
    system = "Genera emails legítimos y naturales."
    prompt = f"Genera un email legítimo de tipo {tipo}. Solo el email."

  try:
    response = self.client.chat.completions.create(
    model=self.modelos[calidad],
    messages=[
    {"role": "system", "content": system},
    {"role": "user", "content": prompt}
    ],
    # Esto le indica que tan creativo tendria que ser con las
    #respuestas que de
    temperature=0.85,
    # Aqui le indica cuantas palabras tiene que generar, con 1000
    # son aproximadamente 750 palabras
    max_tokens=1000
    )
    # retorna el texto que genero el modelo desde la api
    return response.choices[0].message.content

  except Exception as e:
    print(f"Error: {e}")
    return None

if __name__ == "__main__":
 generador = GeneradorEmailsGroq(api_key=API_KEY)
 # Aqui poder cambiar el parametro que dice netflix para que pruebe con
#otras empresas
 email = generador.generar_email("Netflix", "phishing", "mejor")
 # Si genero un correo lo mostrara
 if email:
  print("\n")
  print(email)

def generar_email_gradio(nombre_empresa, categoria, calidad):
 generador = GeneradorEmailsGroq(api_key=API_KEY)
 email = generador.generar_email(nombre_empresa, categoria, calidad)
 return email

iface = gr.Interface(
 fn=generar_email_gradio,
 inputs=[
  gr.Textbox(label="Nombre de la empresa"),
  gr.Radio(["phishing", "legitimo"], label="Categoría del email"),
  gr.Dropdown(["rapido", "balanceado", "mejor"], label="Calidad del modelo")
 ],
 outputs=gr.Textbox(label="Email Generado", elem_id="email_output",
  lines=10)
)

iface.launch()
