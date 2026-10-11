import pyttsx3


def speak(text):
    print(f"KALKI: {text}", flush=True)

    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as error:
        print(f"Speech error: {error}", flush=True)
    finally:
        engine.stop()
        del engine