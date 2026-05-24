import google.generativeai as genai

API_KEY = "AIzaSyCWkeg4OYh8wpKlxkfPCPpYn-SWV5JjV_w"

genai.configure(api_key=API_KEY)

print("Daftar model yang diizinkan untuk kuncimu:")
for m in genai.list_models():
    if 'generateContent' in m.supported_methods:
        print(f"Nama Model: {m.name}")