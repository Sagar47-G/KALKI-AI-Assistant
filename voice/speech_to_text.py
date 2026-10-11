
import speech_recognition as sr

recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("\nListening... Speak now.")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()

        except sr.WaitTimeoutError:
            print("No speech detected.")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
        except sr.RequestError:
            print("Speech service unavailable. Check your internet.")

        return ""
