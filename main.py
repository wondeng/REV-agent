import os
import openai
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import time
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Settings
duration = 5  # seconds
sample_rate = 44100
file_name = "input.wav"
tts_file = "response.mp3"

def record_audio():
    print("\n🎙 Speak in 1 sec...")
    time.sleep(1)
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    wav.write(file_name, sample_rate, audio)
    print("✅ Recorded.")

def transcribe_audio():
    print("🔍 Transcribing...")
    with open(file_name, "rb") as f:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language="en"
        )
    print("📝 You said:", transcript.text)
    return transcript.text.strip().lower()

def get_gpt_response(prompt):
    print("🤖 Thinking...")
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    reply = response.choices[0].message.content
    return reply.strip()

def speak(text):
    print("🔊 Speaking...")
    speech = openai.audio.speech.create(model="tts-1", voice="nova", input=text)
    with open(tts_file, "wb") as f:
        f.write(speech.content)
    os.system(f"afplay {tts_file}")  # macOS

if __name__ == "__main__":
    print("🧠 REV-Agent is listening. Say 'goodbye' to end the chat.")
    try:
        while True:
            record_audio()
            prompt = transcribe_audio()

            if "goodbye" in prompt or "exit" in prompt or "stop" in prompt:
                print("👋 Exiting conversation. Bye!")
                speak("Goodbye! Have a great day.")
                break

            reply = get_gpt_response(prompt)
            print("🤖 Assistant:", reply)
            speak(reply)

    except KeyboardInterrupt:
        print("\n🛑 Conversation manually stopped.")
