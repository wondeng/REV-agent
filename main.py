import os
import openai
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import time
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Settings
duration = 5  # seconds
sample_rate = 44100
file_name = "input.wav"
tts_file = "response.mp3"

def record_audio():
    print("🎙 Speak now in 1 sec...")
    time.sleep(1)
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    wav.write(file_name, sample_rate, audio)
    print("✅ Recorded!")

def transcribe_audio():
    print("🔍 Transcribing...")
    with open(file_name, "rb") as f:
        transcript = openai.audio.transcriptions.create(model="whisper-1", file=f)
    print("📝 You said:", transcript.text)
    return transcript.text

def get_gpt_response(prompt):
    print("🧠 Thinking...")
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def speak(text):
    print("🔊 Speaking...")
    speech = openai.audio.speech.create(model="tts-1", voice="nova", input=text)
    with open(tts_file, "wb") as f:
        f.write(speech.content)
    os.system(f"afplay {tts_file}")  # macOS only

if __name__ == "__main__":
    print("🔁 Start chatting with your voice assistant (say 'stop' to quit)")
    while True:
        record_audio()
        prompt = transcribe_audio()

        if "stop" in prompt.lower():
            print("👋 Conversation ended.")
            break

        reply = get_gpt_response(prompt)
        print("🤖 Assistant:", reply)
        speak(reply)
