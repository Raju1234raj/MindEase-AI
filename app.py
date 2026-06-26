import streamlit as st

st.set_page_config(
    page_title="MindEase AI",
    page_icon="💜",
    layout="wide"
)

# ----------------------------
# Session State
# ----------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "mood_log" not in st.session_state:
    st.session_state.mood_log = []

if "crisis_flag" not in st.session_state:
    st.session_state.crisis_flag = False

# ----------------------------
# CSS
# ----------------------------

st.markdown("""
<style>

.main{
    background:#F6F7FB;
}

.hero{
    background:linear-gradient(135deg,#5B4BDB,#8E7CFF);
    color:white;
    padding:45px;
    border-radius:20px;
}

.feature{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,.08);
    text-align:center;
    height:220px;
}

.stat{
    background:white;
    padding:18px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 2px 8px rgba(0,0,0,.08);
}

.footer{
    text-align:center;
    color:gray;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Hero
# ----------------------------

st.markdown("""
<div class='hero'>

<h1>💜 MindEase AI</h1>

### Your Mental Wellness Companion

Built for students using **Groq AI**.

Chat with AI, track moods, practice mindfulness and improve emotional wellbeing.

</div>

""", unsafe_allow_html=True)

st.write("")

# ----------------------------
# Navigation
# ----------------------------

col1,col2,col3=st.columns(3)

with col1:

    st.page_link(
        "pages/chat.py",
        label="💬 Chat",
        use_container_width=True
    )

with col2:

    st.page_link(
        "pages/moodtracker.py",
        label="📊 Mood Tracker",
        use_container_width=True
    )

with col3:

    st.page_link(
        "pages/wellnesstoolkit.py",
        label="🧘 Wellness Toolkit",
        use_container_width=True
    )

st.divider()

# ----------------------------
# Stats
# ----------------------------

c1,c2,c3=st.columns(3)

with c1:

    st.markdown(f"""
<div class="stat">
<h2>{len(st.session_state.chat_history)}</h2>
Messages
</div>
""",unsafe_allow_html=True)

with c2:

    st.markdown(f"""
<div class="stat">
<h2>{len(st.session_state.mood_log)}</h2>
Mood Logs
</div>
""",unsafe_allow_html=True)

with c3:

    st.markdown("""
<div class="stat">
<h2>Groq</h2>
AI Model
</div>
""",unsafe_allow_html=True)

st.write("")

# ----------------------------
# Features
# ----------------------------

st.subheader("✨ Features")

f1,f2,f3=st.columns(3)

with f1:

    st.markdown("""
<div class="feature">

# 💬

### AI Chat

Talk freely.

MindEase listens without judgement and responds with empathy.

</div>
""",unsafe_allow_html=True)

with f2:

    st.markdown("""
<div class="feature">

# 📈

### Mood Tracker

Track your emotional wellbeing with beautiful charts.

</div>
""",unsafe_allow_html=True)

with f3:

    st.markdown("""
<div class="feature">

# 🧘

### Wellness Toolkit

Breathing exercises.

Grounding techniques.

Daily wellness tips.

</div>
""",unsafe_allow_html=True)

st.write("")

# ----------------------------
# About
# ----------------------------

st.subheader("About")

st.write("""

MindEase AI is designed especially for college students.

It helps students

- Reduce stress

- Manage anxiety

- Improve emotional wellbeing

- Build healthy habits

using modern AI technology powered by **Groq Llama 3.3 70B**.

""")

st.info("⚠️ MindEase is not a replacement for professional medical advice.")

st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit + Groq AI

</div>
""",unsafe_allow_html=True)