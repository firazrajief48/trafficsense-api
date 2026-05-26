pip install -r requirements.txt : Install Library (Wajib)
pip install google-generativeai : Library Gemini
pip install -U google-genai : Kalo Library Gemini Gagal Pake Ini
pip install --upgrade protobuf : Install Protobuf
pip install --upgrade tensorflow : Update Tensorflow

py -3.11 -m venv venv : (Create VENV Python 3.11, Instal Dulu Jika Tidak Ada)
.\venv\Scripts\activate : On VENV
Running API : uvicorn main:app --reload
http://127.0.0.1:8000/docs : UI Trafficsense API (Post > Try It Out > Upload Gambar/Video > Execute)
http://127.0.0.1:8000 : Cek API Aktif/Tidak Aktif

# Jangan Lupa Isi API Gemini di main.py, Ambil di Google Studio Sendiri Hehe

# VENV Wajib Nyala Kalau Mau Start API!

Kalau Library Tensorflow Garis Kuning Bawah Edit File (.vscode/settings.json)
Tambahin/Ubah Bagian :
{
    "python.analysis.diagnosticSeverityOverrides": {
        "reportMissingModuleSource": "none"
    }
}