import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route('/', methods=['GET'])
def home():
    return "Serverul ESP32-CAM este activ și pregătit!"

@app.route('/upload', methods=['POST'])
def receive_image():
    if 'image' not in request.files:
        return jsonify({"error": "Nicio imagine trimisă"}), 400
    
    image_file = request.files['image']
    image_bytes = image_file.read()

    try:
        model = genai.GenerativeModel('gemini-3.5-flash-lite')
        response = model.generate_content([
            "Analizează această imagine trimisă de ESP32-CAM și descrie ce vezi pe scurt:",
            {"mime_type": "image/jpeg", "data": image_bytes}
        ])
        
        return jsonify({"status": "success", "analysis": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
