
from flask import Flask, request, render_template, jsonify
import requests
import os

from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
DEEPL_API_KEY = 'YOUR_DEEPL_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    if filename.endswith('.pdf'):
        text = extract_text_from_pdf(filepath)
    else:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

    return jsonify({'text': text})

from pdfminer.high_level import extract_text

import re

import re

def clean_text(text):
    # inline 수식 $...$
    text = re.sub(r'\$(?:\\.|[^\$\\])*\$', '', text, flags=re.DOTALL)

    # display math $$...$$
    text = re.sub(r'\$\$(?:\\.|[^\$\\])*\$\$', '', text, flags=re.DOTALL)

    # \[ ... \] 수식
    text = re.sub(r'\\\[(?:.|\n)*?\\\]', '', text, flags=re.DOTALL)

    # \( ... \) 수식
    text = re.sub(r'\\\((?:.|\n)*?\\\)', '', text, flags=re.DOTALL)

    # 괄호 속 번호 제거 (예: (1), [2]) - 필요하면 유지하거나 삭제 가능
    text = re.sub(r'\(\d+\)', '', text)
    text = re.sub(r'\[\d+\]', '', text)

    # 중복 공백은 하나로 줄이기
    text = re.sub(r'\s{2,}', ' ', text)

    return text.strip()


def extract_text_from_pdf(pdf_path):
    
    try:
        text = extract_text(pdf_path)
        text = clean_text(text)
        return text
    except Exception as e:
        return f"[PDF 파싱 오류] {str(e)}"

@app.route('/translate', methods=['POST'])
def translate():
    word = request.json.get('word', '')
    response = requests.post(
        'https://api-free.deepl.com/v2/translate',
        data={
            'auth_key': DEEPL_API_KEY,
            'text': word,
            'target_lang': 'KO',
        }
    )
    result = response.json()
    return jsonify({'translated': result['translations'][0]['text']})

if __name__ == '__main__':
    os.makedirs('./uploads', exist_ok=True)
    app.run(debug=True)

