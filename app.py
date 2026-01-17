import streamlit as st
import pandas as pd
import joblib

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Cardiac Risk Dashboard",
    page_icon="🫀",
    layout="wide"
)

# ==========================================
# MINIMAL ADMIN-STYLE CSS
# ==========================================
st.markdown("""
<style>
.main {
    background-color: #0f172a;
}
.sidebar .sidebar-content {
    background-color: #020617;
}
.card {
    background-color: #020617;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
}
.title {
    color: #e5e7eb;
}
.label {
    color: #9ca3af;
}
.success {
    color: #22c55e;
    font-size: 20px;
    font-weight: bold;
}
.danger {
    color: #ef4444;
    font-size: 20px;
    font-weight: bold;
}
.metric {
    font-size: 28px;
    font-weight: bold;
    color: #38bdf8;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================
st.markdown("""
<div class="card">
    <h2 class="title">🫀 Cardiac Risk Prediction</h2>
    <p class="label">Machine Learning – CHD Dataset</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# LOAD MODEL
# ==========================================
model = joblib.load("Model.pkl")

# ==========================================
# MAIN CONTENT (ADMIN SHAPE)
# ==========================================
left, right = st.columns([2, 1])

# ---------- LEFT: FORM ----------
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Patient Information")

    sbp = st.number_input("Systolic Blood Pressure", 80, 250, 130)
    tobacco = st.number_input("Tobacco", 0.0, value=0.0)
    ldl = st.number_input("LDL Cholesterol", 0.0, value=3.0)
    adiposity = st.number_input("Adiposity", 0.0, value=25.0)
    typea = st.number_input("Type A", 0.0, value=50.0)
    obesity = st.number_input("Obesity", 0.0, value=25.0)
    alcohol = st.number_input("Alcohol", 0.0, value=0.0)
    age = st.number_input("Age", 20, 100, 50)

    famhist = st.selectbox("Family History", ["Absent", "Present"])

    predict = st.button("🔍 Predict")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- RIGHT: RESULT ----------
with right:
    if predict:
        input_data = pd.DataFrame([{
            "sbp": sbp,
            "tobacco": tobacco,
            "ldl": ldl,
            "adiposity": adiposity,
            "typea": typea,
            "obesity": obesity,
            "alcohol": alcohol,
            "age": age,
            "famhist": famhist
        }])

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Prediction Result")

        if prediction == 1:
            st.markdown("<div class='danger'>⚠️ HIGH CARDIAC RISK</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='success'>✅ LOW CARDIAC RISK</div>", unsafe_allow_html=True)

        st.markdown(
            f"<div class='metric'>{probability*100:.2f}%</div>",
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================
st.caption("Academic Project – Cardiac Risk Prediction")
