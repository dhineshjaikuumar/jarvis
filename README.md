# jarvis
Jarvis is an AI-powered personal voice assistant built with Python, LiveKit, and Google Gemini AI. It can listen, understand, and respond in real time with natural, human-like conversations. Jarvis supports voice interaction, humor mode, memory with SQLite, and noise cancellation, making it a smart, fun, and efficient assistant for everyday use.
Jarvis AI Assistant

Your personal AI-powered voice assistant built with Python, LiveKit, and Google Gemini AI.
Jarvis can listen, understand, and respond in real time using natural, human-like conversations.








 Features

 Real-time voice interaction with natural responses
 Integrated with Google Gemini AI for smart conversations
 Noise cancellation for crystal-clear communication
 Built-in humor mode for fun & engaging replies
 SQLite memory to remember previous chats
 Simple, lightweight, and developer-friendly

 Tech Stack

Python  – Core programming language

LiveKit SDK 🎙 – Real-time voice & streaming support

Google Gemini API  – AI model for responses

SQLite3 🗄 – Local database to store memory

Noise Cancellation 🎧 – Better voice clarity

 Getting Started
1️ Clone the Repository
git clone https://github.com/your-username/jarvis-ai-assistant.git
cd jarvis-ai-assistant

2️ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # For Windows
source venv/bin/activate  # For Mac/Linux

3️ Install Dependencies
pip install -r requirements.txt

4️ Set Up API Keys

Create a .env file in the root directory and add:

LIVEKIT_URL=wss://your-livekit-url
LIVEKIT_API_KEY=your-livekit-api-key
LIVEKIT_API_SECRET=your-livekit-api-secret
GOOGLE_API_KEY=your-google-api-key

5️ Run the Project
python agent.py

 How Jarvis Works

Listens to your voice commands

Processes them using Google Gemini AI

Generates smart responses in real time

Remembers conversations using SQLite memory

Speaks back with natural-sounding voices

 Project Structure
jarvis-ai-assistant/
│── agent.py           # Main assistant logic
│── db_manager.py      # Handles SQLite database operations
│── prompt.py          # AI instructions and humor mode
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation
│── jarvis_memory.db   # SQLite memory database

 Future Enhancements

🔹 Integration with OpenAI GPT for multi-model support
🔹 Add custom wake word detection (e.g., "Hey Jarvis")
🔹 Create a desktop app using PyQt or Electron
🔹 Add home automation support for IoT devices



🧑‍💻 Author

Dhinesh J
 | 🌐 LinkedIn - https://www.linkedin.com/in/dhinesh-j-ba1417281?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
