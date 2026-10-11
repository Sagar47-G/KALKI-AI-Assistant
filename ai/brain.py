
import json
import urllib.request
import urllib.error


def ask_ai(question):
    url = "http://localhost:11434/api/chat"

    data = {
        "model": "llama3.2:3b",
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "stream": False
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["message"]["content"]

    except urllib.error.URLError as error:
        print(f"AI connection error: {error}")
        return "I cannot connect to my local AI model. Please check Ollama."

    except Exception as error:
        print(f"AI error: {error}")
        return "Sorry, I could not generate an answer."
