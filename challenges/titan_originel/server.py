#!/usr/bin/env python3
import os
from flask import Flask, request, send_from_directory
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = "./uploads"
FLAG_FILE = "./flag_originel.txt"

# Crée le dossier uploads s'il n'existe pas
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Route pour servir le fichier caché
@app.route('/hidden/<path:filename>')
def serve_hidden(filename):
    # Sert uniquement les fichiers existants dans uploads
    return send_from_directory(UPLOAD_FOLDER, filename)

# Route d'upload
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return '<pre>Error: No file part</pre>'
    file = request.files['file']
    if file.filename == '':
        return '<pre>Error: No selected file</pre>'

    if file and file.filename.lower().endswith(".png"):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Lecture des métadonnées PNG
        try:
            img = Image.open(filepath)
            png_meta = img.info
        except Exception as e:
            return f'<pre>Error reading PNG: {e}</pre>'

        # Vérification de la clé
        if 'originel_key' in file.filename or any('originel_key' in str(v) for v in png_meta.values()):
            try:
                with open(FLAG_FILE) as f:
                    flag = f.read().strip()
                return f'<pre>Flag: {flag}</pre>'
            except Exception as e:
                return f'<pre>Error reading flag: {e}</pre>'

        return f'<pre>File uploaded: {file.filename}</pre>'

    return '<pre>Error: File not allowed</pre>'

# Route racine pour test simple
@app.route('/')
def index():
    return '<h1>Titan Originel Challenge</h1><p>Upload your PNG to /upload</p>'

if __name__ == "__main__":
    # Fichier de test du flag
    if not os.path.exists(FLAG_FILE):
        with open(FLAG_FILE, 'w') as f:
            f.write("ESD{TITAN_ORIGINEL_RCE}")

    app.run(host='0.0.0.0', port=9000)
