Bu proje, Flask ile geliştirilmiş ve Ollama LLaMA3 modeliyle entegre edilmiş bir yapay zekâ destekli Python kod üretici uygulamasıdır.

Projenin Özellikleri:
-Kullanıcıdan aldığı promat'a göre Python kodu üretir.
-Üretilen kodu özetleyen kısa ve anlamı bir başlık ile sunar.
-Basit ve sade arayüz.

Kullanılan Teknolojiler:
-Python 3.10 
-Flask 
-Ollama (LLaMA 3 Modeli)
-HTML

Kurulum:
```bash
git clone https://github.com/BeyzaCelik0/aiKodUretici.git
cd aiKodUretici
pip install -r requirements.txt
ollama run llama3
python app.py

Kullanım:
-Uygulamayı başlatmak için `python app.py` komutunu çalıştırın.
-Tarayıcınızda `http://127.0.0.1:5000` adresine gidin.
-Bir prompt girin ve "Kodu Üret" butonuna basın.
-Yapay zeka, verilen prompt'a göre Python kodunu ve başlığını üretecektir.