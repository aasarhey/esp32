
  
import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configurarea cheii API pentru Gemini (preluată din variabilele de mediu de pe Render)
# Asigură-te că ai setat GEMINI_API_KEY în panoul de control Render.
api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        # Preluăm datele binare trimise direct în corpul cererii de ESP32-CAM
        image_bytes = request.data
        
        if not image_bytes or len(image_bytes) == 0:
            return jsonify({
                "status": "error",
                "message": "Nicio imagine trimisă sau corpul cererii este gol."
            }), 400

        # Verificăm dacă cheia API este configurată
        if not api_key:
            return jsonify({
                "status": "error",
                "message": "Cheia GEMINI_API_KEY nu este configurată pe server."
            }), 500

        # Inițializăm modelul Gemini (folosind un model multimodal compatibil, ex: gemini-1.5-flash)
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Pregătim imaginea pentru a fi trimisă către Gemini (folosind formatul binar raw)
        image_part = {
            "mime_type": "image/jpeg",
            "data": image_bytes
        }

        # Generăm conținutul / analiza imaginii
        prompt = "Analizează această imagine și descrie scurt ce vezi în ea."
        response = model.generate_content([image_part, prompt])

        # Returnăm răspunsul obținut de la Gemini către ESP32
        return jsonify({
            "status": "success",
            "analysis": response.text
        }), 200

    except Exception as e:
        # Prindem orice eroare neprevăzută (ex: eroare de rețea cu API-ul Gemini, eroare de model, etc.)
        return jsonify({
            "status": "error",
            "message": "Eroare internă pe server în timpul procesării.",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
