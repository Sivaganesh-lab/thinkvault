import streamlit as st
from utils.hasher import hash_idea
from utils.timestamp import get_utc_timestamp
from utils.certificate_generator import generate_certificate
from utils.data_store import save_idea, verify_hash

st.set_page_config(
    page_title="ThinkVault",
    page_icon="🔐",
    layout="centered"
)
st.markdown("""
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }

        .stTextInput>div>input {
            border-radius: 10px;
        }

        .css-18e3th9 {
            background: #f8f9fa;
        }

        .main {
            background-color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)


#st.image("static/logo.png", width=50)
st.markdown("<h1 style='text-align: center;'>🔐 ThinkVault</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Prove your idea existed — instantly.</h4>", unsafe_allow_html=True)

st.title("🔐 ThinkVault - Idea Ownership Locker")

st.write("Enter your original idea below to generate a secure timestamp and certificate.")

tab1, tab2 = st.tabs(["🧠 Submit Idea", "🔍 Verify Idea"])

# --- Tab 1: Submit Idea ---
with tab1:
    idea = st.text_area("💡 Your Original Idea", height=200)
    submitted = st.button("🕒 Generate Timestamp Certificate")

    if submitted and idea.strip():
        idea_hash = hash_idea(idea)
        timestamp = get_utc_timestamp()

        st.code(f"Idea Hash: {idea_hash}", language="text")
        st.code(f"Timestamp: {timestamp}", language="text")
        st.code(idea_hash, language="text")
        st.button("📋 Copy Hash", on_click=st.toast, args=("Hash copied!",))

        # Generate PDF Certificate
        pdf_path = generate_certificate(idea_hash, timestamp)

        st.success("✅ Your idea has been secured! Download your proof below.")

        # Provide PDF download
        with open(pdf_path, "rb") as f:
            st.download_button("📄 Download Certificate (PDF)", f, file_name="ThinkVault_Certificate.pdf")

        # Save the idea to datastore
        save_idea(idea, idea_hash, timestamp)

# --- Tab 2: Verify Idea ---
with tab2:
    st.markdown("---")
    st.header("🔍 Verify Your Idea Certificate")

    input_hash = st.text_input("Enter your idea hash:")
    if st.button("Verify"):
        if input_hash.strip():
            valid, result = verify_hash(input_hash.strip())
            if valid:
                st.success("✅ Match Found!")
                st.write("**Idea:**", result["idea"])
                st.write("**Timestamp:**", result["timestamp"])
            else:
                st.error("❌ No match found.")



from utils.emailer import send_certificate

email = st.text_input("📧 Enter your email to receive the certificate:")
if st.button("Send via Email"):
    send_certificate(email, cert_path)
    st.success("📨 Sent to your inbox!")


st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ by Siva Ganesh | 2025</p>", unsafe_allow_html=True)

