import streamlit as st
import google.generativeai as genai
import os
import config
import json
import time
from filter import is_solar_related  # Import the solar query filter

# Configure Gemini API
genai.configure(api_key=config.API_KEY)

def get_ai_response(user_input):
    model = genai.GenerativeModel("gemini-pro")  # Using Gemini Pro model
    response = model.generate_content(user_input)
    return response.text if hasattr(response, "text") else "Error fetching response"

# Streamlit UI
st.set_page_config(page_title="Solar Industry AI Assistant", page_icon="☀️", layout="wide")
st.title("🌞 Solar Industry AI Assistant")
st.write("🔍 **Ask any question related to solar energy, installation, cost, regulations, and more!**")

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Layout with columns
col1, col2 = st.columns([2, 1])

with col1:
    user_query = st.text_area("💡 Enter your question:", height=100)
    if st.button("⚡ Get Answer", use_container_width=True):
        if user_query.strip():
            if is_solar_related(user_query):  # Check if the query is solar-related
                with st.spinner("Thinking...💭"):
                    time.sleep(1)  # Simulate thinking animation
                    response = get_ai_response(user_query)
                st.session_state.chat_history.append({"question": user_query, "answer": response})
                st.subheader("🤖 AI Response:")
                st.success(response)
            else:
                st.warning("⚠️ Please ask only solar energy-related questions.")
        else:
            st.warning("⚠️ Please enter a question.")

# Export Chat History
if st.sidebar.button("💾 Export Chat History"):
    chat_data = json.dumps(st.session_state.chat_history, indent=4)
    st.sidebar.download_button("📥 Download", chat_data, "chat_history.json", "application/json")

# Display chat history in sidebar
with col2:
    st.sidebar.title("📜 Chat History")
    for chat in st.session_state.chat_history[::-1]:
        if st.sidebar.button(f"🗨️ {chat['question'][:50]}...", key=chat['question']):
            st.sidebar.write(f"**Q:** {chat['question']}")
            st.sidebar.write(f"**A:** {chat['answer']}")
