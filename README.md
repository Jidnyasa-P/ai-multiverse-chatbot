# 🌌 Upgrading the AI Multiverse

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Chat%20App-FF4B4B?style=for-the-badge&logo=streamlit)
![Gemini](https://img.shields.io/badge/Gemini-API-8E75B2?style=for-the-badge&logo=google)
![Status](https://img.shields.io/badge/Assignment%202-Completed-success?style=for-the-badge)

### A modern Gemini-powered Streamlit chat app with sidebar settings, creative AI personas, intensity tuning, chat bubbles, and dynamic avatars.

</div>

---

## 📌 Demo Video


https://github.com/user-attachments/assets/4051f073-3a09-40be-9606-a3b24faa7a59

---

## ✨ Features Implemented

| Task | Requirement | Status |
|---|---|---|
| Task 1 | Move personality dropdown to sidebar | ✅ Done |
| Task 1 | Add `st.sidebar.title("App Settings")` | ✅ Done |
| Task 2 | Add at least 3 creative personalities | ✅ Done |
| Task 3 | Add sidebar slider for intensity level | ✅ Done |
| Task 3 | Inject personality + intensity into prompt f-string | ✅ Done |
| Task 4 | Replace plain output with `st.chat_message()` | ✅ Done |
| Task 4 | Render user and assistant as chat bubbles | ✅ Done |
| Task 5 | Add if/elif avatar control flow | ✅ Done |
| Task 5 | Pass dynamic avatar to assistant chat bubble | ✅ Done |

---

## 🎭 Available Personalities

- 🌸 A friendly AI mentor
- 💻 An expert Hacker
- 🚀 A wise space explorer
- 😵‍💫 A panicked college student at 3 AM
- 🎩 A 1920s Mafia Boss
- 🏋️ A highly sarcastic fitness coach
- 🤖 A dramatic Shakespearean robot
- 🧸 A cheerful kindergarten teacher

---

## 🎚️ Intensity Level

The sidebar includes an **Intensity Level** slider from `1` to `10`.

```text
1-3   → subtle personality
4-7   → clearly noticeable personality
8-10  → highly dramatic personality
```

The selected intensity is injected directly into the Gemini system prompt.

---

## 📁 Project Structure

```text
upgrading-ai-multiverse/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔐 Gemini API Key Setup

The app reads your Gemini API key from either Streamlit secrets or an environment variable.

### Option 1: Streamlit Secrets

Create this file:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
```

### Option 2: Environment Variable

#### Windows PowerShell

```powershell
$env:GEMINI_API_KEY="your_gemini_api_key_here"
```

#### macOS/Linux

```bash
export GEMINI_API_KEY="your_gemini_api_key_here"
```

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL shown in the terminal:

```text
http://localhost:8501
```

---

## 🧪 Testing Checklist

- [x] Sidebar contains personality dropdown
- [x] Sidebar contains intensity slider
- [x] Gemini response appears as a chat bubble
- [x] User message appears as a chat bubble
- [x] Avatar changes when personality changes
- [x] Empty message shows warning
- [x] API key missing shows clear error
- [x] Chat history remains visible during the session

---

<div align="center">

### Built with 💙 using Streamlit + Gemini

</div>
