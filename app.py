import streamlit as st
import pandas as pd
import numpy as np
import time
import random

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="BioRhythm AI", layout="wide")

# --- 2. SESSION STATE (Memory) ---
if 'h_val' not in st.session_state: st.session_state.h_val = 0.12
if 'dd_val' not in st.session_state: st.session_state.dd_val = 0.25
if 'ud_val' not in st.session_state: st.session_state.ud_val = 0.15

def auto_set_logic():
    patterns = [
        {"h": 0.08, "dd": 0.15, "ud": 0.07},
        {"h": 0.14, "dd": 0.35, "ud": 0.12},
        {"h": 0.04, "dd": 0.60, "ud": 0.05},
        {"h": 0.20, "dd": 0.10, "ud": 0.30},
        {"h": 0.03, "dd": 0.05, "ud": 0.02},
        {"h": 0.10, "dd": 0.80, "ud": 0.40},
        {"h": 0.25, "dd": 0.20, "ud": 0.10},
        {"h": 0.06, "dd": 0.12, "ud": 0.06}
    ]
    new_p = random.choice(patterns)
    st.session_state.h_val = new_p["h"]
    st.session_state.dd_val = new_p["dd"]
    st.session_state.ud_val = new_p["ud"]
    st.session_state.demo_mode = True

# --- 3. CSS STYLE ---
st.markdown("""
    <style>
    .stDeployButton {display:none !important;}
    .stButton > button {
        background: linear-gradient(to right, #4A90E2, #9013FE) !important;
        color: white !important;
        border-radius: 10px !important;
        height: 45px; width: 100%; font-weight: bold;
    }
    .analysis-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ BioRhythm: Identity Analytics")
st.divider()

# --- TOP SECTION: INPUTS ---
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.subheader("⌨️ Biometric Capture")
    st.button("✨ Auto-Set (Change Pattern)", on_click=auto_set_logic)
    with st.container(border=True):
        h_time = st.slider("Hold Duration (H)", 0.01, 0.30, key="h_val")
        dd_time = st.slider("Down-Down Latency (DD)", 0.01, 1.00, key="dd_val")
        ud_time = st.slider("Up-Down Latency (UD)", 0.01, 0.50, key="ud_val")
        run_analysis = st.button("🚀 EXECUTE IDENTITY SCAN")

with col_right:
    st.subheader("📡 Live Preview")
    preview_data = pd.DataFrame({'User Signature': [h_time, dd_time, ud_time] * 5})
    st.line_chart(preview_data, color="#4A90E2", height=230)

st.divider()

if run_analysis:
    _, middle_col, _ = st.columns([0.5, 2, 0.5])
    
    with middle_col:
        with st.spinner('Authenticating...'):
            time.sleep(1)
            is_demo = st.session_state.get('demo_mode', False)
            
            st.markdown("<div class='analysis-container'>", unsafe_allow_html=True)
            st.subheader("📋 Analysis Report")
            
            c1, c2 = st.columns(2)
            c1.metric("Detected User", "ID-s002" if is_demo else "Unknown Subject")
            c2.metric("Neural Confidence", "94.49%" if is_demo else "18.22%")

            if is_demo:
                st.success("✅ AUTHENTICATED: Biometric Signature Match")
                # --- ADDED THE BALLOONS HERE ---
                st.balloons() 
            else:
                st.error("❌ REJECTED: Signature mismatch detected")

            st.write("#### 📉 Biometric Signature Comparison")
            comparison_data = pd.DataFrame({
                'User Rhythm': [h_time, dd_time, ud_time] * 5,
                'System Baseline': [0.08, 0.15, 0.07] * 5
            })
            st.area_chart(comparison_data, color=["#4A90E2", "#FF4B4B"], height=350)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.session_state.demo_mode = False
else:
    st.markdown("<h3 style='text-align: center; color: grey;'>Waiting for Identity Scan...</h3>", unsafe_allow_html=True)

st.divider()
st.caption("Developer: Nisha")