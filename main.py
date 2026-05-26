from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from services.detection import process_traffic_video, process_traffic_image
from services.advisor import get_traffic_advice

app = FastAPI(title="TrafficSense API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GEMINI_API_KEY = "GANTI PAKE KODE API PUNYAMU SENDIRI"

@app.get("/")
def read_root():
    return {"message": "TrafficSense API is running!"}

@app.post("/api/v1/analyze")
async def analyze_traffic(
    file: UploadFile = File(...),
    line_y: int = Form(None)
):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        content_type = file.content_type
        
        if content_type.startswith('video/'):
            hasil_analisis = process_traffic_video(temp_path, line_y)
        elif content_type.startswith('image/'):
            hasil_analisis = process_traffic_image(temp_path)
        else:
            raise Exception("Format file tidak didukung. Harap unggah Gambar (JPG/PNG) atau Video (MP4).")

        status_jalan = hasil_analisis["kemacetan"]["status"]
        total_kendaraan = hasil_analisis["total_kendaraan"]
        
        pesan_ai = get_traffic_advice(total_kendaraan, status_jalan, GEMINI_API_KEY)
        
        hasil_analisis["pesan_ai_advisor"] = pesan_ai

        os.remove(temp_path)
        return {
            "status": "success",
            "data": hasil_analisis
        }
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return {"status": "error", "message": str(e)}