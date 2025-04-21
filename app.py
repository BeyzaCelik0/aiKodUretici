from flask import Flask, request, render_template
import ollama

app = Flask(__name__)

SYSTEM_PROMPT = """
Sen bir Python geliştirici asistanısın.
Kullanıcıdan gelen isteğe göre Python kodu üret.
Ayrıca bu kodu özetleyen kısa bir başlık da döndür.
Cevap formatı şu şekilde olmalı:
---
Başlık: <kısa başlık>
Kod:
<code bloğu>
---
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    title = ""
    code = ""
    response = ""
    if request.method == 'POST':
        user_prompt = request.form['prompt']
        full_prompt = SYSTEM_PROMPT + "\nİstek: " + user_prompt
        response = ollama.chat(model='llama3', messages=[
            {"role": "user", "content": full_prompt}
        ])
        content = response['message']['content']
        try:
            title = content.split('Başlık:')[1].split('Kod:')[0].strip()
            code = content.split('Kod:')[1].strip()
        except:
            code = content  # fallback
    return render_template('index.html', title=title, code=code, response=response)

if __name__ == '__main__':
    app.run(debug=True)
