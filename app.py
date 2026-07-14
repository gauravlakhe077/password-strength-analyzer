import streamlit as st
import re
from zxcvbn import zxcvbn

# Page Configuration
st.set_page_config(
    page_title="🔐 Password Strength Analyzer",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Title & Description
st.title("🔐 Password Strength Analyzer")
st.markdown("""
Analyze your password strength with real-time feedback and security recommendations.
""")

# Sidebar
with st.sidebar:
    st.header("About")
    st.markdown("""
    ### Features:
    - ✅ Real-time strength analysis
    - 🔍 Advanced zxcvbn scoring
    - 💡 Security recommendations
    - 📊 Visual feedback
    """)

# Create tabs
tab1, tab2 = st.tabs(["🔍 Check Password", "📚 How It Works"])

with tab1:
    # Password input
    password = st.text_input("Enter your password:", type="password", placeholder="Type password here...")
    
    if password:
        # ===== BASIC CHECKS =====
        st.subheader("📋 Basic Checks")
        
        checks = {
            "Length ≥ 8 characters": len(password) >= 8,
            "Contains Uppercase (A-Z)": bool(re.search(r"[A-Z]", password)),
            "Contains Lowercase (a-z)": bool(re.search(r"[a-z]", password)),
            "Contains Digits (0-9)": bool(re.search(r"\d", password)),
            "Contains Symbols (!@#$%^&*)": bool(re.search(r"[!@#$%^&*]", password)),
        }
        
        # Display checks in columns
        col1, col2 = st.columns(2)
        for i, (check, passed) in enumerate(checks.items()):
            with col1 if i % 2 == 0 else col2:
                if passed:
                    st.success(f"✔ {check}")
                else:
                    st.error(f"✘ {check}")
        
        # ===== ADVANCED ANALYSIS =====
        st.subheader("🔬 Advanced Analysis (zxcvbn)")
        
        try:
            result = zxcvbn(password)
            score = result['score']  # 0-4
            
            # Score interpretation
            score_labels = ["Very Weak ⚠️", "Weak ⚠️", "Fair ⚡", "Good ✓", "Strong ✅"]
            
            # Progress bar
            st.progress((score + 1) / 5, text=f"Strength: {score_labels[score]}")
            
            # Score details
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Score", f"{score}/4")
            with col2:
                st.metric("Guesses", f"{result['guesses']:,}")
            with col3:
                crack_time = result['crack_times_display']['online_throttling_100_per_10_seconds']
                st.metric("Crack Time", crack_time)
            
            # Feedback & Suggestions
            if result['feedback']['warning']:
                st.warning(f"⚠️ **Warning:** {result['feedback']['warning']}")
            
            if result['feedback']['suggestions']:
                st.info("""
                ### 💡 Suggestions to Improve:
                """ + "\n".join(f"- {s}" for s in result['feedback']['suggestions']))
            
            # Password sequence analysis
            with st.expander("📊 Detailed Sequence Analysis"):
                st.write("Password patterns detected:")
                for i, seq in enumerate(result['sequence'], 1):
                    st.write(f"{i}. **{seq['pattern']}** - {seq.get('token', 'N/A')}")
        
        except Exception as e:
            st.error(f"Error analyzing password: {e}")
    
    else:
        st.info("👆 Enter a password above to get started!")

with tab2:
    st.markdown("""
    ## 📚 How This Tool Works
    
    ### What is Password Strength?
    A strong password is resistant to being guessed or cracked. This tool evaluates passwords based on:
    
    #### 1️⃣ **Basic Checks**
    - **Length**: Longer passwords are harder to crack
    - **Character Variety**: Mix of uppercase, lowercase, digits, and symbols
    
    #### 2️⃣ **Advanced Scoring (zxcvbn)**
    Uses sophisticated algorithms to:
    - Detect

