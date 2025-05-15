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

        try:
            response = requests.post("http://localhost:11434/api/generate", json={
                "model": "llama3",
                "prompt": full_prompt,
                "stream": False
            })

            json_response = response.json()
            print("Gelen JSON:", json_response)  # <<< BURADA BASTIRIYORUZ

            # HATA KONTROLÜ
            if "message" in json_response:
                result = json_response["message"]["content"]
                print("Yapay zekadan gelen sonuç:\n", result)

                try:
                    title = result.split("Başlık:")[1].split("Kod:")[0].strip()
                    code = result.split("Kod:")[1].strip()
                except Exception as e:
                    print(f"Başlık veya Kod ayrıştırılamadı: {e}")
                    code = result.strip()
            elif "error" in json_response:
                code = f"Hata: {json_response['error']}"
            else:
                code = f"Hata: Beklenmeyen cevap: {json_response}"
        except Exception as e:
            code = f"Sunucu hatası: {str(e)}"

    return render_template("index.html", title=title, code=code)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
