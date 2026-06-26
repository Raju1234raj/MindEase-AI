"""
utils.py
MindEase AI - Shared Utility Functions
"""

import os
from datetime import datetime

from dotenv import load_dotenv
from groq import Groq

# ----------------------------------------------------
# Load Environment Variables
# ----------------------------------------------------

load_dotenv()

MODEL = "llama-3.3-70b-versatile"

# ----------------------------------------------------
# Groq Client
# ----------------------------------------------------

def get_groq_client():
    """
    Returns authenticated Groq client.
    """

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "Groq API key not found.\n"
            "Create a .env file and add:\n"
            "GROQ_API_KEY=your_api_key"
        )

    return Groq(api_key=api_key)


# ----------------------------------------------------
# Mood Keywords
# ----------------------------------------------------

MOOD_KEYWORDS = {

    "happy": [
        "happy",
        "great",
        "good",
        "awesome",
        "amazing",
        "fantastic",
        "excited",
        "joy",
        "smile",
        "fine"
    ],

    "sad": [
        "sad",
        "cry",
        "crying",
        "depressed",
        "upset",
        "hurt",
        "lonely",
        "empty",
        "hopeless"
    ],

    "anxious": [
        "anxiety",
        "anxious",
        "worried",
        "panic",
        "fear",
        "scared",
        "nervous"
    ],

    "stressed": [
        "stress",
        "stressed",
        "pressure",
        "deadline",
        "exam",
        "assignment",
        "burnout",
        "tired"
    ],

    "angry": [
        "angry",
        "frustrated",
        "mad",
        "annoyed",
        "furious",
        "rage"
    ],

    "okay": [
        "okay",
        "ok",
        "normal",
        "neutral",
        "alright"
    ]
}

# ----------------------------------------------------
# Crisis Detection
# ----------------------------------------------------

CRISIS_WORDS = [

    "suicide",

    "kill myself",

    "want to die",

    "end my life",

    "self harm",

    "hurt myself",

    "better off dead",

    "end it all",

    "no reason to live"
]

# ----------------------------------------------------
# Mood UI Metadata
# ----------------------------------------------------

MOOD_META = {

    "happy": {
        "emoji": "😊",
        "label": "Happy",
        "color": "#DFF6DD"
    },

    "sad": {
        "emoji": "😔",
        "label": "Sad",
        "color": "#D6EAF8"
    },

    "anxious": {
        "emoji": "😰",
        "label": "Anxious",
        "color": "#FFF4CC"
    },

    "stressed": {
        "emoji": "😤",
        "label": "Stressed",
        "color": "#FADBD8"
    },

    "angry": {
        "emoji": "😠",
        "label": "Angry",
        "color": "#F5B7B1"
    },

    "okay": {
        "emoji": "😐",
        "label": "Okay",
        "color": "#EBEDEF"
    }

}

# ----------------------------------------------------
# Wellness Tips
# ----------------------------------------------------

TIPS = {

    "happy": (
        "Keep the positivity going!",
        "Write down one thing that made you smile today."
    ),

    "sad": (
        "Take a small step.",
        "Go outside for 10 minutes and get some fresh air."
    ),

    "anxious": (
        "Try Box Breathing.",
        "Inhale 4 sec → Hold 4 sec → Exhale 4 sec."
    ),

    "stressed": (
        "Take a break.",
        "Study for 25 minutes, then rest for 5 minutes."
    ),

    "angry": (
        "Pause before reacting.",
        "Take deep breaths and drink a glass of water."
    ),

    "okay": (
        "Stay balanced.",
        "Maintain your healthy routine today."
    )

}
# ----------------------------------------------------
# Detect Mood
# ----------------------------------------------------

def detect_mood(text: str):
    """
    Detect user's mood from the message.
    """

    text = text.lower()

    for mood, keywords in MOOD_KEYWORDS.items():
        for word in keywords:
            if word in text:
                return mood

    return "okay"


# ----------------------------------------------------
# Detect Crisis
# ----------------------------------------------------

def detect_crisis(text: str):
    """
    Check if the message contains crisis keywords.
    """

    text = text.lower()

    for word in CRISIS_WORDS:
        if word in text:
            return True

    return False


# ----------------------------------------------------
# Build AI System Prompt
# ----------------------------------------------------

def build_system_prompt(mood, crisis):
    """
    Creates the system prompt sent to Groq.
    """

    prompt = """
You are MindEase AI.

You are a warm, kind and empathetic mental health companion for college students.

Rules:

1. Speak like a caring friend.
2. Never judge the user.
3. Never diagnose mental illness.
4. Keep answers short (3-6 sentences).
5. Encourage healthy coping techniques.
6. If the user is in crisis, respond calmly and encourage them to seek immediate help.
"""

    if mood:

        prompt += f"\nThe user's detected mood is: {mood}."

    if crisis:

        prompt += """

The user may be experiencing a mental health crisis.

Respond with empathy.

Recommend contacting:

• iCall India — 9152987821
• Vandrevala Foundation — 18602662345

Do not panic the user.
"""

    return prompt


# ----------------------------------------------------
# Stream Response from Groq
# ----------------------------------------------------

def stream_groq_response(messages, system_prompt):
    """
    Streams the AI response.
    """

    client = get_groq_client()

    response = client.chat.completions.create(

        model=MODEL,

        stream=True,

        temperature=0.7,

        max_tokens=500,

        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            *messages,
        ],
    )

    for chunk in response:

        if (
            chunk.choices
            and chunk.choices[0].delta
            and chunk.choices[0].delta.content
        ):
            yield chunk.choices[0].delta.content


# ----------------------------------------------------
# Time Helpers
# ----------------------------------------------------

def now_time():
    """
    Returns current time.
    """

    return datetime.now().strftime("%H:%M")


def now_iso():
    """
    Returns ISO timestamp.
    """

    return datetime.now().isoformat()