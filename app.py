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
            score = result['score']
            
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
                st.warning(f"⚠️ Warning: {result['feedback']['warning']}")
            
            if result['feedback']['suggestions']:
                suggestions_text = "\n".join(f"- {s}" for s in result['feedback']['suggestions'])
                st.info(f"### 💡 Suggestions to Improve:\n{suggestions_text}")
            
            # Password sequence analysis
            with st.expander("📊 Detailed Sequence Analysis"):
                st.write("Password patterns detected:")
                for i, seq in enumerate(result['sequence'], 1):
                    pattern = seq['pattern']
                    token = seq.get('token', 'N/A')
                    st.write(f"{i}. **{pattern}** - {token}")
        
        except Exception as e:
            st.error(f"Error analyzing password: {e}")
    
    else:
        st.info("👆 Enter a password above to get started!")

with tab2:
    st.header("📚 How This Tool Works")
    
    st.subheader("What is Password Strength?")
    st.write("A strong password is resistant to being guessed or cracked. This tool evaluates passwords based on:")
    
    st.subheader("1️⃣ Basic Checks")
    st.write("- **Length**: Longer passwords are harder to crack")
    st.write("- **Character Variety**: Mix of uppercase, lowercase, digits, and symbols")
    
    st.subheader("2️⃣ Advanced Scoring (zxcvbn)")
    st.write("Uses sophisticated algorithms to:")
    st.write("- Detect common patterns (birthdates, sequential numbers)")
    st.write("- Check against common password dictionaries")
    st.write("- Analyze entropy")
    st.write("- Estimate crack time")
    
    st.subheader("🎯 Score Interpretation")
    st.write("- **0 - Very Weak**: Could be cracked in seconds")
    st.write("- **1 - Weak**: Could be cracked in hours")
    st.write("- **2 - Fair**: Could be cracked in days/weeks")
    st.write("- **3 - Good**: Could be cracked in months")
    st.write("- **4 - Strong**: Very resistant to cracking")
    
    st.subheader("🔐 Tips for Strong Passwords")
    st.write("✅ Use at least 12 characters")
    st.write("✅ Mix uppercase and lowercase")
    st.write("✅ Include numbers and symbols")
    st.write("✅ Avoid common words and patterns")
    st.write("✅ Don't reuse passwords across sites")
    st.write("✅ Use a password manager")
    
    st.warning("⚠️ Never enter passwords you actually use! This is for educational purposes.")

# Footer
st.divider()
st.caption("🔐 Made with Streamlit | Educational Purpose Only")
