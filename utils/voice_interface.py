import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
import subprocess
import pygame
import time

def get_voice_input() -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
        return ""
    except sr.RequestError:
        print("❌ STT service error.")
        return ""

def speak_text(text: str):
    try:
        tts = gTTS(text=text, lang='en')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            temp_path = fp.name

        print("🔊 Processing audio...")

        pygame.mixer.init()
        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.3)

        pygame.mixer.quit()
        os.remove(temp_path)

    except Exception as e:
        print(f"❌ Error during audio playback: {e}")

def choose_input_mode() -> str:
    print("\n🗾 Select input method:")
    print("1️⃣ Speak your input")
    print("2️⃣ Type your input")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        return get_voice_input()
    elif choice == "2":
        return input("✍️ Enter your input: ").strip()
    else:
        print("⚠️ Invalid choice. Defaulting to text.")
        return input("✍️ Enter your input: ").strip()

def choose_output_mode(context: str = "output") -> str:
    print(f"\n📤 How would you like to experience the {context}?")
    print("1️⃣ Listen to audio")
    print("2️⃣ Read in terminal")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        return "audio"
    elif choice == "2":
        return "text"
    else:
        print("⚠️ Invalid choice. Showing text.")
        return "text"
