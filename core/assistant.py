
from core.commands import process_command
from voice.speech_to_text import listen
from voice.text_to_speech import speak


class Assistant:
    def start(self):
        speak("Hello! I am KALKI. Call my name whenever you need me.")

        wake_words = [
            "hey kalki",
            "hi kalki",
            "kalki",
            "halki",
            "cal ki",
            "kal ki",
        ]

        while True:
            try:
                # Wait for the wake word
                command = listen()

                if not command:
                    continue

                command = command.lower().strip()
                print(f"Recognized command: {command}", flush=True)

                # Exit KALKI
                if command in ["exit", "quit", "stop assistant"]:
                    speak("Goodbye! KALKI is shutting down.")
                    break

                # Check whether KALKI was called
                matched_word = next(
                    (
                        word for word in wake_words
                        if word in command
                    ),
                    None,
                )

                if not matched_word:
                    continue

                # Remove the wake word
                command = command.replace(matched_word, "", 1).strip()
                command = " ".join(command.split())

                # If only the name was spoken, ask for a command
                if not command:
                    speak("Yes, how can I help?")

                    command = listen()

                    if not command:
                        continue

                    command = command.lower().strip()

                    if command in ["exit", "quit", "stop assistant"]:
                        speak("Goodbye! KALKI is shutting down.")
                        break

                print(f"Processing command: {command}", flush=True)

                response = process_command(command)

                print(f"KALKI response: {response}", flush=True)
                speak(response)

            except Exception as error:
                print(f"Assistant error: {error}", flush=True)

                try:
                    speak("Sorry, something went wrong.")
                except Exception as voice_error:
                    print(f"Voice error: {voice_error}", flush=True)


if __name__ == "__main__":
    Assistant().start()
