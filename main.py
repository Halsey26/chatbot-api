from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from dotenv import load_dotenv
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
app.title = 'API CHATBOT - FASTAPI - SUPABASE'

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


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

# documentacion supabase para insert rows
# curl -X POST 'https://bupbptppncwasereiuea.supabase.co/rest/v1/logs_chat' \
# -H "apikey: SUPABASE_KEY" \
# -H "Authorization: Bearer SUPABASE_KEY" \
# -H "Content-Type: application/json" \
# -H "Prefer: return=minimal" \
# -d '{ "some_column": "someValue", "other_column": "otherValue" }'