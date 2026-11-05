import os
import unicodedata
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)


def remove_diacritics(text):
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')

    for old, new in [('ă','a'), ('â','a'), ('î','i'), ('ș','s'), ('ț','t'),
                     ('Ă','A'), ('Â','A'), ('Î','I'), ('Ș','S'), ('Ț','T')]:
        text = text.replace(old, new)

    return text


# ==========================================
# HEALTH CHECK - pentru UptimeRobot
# ==========================================
@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200


# ==========================================
# UPLOAD IMAGINE
# ==========================================
@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        image_bytes = request.data

        if not image_bytes or len(image_bytes) == 0:
            return jsonify({
                "status": "error",
                "message": "Nicio imagine"
            }), 400

        if len(image_bytes) > 10 * 1024 * 1024:
            return jsonify({
                "status": "error",
                "message": "Imagine prea mare"
            }), 413

        if not api_key:
            return jsonify({
                "status": "error",
                "message": "Lipseste cheia API"
            }), 500

        if not image_bytes.startswith(b'\xff\xd8'):
            return jsonify({
                "status": "error",
                "message": "Format invalid"
            }), 400

        model = genai.GenerativeModel('gemini-3.5-flash-lite')

        image_part = {
            "mime_type": "image/jpeg",
            "data": image_bytes
        }

        prompt = """Analizeaza cu atentie exercitiile/intrebarile de pe fotografie.

INSTRUCTIUNI SPECIFICE:

1. Identifica obiectul scolar (chimie, fizica, biologie, matematica etc.)

2. CHIMIE:
   - Scrie etapele si logica rezolvarii
   - Simbolul "niu" se scrie cu litere latine: niu
   - Volum = V
   - Volum molar = Vm
   - Partea de masa (procentaj) = W
   - Foloseste simboluri simple: / pentru impartit, * pentru inmultit
   - Delimiteaza ordinea operatiilor cu paranteze
   - Egalare reactii chimice OBLIGATORIE
   - Indici in compusi chimici: cifre simple (ex: H2SO4, Ca(OH)2)
   - Foloseste paranteze pentru grupari multiple (ex: Ca(OH)2)

3. FIZICA:
   - Frecventa = niu (scris cu litere latine)
   - Explica pasii de rezolvare

4. BIOLOGIE:
   - Pentru exercitii de asemanare/deosebire: specifica clar 3 asemanari si 3 deosebiri cu criterii clare
   - Exemplu: ADN vs ARN

5. INTREBARI ADEVARAT/FALS:
   - Raspunde cu explicatii complete

6. GENERAL:
   - Raspunsuri logice si verificate pentru a evita erori
   - Explica in cuvinte unde e nevoie
   - Foloseste doar caractere ASCII (fara diacritice, fara simboluri speciale)

Raspunde in limba romana, fara diacritice."""

        try:
            response = model.generate_content([image_part, prompt])
            clean_text = remove_diacritics(response.text)

            return jsonify({
                "status": "success",
                "analysis": clean_text
            }), 200

        except Exception as gemini_error:
            return jsonify({
                "status": "error",
                "message": "Gemini nu raspunde",
                "details": str(gemini_error)
            }), 503

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Eroare server",
            "details": str(e)
        }), 500


if __name__ == '__main__':
    # Pornim serverul simplu, fara gunicorn
    app.run(
        host='0.0.0.0',
        port=5000,
        threaded=True
    )
