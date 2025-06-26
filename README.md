# FastAPI Chatbot con Supabase 

Esta API recibe logs desde un [chatbot](https://github.com/Halsey26/chat_demo_ecommerce) y los envía a una base de datos Supabase.

## Instalación local

```bash
git clone https://github.com/tuusuario/chatbot-api.git
cd chatbot-api
pip install -r requirements.txt
```


---
## Para trabajar con supabase

### Librerias necesarias
En el entorno virtual
```
pip install pydantic<2 requests python-dotenv
```

---
### Configuración adicional

1. Crear el archivo .env 
En la raíz del proyecto, crea un archivo llamado `.env` y coloca dentro tu clave de API de Supabase:

```
SUPABASE_URL=sk-...
SUPABASE_SERVICE_ROLE=
```
⚠️ Nunca compartas públicamente tu clave de API.

---
## NOTAS:
1. En supabase: En un proyecto debes crear una tabla con la misma estructura:
- id_conversacion: text
- id_usuario: text
- rol: text
- mensaje: text
- fecha: timestamp

    Luego de crear una tabla, ejemplo: `logs_chat`.
Obtener las api key y almacenarla en .env

2. Para el deploy en Render/Railway
- Comando Start: 
    `uvicorn main:app --host 0.0.0.0 --port 8000`