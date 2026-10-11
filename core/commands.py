
import datetime
import subprocess
import webbrowser
from urllib.parse import quote_plus

from system_control.laptop import (
    lock_laptop,
    increase_volume,
    decrease_volume,
    mute_volume,
    unmute_volume,
)

from ai.brain import ask_ai


def process_command(command):
    command = command.lower().strip()

    if command in ["hello", "hi", "hey"]:
        return "Hello! I am KALKI. How can I help you?"

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Okay, I am opening YouTube."

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Okay, I am opening Google."

    elif "open notepad" in command:
        subprocess.Popen(["notepad.exe"])
        return "Okay, I am opening Notepad."

    elif "search for" in command:
        query = command.replace("search for", "", 1).strip()

        if not query:
            return "Please tell me what to search for."

        webbrowser.open(
            "https://www.google.com/search?q=" + quote_plus(query)
        )
        return f"Okay, I am searching Google for {query}."

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "date" in command:
        current_date = datetime.date.today().strftime("%d %B %Y")
        return f"Today's date is {current_date}."

    elif "lock laptop" in command or "lock my laptop" in command:
        return lock_laptop()

    elif "increase volume" in command or "volume up" in command:
        return increase_volume()

    elif "decrease volume" in command or "volume down" in command:
        return decrease_volume()

    elif "mute volume" in command or command == "mute":
        return mute_volume()

    elif "unmute volume" in command or command == "unmute":
        return unmute_volume()

    else:
        # Ask the local AI when no existing command matches
        return ask_ai(command)
