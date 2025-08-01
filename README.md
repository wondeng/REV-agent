-- REV-agent --

REV-agent is a real-time voice assistant built using OpenAI's APIs. It captures user speech, transcribes it, generates intelligent responses with GPT-4o, and replies with natural-sounding speech.

> Features

- Voice input recording using a local microphone
- Speech-to-text transcription powered by OpenAI Whisper
- Smart replies generated using GPT-4o
- Realistic text-to-speech output using OpenAI TTS (Nova voice)
- Conversation loop that exits on natural language cues like "goodbye" or "exit"

> Requirements

- Python 3.9+
- An OpenAI API key with access to Whisper, Chat, and TTS endpoints

> Setup

1) Clone the repository:

   git clone https://github.com/wondeng/REV-agent.git
   cd REV-agent
   
3) Create and activate a virtual environment:
   
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux

5) Install Dependencies:

  pip install -r requirements.txt

6) Create a .env file and add your OpenAI API key:
  OPENAI_API_KEY=your_api_key_here
