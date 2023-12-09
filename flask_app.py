from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Mendapatkan informasi pengguna
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    # Menampilkan informasi pengguna di log terminal
    print(f"IP: {user_ip}, User-Agent: {user_agent}")

    return render_template('index.html')

if __name__ == '__main__':
    # Menentukan port yang ingin Anda expose
    port = 5000  # Ganti dengan nomor port yang diinginkan

    # Menjalankan aplikasi Flask
    app.run(port=port, debug=True)
