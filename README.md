# 🌿 FarmEase – Plant Disease Detection & Recommendation System  
**FarmEase** is an intelligent plant disease detection system designed to assist farmers and gardeners in identifying diseases through image analysis using a CNN model.  
It offers multilingual recommendations and features like disease history tracking and a plant community forum for image sharing and queries.

---

## 🎯 Key Features

📤 **Upload Leaf Image**  
- Upload any plant leaf image via the browser.  
- Backend API calls the trained CNN model to detect disease.

🧠 **CNN-Based AI Model**  
- The system uses a trained Convolutional Neural Network (CNN) to analyze images and predict diseases.

🌐 **Multilingual Recommendations**  
- Get care tips and solutions in:  
  - 🇮🇳 English  
  - 🇮🇳 Hindi  
  - 🇮🇳 Gujarati  

🕓 **History Tracking**  
- All uploaded images and detected diseases are saved per user.  
- View past detections with timestamp and recommended solutions.

👥 **Community Feed**  
- Users can share their posts.  
- Others can comment, like, or reply to queries.

---

## 🛠️ Tech Stack

| Layer           | Technology                         |
|----------------|-------------------------------------|
| Frontend        | React.js, HTML, CSS       |
| Backend         | ASP.NET Core             |
| AI Model        | Python CNN (served via Flask API / integrated into .NET) |
| Database        | SQL Server                |                       |
| Authentication  | JWT-Based Login System              |

---

## 🚀 How It Works

1. **Upload a Leaf Image**  
   → Users select or drag-and-drop an image for analysis.

2. **Disease Detection (CNN)**  
   → .NET backend sends image to a Python CNN model to identify disease.

3. **Multilingual Recommendations via Gemini API**  
   → Detected disease is passed to **Gemini API**, which generates care advice in English, Hindi, or Gujarati.

4. **Save to History**  
   → Image are stored in the user's history.

5. **Community Sharing**  
   → Users can post their image and detection result for discussion.



👥 Contributor
[Amatullagajipurwala](https://github.com/Amatullagajipurwala)
