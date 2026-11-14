# 💜 MindEase AI – Student Mental Wellness Companion

MindEase AI is an AI-powered mental wellness companion designed especially for students. It helps users express their feelings, track their moods, and practice simple wellness activities.

Built using **Python, Streamlit, and Groq AI**.

## ✨ Features

### 💬 AI Chat
- Chat with an AI-powered wellness companion.
- Receive supportive and empathetic responses.
- Get wellness suggestions based on detected moods.

### 📊 Mood Tracker
- Record your daily moods.
- View mood statistics.
- Visualize mood trends using charts.
- Download mood history as CSV.

### 🧘 Wellness Toolkit
- Guided breathing exercises.
- 5-4-3-2-1 grounding technique.
- Daily wellness tips.
- Meditation timer.
- Positive affirmations.
- Emergency support information.

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- Pandas
- Plotly
- Python Dotenv

## 📁 Project Structure

```text
MindEase-AI/
│
├── assets/
├── pages/
│   ├── chat.py
│   ├── moodtracker.py
│   └── wellnesstoolkit.py
│
├── app.py
├── utils.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Raju1234raj/MindEase-AI.git
```

### 2. Open the project folder

```bash
cd MindEase-AI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Groq API Key

Create a `.env` file in the project folder:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/keys).

### 7. Run the application

```bash
streamlit run app.py
```

## 🔐 Security

- Keep your API key private.
- Never upload your `.env` file to GitHub.
- Do not share private user information.

## ⚠️ Disclaimer

MindEase AI is an educational wellness project. It is not a substitute for professional mental health care, diagnosis, or emergency services.

## 👨‍💻 Developer

**Raju1234raj**

GitHub: [@Raju1234raj](https://github.com/Raju1234raj)

---

Made with 💜 using Python, Streamlit and Groq AI.
