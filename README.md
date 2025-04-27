Yapay Zeka Destekli Kod Üretici Uygulaması
Bu proje, Flask ile geliştirilmiş ve Ollama LLaMA3 modeliyle entegre edilmiş bir yapay zekâ destekli Python kod üretici uygulamasıdır.

Projenin Özellikleri:
- Kullanıcıdan aldığı promat'a göre Python kodu üretir.
- Üretilen kodu özetleyen kısa ve anlamı bir başlık ile sunar.
- Flask web arayüzü ile prompt gönderimi ve çıktı gösterimi sağlar.
- Ollama üzerinden LLaMA3 modeli kullanır. 
- Docker, Kubernetes (Minikube) ve Helm Chart ile dağıtım sağlanmıştır.

Kullanılan Teknolojiler:
- Python 3.10 
- Flask 
- Ollama (LLaMA 3 Modeli)
- HTML/CSS
- Docker
- Kubernetes + Minikube
- Helm

Projenin Yapısı:
ai-kod-uretici/
|
|- app.py
|- Dockerfile
|- requirements.txt
|- .dockerignore
|
|- templates/
| |- index.html
|
|- ai-kod-uretici-chart/
| |- Chart.yaml
| |- values.yaml
| |- templates/
|    |- deployment.yaml
|    |- service.yaml
|
|- ollama-deployment.yaml
|- ollama-service.yaml
|
|- README.md

Kurulum ve Çalıştırma Adımları:
1- Deployu klonlayın
```
git clone https://github.com/BeyzaCelik0/aiKodUretici.git
cd aiKodUretici
```
2- Docker imajı oluşturulması ve pushlanması
İlk olarak proje klasöründe terminal açarak Docker imajınızı oluşturun ve DockerHub'a pushlayın:
```
docker build -t <dockerhub-kullanici-adiniz>/ai-kod-uretici:latest .
docker push <dockerhub-kullanici-adiniz>/ai-kod-uretici:latest
```
3- Ollama sunucusunun kurulması
Ollama sunucusunu Kubernetes üzerinde deploy edin:
```
kubectl apply -f ollama-deployment.yaml
kubectl apply -f ollama-service.yaml
```
Ollama podu içerisine girip gerekli modeli çekin:
```
kubectl exec -it <ollama-pod-adı> -- bash
ollama pull llama3
exit
```
kubectl get pods komutuyla <ollama-pod-adı> kısmını öğrenebilirsiniz.
4- Helm Chart ile Uygulamanın Deploy Edilmesi
Helm chart klasörüne (ai-kod-uretici-chart/) girip uygulamayı deploy edin:
```
helm upgrade --install koduretici ./ai-kod-uretici-chart
```
Ardından Flask uygulamasını restart etmek için:
```
kubectl rollout restart deployment/ai-kod-uretici-chart
```
5- Port Yönlendirmesi (Port Forward)
Flask uygulamasına tarayıcıdan erişebilmek için:
```
kubectl port-forward service/ai-kod-uretici-chart-service 5000:80
```
Bu komut çalıştıktan sonra uygulama http://127.0.0.1:5000 veya http://localhost:5000 adresinden erişilebilir olacaktır.

Kullanım:
- Tarayıcınızda `http://127.0.0.1:5000` adresine gidin.
- Bir prompt girin ve "Kodu Üret" butonuna basın.
- Yapay zeka, verilen prompt'a göre Python kodunu ve başlığını üretecektir.

Bilgilendirme:
- Uygulama Ollama'nın Llama3 modelini kullandığı için yüksek RAM ihtiyacı vardır.
- Sağlıklı bir kullanım için bilgisayarınızda en az 8 GB RAM bulunması, tercihen 16 GB veya üzeri RAM kullanılması önerilir.
- 8 GB RAM ile model yüklenmeye çalışıldığında yetersiz bellek nedeniyle cevap alınamayabilir.

Uygulama Arayüzü
![Uygulama Arayüzü](arayuz.png)

Promt Örneği
Prompt: Login formu oluşturan Python kodu
Başlık: Simple Login Form
Kod: 
```
import tkinter as tk
from tkinter import messagebox

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        # Create widgets
        label_username = tk.Label(root, text="Username:")
        label_password = tk.Label(root, text="Password:")
        entry_username = tk.Entry(root)
        entry_password = tk.Entry(root, show="*")
        button_login = tk.Button(root, text="Login", command=self.login)

        # Place widgets
        label_username.grid(row=0, column=0)
        entry_username.grid(row=1, column=0)
        label_password.grid(row=2, column=0)
        entry_password.grid(row=3, column=0)
        button_login.grid(row=4, column=0)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Check if username and password are valid
        if username == "admin" and password == "password":
            messagebox.showinfo("Login", "Successful!")
        else:
            messagebox.showerror("Login", "Invalid credentials")

root = tk.Tk()
app = LoginForm(root)
root.mainloop()
```