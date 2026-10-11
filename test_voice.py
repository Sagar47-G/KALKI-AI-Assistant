
from voice.speech_to_text import listen
from voice.text_to_speech import speak

speak("Hello! I am your personal assistant.")
command = listen()

if command:
    speak(f"You said {command}")
else:
    speak("I did not hear anything.")

