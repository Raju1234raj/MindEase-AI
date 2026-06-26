import streamlit as st
import pandas as pd
import plotly.express as px
from utils import MOOD_META, now_iso

st.set_page_config(
    page_title="Mood Tracker",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Mood Tracker")

st.caption("Track your emotional wellbeing over time.")

# -----------------------------
# Session State
# -----------------------------
if "mood_log" not in st.session_state:
    st.session_state.mood_log = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("💜 MindEase")

    st.page_link("app.py", label="🏠 Home")

    st.page_link(
        "pages/chat.py",
        label="💬 Chat"
    )

    st.page_link(
        "pages/wellnesstoolkit.py",
        label="🧘 Wellness Toolkit"
    )

    st.divider()

    st.subheader("Log Mood")

    mood = st.selectbox(
        "Today's Mood",
        [
            "😊 Happy",
            "😐 Okay",
            "😰 Anxious",
            "😤 Stressed",
            "😔 Sad",
            "😠 Angry",
        ],
    )

    note = st.text_input(
        "Optional Note"
    )

    if st.button("Save Mood", use_container_width=True):

        mood_key = mood.split(" ", 1)[1].lower()

        st.session_state.mood_log.append(
            {
                "mood": mood_key,
                "timestamp": now_iso(),
                "note": note,
            }
        )

        st.success("Mood saved successfully!")

        st.rerun()

    st.divider()

    if st.button(
        "🗑 Clear Mood History",
        use_container_width=True
    ):
        st.session_state.mood_log = []
        st.rerun()

# -----------------------------
# No Data
# -----------------------------
if len(st.session_state.mood_log) == 0:

    st.info(
        "No mood history yet.\n\n"
        "Log your first mood using the sidebar."
    )

    st.stop()

# -----------------------------
# DataFrame
# -----------------------------
df = pd.DataFrame(st.session_state.mood_log)

df["timestamp"] = pd.to_datetime(df["timestamp"])

df["date"] = df["timestamp"].dt.date

df["emoji"] = df["mood"].apply(
    lambda x: MOOD_META.get(x, {}).get("emoji", "")
)

df["label"] = df["mood"].apply(
    lambda x: MOOD_META.get(x, {}).get("label", x)
)

# Mood Score
score_map = {
    "happy": 5,
    "okay": 4,
    "anxious": 3,
    "stressed": 2,
    "sad": 1,
    "angry": 1,
}

df["score"] = df["mood"].map(score_map)
# --------------------------------------------------
# Statistics
# --------------------------------------------------

st.subheader("📈 Mood Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Total Logs",
        len(df)
    )

with c2:
    st.metric(
        "Days Tracked",
        df["date"].nunique()
    )

with c3:
    st.metric(
        "Average Score",
        round(df["score"].mean(), 1)
    )

with c4:
    top_mood = df["label"].value_counts().idxmax()
    st.metric(
        "Most Common",
        top_mood
    )

st.divider()

# --------------------------------------------------
# Mood Score Timeline
# --------------------------------------------------

st.subheader("📈 Mood Timeline")

fig = px.line(
    df,
    x="timestamp",
    y="score",
    markers=True,
    title="Mood Trend",
)

fig.update_layout(
    yaxis=dict(range=[1, 5]),
    xaxis_title="Date",
    yaxis_title="Mood Score",
    height=450,
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Mood Distribution
# --------------------------------------------------

st.subheader("🥧 Mood Distribution")

pie = px.pie(
    df,
    names="label",
    hole=0.45,
)

st.plotly_chart(
    pie,
    use_container_width=True,
)

# --------------------------------------------------
# Recent Mood History
# --------------------------------------------------

st.subheader("📝 Mood History")

history = df.copy()

history["Time"] = history["timestamp"].dt.strftime(
    "%d %b %Y %I:%M %p"
)

history["Mood"] = history["emoji"] + " " + history["label"]

history = history[
    [
        "Time",
        "Mood",
        "note",
    ]
]

history.columns = [
    "Date & Time",
    "Mood",
    "Note",
]

st.dataframe(
    history.iloc[::-1],
    use_container_width=True,
    hide_index=True,
)

# --------------------------------------------------
# Download CSV
# --------------------------------------------------

csv = history.to_csv(index=False).encode()

st.download_button(
    "📥 Download Mood History",
    csv,
    file_name="mood_history.csv",
    mime="text/csv",
    use_container_width=True,
)