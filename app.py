import os
import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Upgrading the AI Multiverse",
    page_icon="🌌",
    layout="centered",
)

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(129, 140, 248, 0.25), transparent 35%),
            radial-gradient(circle at bottom right, rgba(34, 211, 238, 0.18), transparent 35%),
            linear-gradient(135deg, #020617 0%, #0f172a 45%, #111827 100%);
        color: #e5e7eb;
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #020617 0%, #111827 100%);
        border-right: 1px solid rgba(148, 163, 184, 0.18);
    }
    .main-title {
        text-align: center;
        font-size: 2.4rem;
        font-weight: 900;
        margin-bottom: 0.2rem;
        background: linear-gradient(90deg, #67e8f9, #a78bfa, #f0abfc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .sub-text {
        text-align: center;
        color: #cbd5e1;
        font-size: 1rem;
        margin-bottom: 1.3rem;
    }
    .glass-card {
        padding: 1rem 1.1rem;
        border-radius: 18px;
        background: rgba(15, 23, 42, 0.70);
        border: 1px solid rgba(148, 163, 184, 0.22);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.28);
        margin-bottom: 1rem;
    }
    .settings-pill {
        display: inline-block;
        padding: 0.35rem 0.65rem;
        border-radius: 999px;
        background: rgba(56, 189, 248, 0.12);
        border: 1px solid rgba(56, 189, 248, 0.25);
        color: #bae6fd;
        font-size: 0.85rem;
        margin-right: 0.35rem;
        margin-top: 0.35rem;
    }
    div[data-testid="stTextArea"] textarea {
        border-radius: 16px;
        border: 1px solid rgba(148, 163, 184, 0.28);
        background: rgba(15, 23, 42, 0.85);
        color: #f8fafc;
    }
    .stButton > button {
        width: 100%;
        border-radius: 14px;
        border: none;
        padding: 0.8rem 1rem;
        font-weight: 900;
        background: linear-gradient(90deg, #22d3ee, #818cf8, #e879f9);
        color: #020617;
        transition: 0.25s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(129, 140, 248, 0.35);
        color: #020617;
    }
    .footer-note {
        color: #94a3b8;
        text-align: center;
        font-size: 0.82rem;
        margin-top: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def get_api_key() -> str | None:
    """Read Gemini API key from Streamlit secrets first, then environment variable."""
    try:
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass
    return os.getenv("GEMINI_API_KEY")


api_key = get_api_key()
if api_key:
    genai.configure(api_key=api_key)

# Task 1: The UI Cleanup - Sidebar Integration
st.sidebar.title("App Settings")

# Task 2: Persona Expansion
personalities = [
    "A friendly AI mentor",
    "An expert Hacker",
    "A wise space explorer",
    "A panicked college student at 3 AM",
    "A 1920s Mafia Boss",
    "A highly sarcastic fitness coach",
    "A dramatic Shakespearean robot",
    "A cheerful kindergarten teacher",
]

selected_personality = st.sidebar.selectbox("Choose AI Personality", personalities)

# Task 3: Parameter Tuning - The Slider
intensity_level = st.sidebar.slider(
    "Intensity Level",
    min_value=1,
    max_value=10,
    value=6,
)

st.sidebar.markdown("---")
st.sidebar.write("**How intensity works:**")
st.sidebar.caption("1 = subtle personality, 10 = extremely dramatic and fully in character.")

# Task 5: Dynamic Avatars using if/elif control flow
if selected_personality == "A friendly AI mentor":
    bot_avatar = "🌸"
elif selected_personality == "An expert Hacker":
    bot_avatar = "💻"
elif selected_personality == "A wise space explorer":
    bot_avatar = "🚀"
elif selected_personality == "A panicked college student at 3 AM":
    bot_avatar = "😵‍💫"
elif selected_personality == "A 1920s Mafia Boss":
    bot_avatar = "🎩"
elif selected_personality == "A highly sarcastic fitness coach":
    bot_avatar = "🏋️"
elif selected_personality == "A dramatic Shakespearean robot":
    bot_avatar = "🤖"
elif selected_personality == "A cheerful kindergarten teacher":
    bot_avatar = "🧸"
else:
    bot_avatar = "✨"

st.markdown('<h1 class="main-title">🌌 Upgrading the AI Multiverse</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-text">A modern Gemini-powered chat interface with creative personas, intensity control, and dynamic avatars.</p>',
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="glass-card">
        <strong>Current Multiverse Settings</strong><br>
        <span class="settings-pill">Persona: {selected_personality}</span>
        <span class="settings-pill">Intensity: {intensity_level}/10</span>
        <span class="settings-pill">Avatar: {bot_avatar}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    if message["role"] == "user":
        with st.chat_message("user", avatar="🧑"):
            st.markdown(message["content"])
    else:
        with st.chat_message("assistant", avatar=message.get("avatar", "✨")):
            st.markdown(message["content"])

user_message = st.text_area(
    "Type your message",
    placeholder="Ask anything and watch the selected personality respond...",
    height=120,
)

send_clicked = st.button("SEND")

# Task 3: Prompt Engineering Update using f-string
ai_instructions = f"""
You are acting as: {selected_personality}.

Your personality intensity level is {intensity_level} out of 10.

Follow these rules:
- Stay in the selected personality throughout the response.
- If intensity is 1 to 3, keep the personality subtle and mostly professional.
- If intensity is 4 to 7, make the personality clearly noticeable and entertaining.
- If intensity is 8 to 10, act very strongly in character while still being useful and understandable.
- Answer the user's actual question clearly.
- Do not mention that you are pretending unless the user asks.
- Keep responses concise, helpful, and engaging.
"""

# Task 4: The Visual Upgrade - Chat Elements
if send_clicked:
    if not user_message.strip():
        st.warning("Please type a message before sending.")
    elif not api_key:
        st.error(
            "Gemini API key not found. Add GEMINI_API_KEY in Streamlit secrets "
            "or set it as an environment variable."
        )
    else:
        cleaned_message = user_message.strip()

        with st.chat_message("user", avatar="🧑"):
            st.markdown(cleaned_message)

        st.session_state.chat_history.append({"role": "user", "content": cleaned_message})

        try:
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction=ai_instructions,
            )

            with st.spinner("The multiverse is generating a response..."):
                response = model.generate_content(cleaned_message)

            assistant_reply = response.text if response.text else "I could not generate a response. Please try again."

            with st.chat_message("assistant", avatar=bot_avatar):
                st.markdown(assistant_reply)

            st.session_state.chat_history.append(
                {"role": "assistant", "content": assistant_reply, "avatar": bot_avatar}
            )

        except Exception as error:
            st.error(f"Something went wrong while contacting Gemini: {error}")

st.markdown(
    '<p class="footer-note">Built for MirAI School of Technology — AI Builder Track Assignment 2</p>',
    unsafe_allow_html=True,
)
