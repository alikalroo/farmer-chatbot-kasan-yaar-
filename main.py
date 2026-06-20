import json
import re
import tkinter as tk
from pathlib import Path

from ui import ChatUI

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.json"

with DATA_FILE.open("r", encoding="utf-8") as file:
    data = json.load(file)


def normalize_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def get_best_response(user_input):
    query = normalize_text(user_input)
    if not query:
        return "Maazrat, aap ne kuch likha nahi."

    best_response = "Maazrat, is sawal ka jawab mere database mein mojood nahi hai."
    best_score = 0

    for item in data["questions"]:
        for pattern in item["patterns"]:
            pattern_text = normalize_text(pattern)
            query_tokens = set(query.split())
            pattern_tokens = set(pattern_text.split())

            if query == pattern_text:
                return item["response"]

            overlap_count = len(query_tokens & pattern_tokens)
            score = overlap_count * 10

            # Give extra weight to stronger matches such as full phrase overlap
            if query in pattern_text or pattern_text in query:
                score += 50

            if overlap_count >= 2 and score > best_score:
                best_score = score
                best_response = item["response"]

    return best_response


def send_message():
    user_input = app.entry.get().strip()

    if user_input == "":
        return

    app.chat_area.insert(tk.END, "Aap: " + user_input + "\n")

    answer = get_best_response(user_input)
    app.chat_area.insert(tk.END, "Bot: " + answer + "\n\n")

    app.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatUI(root)
    app.send_button.config(command=send_message)
    root.mainloop()