
import threading
import tkinter as tk
from tkinter import scrolledtext

from ai.brain import ask_ai
from core.commands import process_command
from voice.speech_to_text import listen
from voice.text_to_speech import speak


class KalkiDesktop:
    def __init__(self, root):
        self.root = root
        self.root.title("KALKI AI Assistant")
        self.root.geometry("750x600")
        self.root.minsize(550, 400)

        tk.Label(
            root,
            text="KALKI AI",
            font=("Segoe UI", 22, "bold"),
        ).pack(pady=10)

        self.chat = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Segoe UI", 11),
            state=tk.DISABLED,
        )
        self.chat.pack(
            padx=15, pady=10, fill=tk.BOTH, expand=True
        )

        input_frame = tk.Frame(root)
        input_frame.pack(fill=tk.X, padx=15, pady=10)

        self.entry = tk.Entry(input_frame, font=("Segoe UI", 12))
        self.entry.pack(
            side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10)
        )
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(
            input_frame, text="Send", command=self.send_message
        )
        self.send_button.pack(side=tk.LEFT, padx=(0, 8))

        self.voice_button = tk.Button(
            input_frame,
            text="🎤 Speak",
            command=self.start_voice,
        )
        self.voice_button.pack(side=tk.LEFT)

        self.add_message(
            "KALKI",
            "Hello! Type a question or press Speak to talk.",
        )

    def add_message(self, sender, message):
        self.chat.config(state=tk.NORMAL)
        self.chat.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat.see(tk.END)
        self.chat.config(state=tk.DISABLED)

    def send_message(self, event=None):
        message = self.entry.get().strip()
        if not message:
            return

        self.entry.delete(0, tk.END)
        self.handle_message(message)

    def start_voice(self):
        self.voice_button.config(state=tk.DISABLED)
        self.add_message("KALKI", "Listening...")

        threading.Thread(
            target=self.listen_once,
            daemon=True,
        ).start()

    def listen_once(self):
        try:
            message = listen()
            if message:
                self.root.after(
                    0, lambda text=message: self.handle_message(text)
                )
            else:
                self.root.after(
                    0,
                    lambda: self.add_message(
                        "KALKI", "I didn't hear anything. Please try again."
                    ),
                )
        except Exception as error:
            self.root.after(
                0,
                lambda err=str(error): self.add_message(
                    "KALKI", f"Voice error: {err}"
                ),
            )
        finally:
            self.root.after(
                0,
                lambda: self.voice_button.config(state=tk.NORMAL),
            )

    def handle_message(self, message):
        self.add_message("You", message)
        self.send_button.config(state=tk.DISABLED)
        self.voice_button.config(state=tk.DISABLED)

        threading.Thread(
            target=self.process_message,
            args=(message,),
            daemon=True,
        ).start()

    def process_message(self, message):
        try:
            command = message.lower().strip()

            # Keep known computer commands routed to existing functions.
            system_commands = [
                "lock laptop", "lock my laptop",
                "increase volume", "volume up",
                "decrease volume", "volume down",
                "mute", "mute volume", "unmute", "unmute volume",
                "open youtube", "open google", "open notepad",
                "search for",
            ]

            if any(item in command for item in system_commands):
                answer = process_command(command)
            else:
                answer = ask_ai(message)

            self.root.after(
                0, lambda result=answer: self.add_message("KALKI", result)
            )

            # Speak the response using your existing TTS module.
            speak(answer)

        except Exception as error:
            self.root.after(
                0,
                lambda err=str(error): self.add_message(
                    "KALKI", f"Error: {err}"
                ),
            )
        finally:
            self.root.after(
                0, lambda: self.send_button.config(state=tk.NORMAL)
            )
            self.root.after(
                0, lambda: self.voice_button.config(state=tk.NORMAL)
            )


if __name__ == "__main__":
    window = tk.Tk()
    app = KalkiDesktop(window)
    window.mainloop()
