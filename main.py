from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware #cors para permitir conexión entre dominios
import requests
import os

load_dotenv() #carga el archivo .env
SUPABASE_URL= os.getenv("SUPABASE_URL")
SUPABASE_KEY= os.getenv("SUPABASE_SERVICE_ROLE_KEY")

# prueba de que se cargan correctamente las variables de entorno
# print(SUPABASE_URL)
# print(SUPABASE_KEY)
# print('prueba variables')

app = FastAPI()
app.title = 'API CHATBOT E-COMMERCE'

# MIDDLEWARE CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Dominio del chatbot, por el momento local
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class logs_chat(BaseModel):
    id_conversacion: str
    id_usuario: str
    rol: str
    mensaje: str
    fecha: datetime

@app.post("/logs", tags=['Chatbot'])
def create_log(log:logs_chat):
    #convertimos a dicc y despues en una lista
    data = [{
        **log.dict(),
        "fecha":log.fecha.isoformat()}] # formato válido para json

    headers = {
        "apikey" : SUPABASE_KEY, 
        "Authorization": f"Bearer {SUPABASE_KEY}", 
        "Content-Type": "application/json",
        "Prefer": "return=minimal"

    }
    
    response = requests.post(f"{SUPABASE_URL}/rest/v1/logs_chat", headers=headers, json=data)

    if response.status_code in [200, 201, 204]:
        print("✅ Log enviado a Supabase")
    else:
        print(f"❌ Error al enviar log: {response.status_code}")
        print(response.text)

    return {"status": response.status_code}



# documentacion supabase para insert rows
# curl -X POST 'https://bupbptppncwasereiuea.supabase.co/rest/v1/logs_chat' \
# -H "apikey: SUPABASE_KEY" \
# -H "Authorization: Bearer SUPABASE_KEY" \
# -H "Content-Type: application/json" \
# -H "Prefer: return=minimal" \
# -d '{ "some_column": "someValue", "other_column": "otherValue" }'