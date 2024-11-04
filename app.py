from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjNiYmYxZmY1LWVlN2QtNGY4ZC05ZDExLTA4NmFkZWExZTRlMiIsImlzRGV2ZWxvcGVyIjp0cnVlLCJpYXQiOjE3MzAxMjQyNzEsImV4cCI6MjA0NTcwMDI3MX0.i9of9H22RCbDQ52RTOKqCoq7RwOYIgjJ4K9H-GlrOF0'
BASE_URL = 'https://bothub.chat/api/v2/openai/v1'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    rhyme_type = request.json.get('rhyme_type', 'парная')

    # Формируем инструкцию для ChatGPT в зависимости от выбранного типа рифмы
    rhyme_instruction = f"Используй {rhyme_type} рифму в стихах."

    # Формирование запроса к BotHub
    response = requests.post(
        f"{BASE_URL}/chat/completions",
        headers={
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        },
        json={
            'model': 'gpt-3.5-turbo',
            'messages': [
                {'role': 'system', 'content': "Ты помогатор для написания стихов."},
                {'role': 'user', 'content': f"{rhyme_instruction}\n{user_message}"}
            ]
        }
    )

    if response.status_code == 200:
        reply = response.json()['choices'][0]['message']['content']
        return jsonify({"reply": reply})
    else:
        return jsonify({"reply": "Ошибка: " + response.text}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
