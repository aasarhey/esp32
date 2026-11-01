import os
import unicodedata
from flask import Flask, request, jsonify
import google.generativeai as genai

# Aici pornim serverul
app = Flask(__name__)

# Luam cheia secreta de la Gemini (o avem ascunsa pe Render, nu in cod)
api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def remove_diacritics(text):
    """
    Aceasta functie sterge diacriticele din text.
    De exemplu: "ș" devine "s", "ă" devine "a"
    Pentru ca ecranul tau OLED nu stie sa arate diacritice.
    """
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    # Inlocuiri specifice pentru romana
    for old, new in [('ă','a'), ('â','a'), ('î','i'), ('ș','s'), ('ț','t'),
                     ('Ă','A'), ('Â','A'), ('Î','I'), ('Ș','S'), ('Ț','T')]:
        text = text.replace(old, new)
    return text

# Aici primim poza de la ESP32-CAM
@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        # 1. Luam poza care a venit
        image_bytes = request.data
        
        # 2. Verificam daca a venit ceva
        if not image_bytes or len(image_bytes) == 0:
            return jsonify({"status": "error", "message": "Nicio imagine"}), 400
        
        # 3. Verificam daca e prea mare (maxim 10 MB)
        if len(image_bytes) > 10 * 1024 * 1024:
            return jsonify({"status": "error", "message": "Imagine prea mare"}), 413
        
        # 4. Verificam daca cheia API exista
        if not api_key:
            return jsonify({"status": "error", "message": "Lipseste cheia API"}), 500
        
        # 5. Aici e modelul de AI - IL LASAM ASA CUM AI TU
        model = genai.GenerativeModel('gemini-3.5-flash-lite')
        
        # 6. Pregatim imaginea pentru Gemini
        image_part = {
            "mime_type": "image/jpeg",
            "data": image_bytes
        }
        
        # 7. Ce intrebam Gemini
        prompt = "Analizeaza aceasta imagine si descrie scurt ce vezi in ea. Raspunde in limba romana."
        
        # 8. Trimitem la Gemini si asteptam raspunsul
        response = model.generate_content([image_part, prompt])
        
        # 9. Curatam raspunsul de diacritice
        clean_text = remove_diacritics(response.text)
        
        # 10. Trimitem raspunsul inapoi la ESP32-CAM
        return jsonify({
            "status": "success",
            "analysis": clean_text
        }), 200

    except Exception as e:
        # Daca apare orice eroare, spunem ce s-a intamplat
        return jsonify({
            "status": "error",
            "message": "Eroare server",
            "details": str(e)
        }), 500

# Aici verificam daca serverul e treaz (pentru testare)
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

# Pornim serverul
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
    
