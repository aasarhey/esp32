import os
from flask import Flask, request, render_template_string, Response

app = Flask(__name__)

# Variabila globala care va retine ultima imagine primita de la ESP32-CAM
latest_image = None

# ==========================================
# PAGINA WEB PENTRU VIZUALIZARE LIVE / FOCUS
# ==========================================
@app.route('/', methods=['GET'])
def index():
    html_page = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ESP32-CAM Live View & Focus</title>
        <meta http-equiv="refresh" content="2"> <!-- Se reface pagina automat la fiecare 2 secunde -->
        <style>
            body { font-family: Arial, sans-serif; text-align: center; background: #222; color: #fff; margin-top: 30px; }
            img { max-width: 100%; height: auto; border: 4px solid #444; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
            .info { margin: 15px; font-size: 18px; color: #aaa; }
        </style>
    </head>
    <body>
        <h1>ESP32-CAM Live View (Focus Adjust)</h1>
        <div class="info">Mod Preview Activ. Pagina se actualizeaza automat la fiecare 2 secunde.</div>
        <div>
            <img src="/image.jpg" alt="Ultima imagine capturata de ESP32">
        </div>
    </body>
    </html>
    """
    return render_template_string(html_page)


# ==========================================
# RUTA PENTRU AFISAREA IMAGINII JPEG BRUTE
# ==========================================
@app.route('/image.jpg', methods=['GET'])
def get_latest_image():
    global latest_image
    if latest_image:
        return Response(latest_image, mimetype='image/jpeg')
    else:
        return "Nicio imagine capturată încă.", 404


# ==========================================
# HEALTH CHECK - pentru UptimeRobot
# ==========================================
@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200


# ==========================================
# UPLOAD IMAGINE DE LA ESP32 (DOAR PREVIEW)
# ==========================================
@app.route('/upload', methods=['POST'])
def upload_image():
    global latest_image
    try:
        image_bytes = request.data

        if not image_bytes or len(image_bytes) == 0:
            return "Nicio imagine", 400

        if not image_bytes.startswith(b'\xff\xd8'):
            return "Format invalid", 400

        # Salvam imaginea in memorie pentru preview in browser
        latest_image = image_bytes
        print(f"Imagine primita cu succes! Dimensiune: {len(image_bytes)} octeti")

        # Trimitem text simplu care va aparea direct pe ecranul OLED al ESP32-CAM
        return "Preview OK", 200

    except Exception as e:
        return "Eroare server", 500


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        threaded=True
    )
    
