import streamlit as st
import time

st.set_page_config(
    page_title="Wellness Toolkit",
    page_icon="🧘",
    layout="wide"
)

# ----------------------------
# Sidebar
# ----------------------------

with st.sidebar:

    st.title("💜 MindEase")

    st.page_link("app.py", label="🏠 Home")

    st.page_link(
        "pages/chat.py",
        label="💬 Chat"
    )

    st.page_link(
        "pages/moodtracker.py",
        label="📊 Mood Tracker"
    )

st.title("🧘 Wellness Toolkit")

st.write(
    "Take a few minutes for yourself. Small daily habits can improve emotional wellbeing."
)

st.divider()

# ---------------------------------------------------
# Breathing Exercise
# ---------------------------------------------------

st.header("🌬️ Guided Breathing Exercise")

st.write(
    """
Follow the animation.

Inhale → Hold → Exhale

Repeat for a few cycles.
"""
)

placeholder = st.empty()

if st.button("▶ Start Breathing Exercise"):

    for _ in range(3):

        placeholder.success("🟢 Inhale... (4 sec)")
        time.sleep(4)

        placeholder.info("🟡 Hold... (4 sec)")
        time.sleep(4)

        placeholder.warning("🔵 Exhale... (4 sec)")
        time.sleep(4)

    placeholder.success("✅ Great job! You completed the breathing exercise.")

st.divider()

# ---------------------------------------------------
# Grounding Exercise
# ---------------------------------------------------

st.header("🌳 5-4-3-2-1 Grounding")

st.write(
"""
Look around you and identify:

👀 5 things you can see

✋ 4 things you can touch

👂 3 things you can hear

👃 2 things you can smell

👅 1 thing you can taste
"""
)

st.info(
"This exercise helps reduce anxiety and brings your attention back to the present moment."
)

st.divider()

# ---------------------------------------------------
# Daily Wellness Tips
# ---------------------------------------------------

st.header("💡 Daily Wellness Tips")

tips = [

"Drink enough water 💧",

"Sleep 7–8 hours 😴",

"Go for a short walk 🚶",

"Talk to a friend ❤️",

"Practice gratitude 🙏",

"Take breaks while studying 📚",

"Exercise for 20 minutes 🏃",

"Reduce screen time 📱",

"Eat healthy meals 🥗",

"Celebrate small wins 🌟"

]

for tip in tips:

    st.success(tip)

st.divider()

# ---------------------------------------------------
# Meditation Timer
# ---------------------------------------------------

st.header("⏱ 1 Minute Relaxation")

if st.button("Start 60 Second Timer"):

    progress = st.progress(0)

    for i in range(60):

        progress.progress((i + 1) / 60)

        time.sleep(1)

    st.balloons()

    st.success("🎉 Nice! You completed one minute of mindfulness.")

st.divider()

# ---------------------------------------------------
# Emergency Contacts
# ---------------------------------------------------

st.header("📞 Emergency Support")

st.warning(
"""
If you feel unsafe or need immediate support, please contact:

📞 iCall India
9152987821

📞 Vandrevala Foundation
1860-2662-345

📞 NIMHANS
080-46110007
"""
)

st.divider()

# ---------------------------------------------------
# Positive Affirmations
# ---------------------------------------------------

st.header("💜 Positive Affirmations")

affirmations = [

"I am stronger than I think.",

"My feelings are valid.",

"I deserve kindness.",

"I don't have to be perfect.",

"I am growing every day.",

"I can overcome today's challenges.",

"I believe in myself.",

"Every small step counts."

]

for quote in affirmations:

    st.info("✨ " + quote)

st.divider()

st.success("🌸 Thank you for taking time to care for yourself today.")