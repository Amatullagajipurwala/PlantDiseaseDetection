

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

# 🔐 Configure Gemini API
# genai.configure(api_key="AIzaSyBb-PAjtBT0GFsupf_0DDI5jksXWK1zvYs")
genai.configure(api_key="AIzaSyAmmQmZMqMagDsFXStjSi-UcX6wbajyhLs")      
# 🌱 Create app instance
app = FastAPI()

# 🌍 Enable CORS for frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with ["http://localhost:3000"] for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✨ Define Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

@app.get("/recommend")
def get_recommendation(
    disease: str = Query(..., title="Plant Disease"),
    language: str = Query("english", title="Language")
):
    prompt = (
        f"What is the best treatment for {disease} in plants? Provide a YouTube video link if available. "
        f"Respond in {language}."
    )

    print("🚀 Prompt:", prompt)

    try:
        response = model.generate_content(prompt)
        print("✅ Gemini response received")
        print("🔧 Raw response:", response)

        recommendation = response.text.strip()
        return {
            "disease": disease,
            "recommendation": recommendation,
            "language": language
        }
    except Exception as e:
        print("❌ Error calling Gemini API:", str(e))
        return {"error": str(e)}
