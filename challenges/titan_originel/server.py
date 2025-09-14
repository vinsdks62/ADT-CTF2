from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

FLAG_FILE = './flag.txt'
with open(FLAG_FILE, 'w') as f:
    f.write('ESD{TITAN_ORIGINEL_RCE}')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template_string('''
        <h1>Titan Originel RCE Challenge</h1>
        <form method="post" action="/upload" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    ''')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return '<pre>Error: No file part</pre>'
    file = request.files['file']
    if file.filename == '':
        return '<pre>Error: No selected file</pre>'
    if file and allowed_file(file.filename):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        # RCE simulation: execute code if payload present in filename (for simplicity)
        if file.filename == 'read_flag.png':
            try:
                with open(FLAG_FILE) as f:
                    flag = f.read()
                return f'<pre>Flag: {flag}</pre>'
            except Exception as e:
                return f'<pre>Error: {e}</pre>'
        return f'<pre>File uploaded: {file.filename}</pre>'
    return '<pre>Error: File not allowed</pre>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
