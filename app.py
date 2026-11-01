import os
import unicodedata
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def remove_diacritics(text):
    """Sterge diacriticele din text."""
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    for old, new in [('ă','a'), ('â','a'), ('î','i'), ('ș','s'), ('ț','t'),
                     ('Ă','A'), ('Â','A'), ('Î','I'), ('Ș','S'), ('Ț','T')]:
        text = text.replace(old, new)
    return text

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        image_bytes = request.data
        
        # Verificari de baza
        if not image_bytes or len(image_bytes) == 0:
            return jsonify({
                "status": "error", 
                "message": "Serverul este treaz, dar nu a primit nicio imagine."
            }), 400
            
        if len(image_bytes) > 10 * 1024 * 1024:
            return jsonify({
                "status": "error", 
                "message": "Imaginea este prea mare. Max 10 MB."
            }), 413
        
        if not api_key:
            return jsonify({
                "status": "error", 
                "message": "Serverul nu are cheia API configurata."
            }), 500
        
        # Verificare daca este JPEG valid
        if not image_bytes.startswith(b'\xff\xd8'):
            return jsonify({
                "status": "error", 
                "message": "Fisierul primit nu este o imagine JPEG valida."
            }), 400

        # Modelul Gemini - il lasam asa cum ai zis ca merge
        model = genai.GenerativeModel('gemini-3.5-flash-lite')
        
        image_part = {
            "mime_type": "image/jpeg",
            "data": image_bytes
        }
        
        prompt = "Analizeaza aceasta imagine si descrie scurt ce vezi in ea. Raspunde in limba romana."
        
        # Aici e trucul: daca Gemini doarme sau e lent, prindem eroarea si spunem frumos
        try:
            response = model.generate_content([image_part, prompt])
            clean_text = remove_diacritics(response.text)
            
            return jsonify({
                "status": "success",
                "analysis": clean_text
            }), 200
            
        except Exception as gemini_error:
            # Daca Gemini nu raspunde, nu aruncam eroare tehnica, spunem frumos
            return jsonify({
                "status": "error",
                "message": "Serverul este treaz, dar Gemini nu a raspuns. Incearca din nou.",
                "details": str(gemini_error)
            }), 503  # 503 = Service Unavailable (serverul e ocupat momentan)

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Eroare interna pe server.",
            "details": str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "ok", 
        "message": "Serverul functioneaza. Poti trimite imagini."
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
  
