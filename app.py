import streamlit as st
import time
import pandas as pd

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AadhaarGuard", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0b132b;
}

/* Title */
.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #00FFAA;
}

.subtitle {
    text-align: center;
    color: #ccc;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.06);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.03);
}

/* Images */
.card img {
    border-radius: 15px;
}

/* Big cards */
.big-card {
    text-align: center;
    padding: 25px;
    border-radius: 15px;
    background: rgba(0,255,170,0.15);
    font-size: 20px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🛡️ AadhaarGuard")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📤 Upload", "🧠 Verification", "📊 Report"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚙️ System Status")
st.sidebar.success("🟢 AI Engine Active")
st.sidebar.info("📄 OCR Ready")
st.sidebar.warning("👤 Face Model Loaded")

# ================= HOME =================
if page == "🏠 Home":

    st.markdown('<div class="title">🛡️ AadhaarGuard</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-powered Identity Verification System</div>', unsafe_allow_html=True)

    # -------- IMAGE SECTION --------
    st.markdown("## 🔍 System Preview")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1591696205602-2f950c417cb9")
        st.markdown("🔐 Aadhaar Verification")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1607746882042-944635dfe10e")
        st.markdown("🤖 Face Recognition AI")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # -------- FEATURES --------
    st.markdown("## 🚀 Core Features")

    f1, f2, f3 = st.columns(3)

    f1.markdown('<div class="card">📄 OCR Extraction<br><small>Extract Aadhaar data</small></div>', unsafe_allow_html=True)
    f2.markdown('<div class="card">👤 Face Matching<br><small>AI based matching</small></div>', unsafe_allow_html=True)
    f3.markdown('<div class="card">✅ Validation<br><small>Smart verification</small></div>', unsafe_allow_html=True)

    st.markdown("---")

    # -------- HOW IT WORKS --------
    st.markdown("## 🚀 How It Works")

    s1, s2, s3, s4 = st.columns(4)

    s1.markdown('<div class="card">📄 Upload Aadhaar</div>', unsafe_allow_html=True)
    s2.markdown('<div class="card">👤 Upload Face</div>', unsafe_allow_html=True)
    s3.markdown('<div class="card">🧠 AI Processing</div>', unsafe_allow_html=True)
    s4.markdown('<div class="card">✅ Verification</div>', unsafe_allow_html=True)

    st.markdown("---")

    # -------- METRICS --------
    st.markdown("## 📊 Performance")

    m1, m2, m3 = st.columns(3)

    m1.markdown('<div class="big-card">95% Accuracy</div>', unsafe_allow_html=True)
    m2.markdown('<div class="big-card">1.8s Speed</div>', unsafe_allow_html=True)
    m3.markdown('<div class="big-card">AI Powered</div>', unsafe_allow_html=True)

    st.markdown("---")

    # -------- CHART --------
    st.markdown("## 📊 System Pipeline")

    data = pd.DataFrame({
        "Stage": ["OCR", "Face Match", "Validation"],
        "Score": [85, 75, 90]
    })

    st.bar_chart(data.set_index("Stage"))

# ================= UPLOAD =================
elif page == "📤 Upload":

    st.title("📤 Upload Documents")

    col1, col2 = st.columns(2)

    aadhaar = col1.file_uploader("Upload Aadhaar", type=["jpg","png"])
    face = col2.file_uploader("Upload Face Image", type=["jpg","png"])

    if aadhaar:
        st.image(aadhaar, caption="Aadhaar Uploaded")

    if face:
        st.image(face, caption="Face Uploaded")

    if st.button("🚀 Start Verification"):
        st.session_state["ready"] = True
        st.success("Files uploaded successfully!")

# ================= VERIFICATION =================
elif page == "🧠 Verification":

    st.title("🧠 AI Verification")

    if "ready" not in st.session_state:
        st.warning("⚠️ Upload files first")
    else:
        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        st.success("Processing Complete!")

        similarity_score = 0.82

        st.markdown("## 📊 Confidence")
        st.progress(int(similarity_score * 100))
        st.write(f"{similarity_score*100:.2f}% Match")

        if similarity_score > 0.6:
            st.success("✅ VERIFIED")
        else:
            st.error("❌ NOT VERIFIED")

# ================= REPORT =================
elif page == "📊 Report":

    st.title("📊 Verification Report")

    st.json({
        "Name": "Sample User",
        "DOB": "14/03/2005",
        "Aadhaar": "XXXX XXXX 7404"
    })

    data = pd.DataFrame({
        "Metric": ["OCR", "Face Match", "Validation"],
        "Score": [88, 82, 91]
    })

    st.bar_chart(data.set_index("Metric"))

    st.success("✅ VERIFIED")