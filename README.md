# -AadhaarGuard-Indian-Document-Verification-System
🔍 Overview

AadhaarGuard is a Python-based identity verification system that simulates real-world eKYC (Electronic Know Your Customer) workflows.
It uses OCR (Optical Character Recognition) and facial recognition to extract and validate user identity information from Aadhaar cards.

The system processes uploaded documents, verifies identity through face matching, and outputs an automated verification decision.

⚙️ Key Features
📄 Aadhaar Data Extraction
Extracts Name, Date of Birth, Gender, and Aadhaar Number using OCR
👤 Face Verification
Matches face from Aadhaar card with user-provided image
🔢 Validation Checks
Aadhaar number format validation
Age verification (18+)
Face presence detection
🖼 Image Quality Checks
Detects blurred or low-quality images for better accuracy
✅ Automated Decision System
Outputs final result: Verified / Not Verified
🧠 System Workflow
Upload Aadhaar → OCR Extraction → Face Detection → Face Matching → Validation Checks → Final Decision
🛠 Tech Stack
Python
Streamlit – for interactive UI
OpenCV – image processing & face detection
Tesseract OCR – text extraction
face_recognition / Deep Learning models – facial similarity
📂 Project Structure
aadhaarguard/
│── app.py
│── ocr.py
│── face_match.py
│── validation.py
│── requirements.txt
│── README.md
│── demo/
📸 Demo Screenshots



Upload Interface
Extracted Aadhaar Details
Face Match Result
Final Verification Output
🎥 Demo Video

👉 Add your demo video link here (YouTube recommended)

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/aadhaarguard.git
cd aadhaarguard
2. Install dependencies
pip install -r requirements.txt
3. Run the application
streamlit run app.py
📊 Sample Output
Extracted Text: Name, DOB, Aadhaar Number
Face Match Score: e.g., 0.78
Final Result: ✅ Verified / ❌ Not Verified
🔐 Disclaimer

This project is developed for educational purposes only.
It does not store or process real Aadhaar data and is not affiliated with any government authority.

🚀 Future Improvements
API-based deployment (FastAPI/Flask)
Database integration for verification logs
Advanced OCR using deep learning models
Real-time webcam face verification
