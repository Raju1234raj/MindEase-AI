import streamlit as st
from utils import (
    detect_mood,
    detect_crisis,
    build_system_prompt,
    stream_groq_response,
    MOOD_META,
    TIPS,
    now_time,
    now_iso,
)

st.set_page_config(
    page_title="MindEase Chat",
    page_icon="💬",
    layout="wide",
)

# -----------------------------
# Session State
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "mood_log" not in st.session_state:
    st.session_state.mood_log = []

if "crisis_flag" not in st.session_state:
    st.session_state.crisis_flag = False

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("💜 MindEase")

    st.write("### Quick Mood")

    mood = st.radio(
        "Select your mood",
        [
            "😊 Happy",
            "😐 Okay",
            "😰 Anxious",
            "😤 Stressed",
            "😔 Sad",
            "😠 Angry",
        ],
    )

    st.divider()

    st.write("### Navigation")

    st.page_link("app.py", label="🏠 Home")

    st.page_link(
        "pages/moodtracker.py",
        label="📊 Mood Tracker",
    )

    st.page_link(
        "pages/wellnesstoolkit.py",
        label="🧘 Wellness Toolkit",
    )

    st.divider()

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

# -----------------------------
# Header
# -----------------------------
st.title("💬 MindEase Chat")

st.caption(
    "Talk freely. Everything you share is treated as a conversation, not a diagnosis."
)

# -----------------------------
# Crisis Banner
# -----------------------------
if st.session_state.crisis_flag:

    st.error(
        """
If you feel unsafe or think you may harm yourself,
please contact someone you trust immediately.

📞 iCall India
9152987821

📞 Vandrevala Foundation
18602662345
"""
    )

# -----------------------------
# Welcome
# -----------------------------
if len(st.session_state.chat_history) == 0:

    st.info(
        """
👋 Hello!

I'm MindEase.

I'm here to listen, support and encourage you.

Tell me how you're feeling today.
"""
    )

# -----------------------------
# Display Chat
# -----------------------------
for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            mood = message.get("mood")

            if mood in MOOD_META:

                st.caption(
                    f"{MOOD_META[mood]['emoji']} {MOOD_META[mood]['label']}"
                )

                if mood in TIPS:

                    title, body = TIPS[mood]

                    with st.expander("💡 Wellness Tip"):

                        st.write(f"**{title}**")

                        st.write(body)

        # --------------------------------------------------
# Chat Input
# --------------------------------------------------

prompt = st.chat_input("Type your message...")

if prompt:

    mood = detect_mood(prompt)

    crisis = detect_crisis(prompt)

    if crisis:
        st.session_state.crisis_flag = True

    # Save user message
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": prompt,
            "mood": mood,
            "time": now_time(),
        }
    )

    # Save mood history
    st.session_state.mood_log.append(
        {
            "mood": mood,
            "timestamp": now_iso(),
        }
    )

    # Display user message immediately
    with st.chat_message("user"):
        st.markdown(prompt)

    # Build AI prompt
    system_prompt = build_system_prompt(
        mood=mood,
        crisis=crisis,
    )

    messages = []

    for msg in st.session_state.chat_history:

        messages.append(
            {
                "role": msg["role"],
                "content": msg["content"],
            }
        )

    # AI Response
    with st.chat_message("assistant"):

        placeholder = st.empty()

        response = ""

        try:

            for chunk in stream_groq_response(
                messages,
                system_prompt,
            ):

                response += chunk

                placeholder.markdown(response + "▌")

            placeholder.markdown(response)

        except Exception as e:
            import traceback

            st.error(f"Error: {e}")
            st.code(traceback.format_exc())

            raise
    # Save assistant message
    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": response,
            "mood": mood,
            "time": now_time(),
        }
    )

    st.rerun()