from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    title = ""
    code = ""

    if request.method == "POST":
        prompt = request.form["prompt"]
        print("Kullanıcıdan gelen prompt:", prompt)

        system_prompt = """
Sen bir Python geliştirici asistanısın.
Kullanıcıdan gelen isteğe göre Python kodu üret.
Ayrıca bu kodu özetleyen kısa bir başlık da döndür.
Cevap formatı şu şekilde olmalı:
---
Başlık: <kısa başlık>
Kod:
<code bloğu>
---"""
        full_prompt = f"{system_prompt}\nİstek: {prompt}"

        response = requests.post("http://localhost:11434/api/chat", json={
            "model": "llama3",
            "messages": [{"role": "user", "content": full_prompt}],
            "stream": False
        })

        result = ""
        for line in response.iter_lines():
            if line:
                json_line = line.decode("utf-8")
                try:
                    content_piece = eval(json_line).get("message", {}).get("content", "")
                    result += content_piece
                except:
                    continue
        result = response.json()["message"]["content"]
        print("Yapay zekadan gelen sonuç:\n", result)

        try:
            title = result.split("Başlık:")[1].split("Kod:")[0].strip()
            code = result.split("Kod:")[1].strip()
        except:
            code = result.strip()

    return render_template("index.html", title=title, code=code)

if __name__ == "__main__":
    app.run(debug=True)

