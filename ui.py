import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class ChatUI:

    def __init__(self, root):

        # ===== Header =====
        header_frame = tk.Frame(
            root,
            bg="#EAF5D7",
            height=120
        )
        header_frame.pack(fill="x")

        title_label = tk.Label(
            header_frame,
            text="Kisan Yaar",
            font=("Georgia", 32, "bold"),
            fg="darkgreen",
            bg="#EAF5D7"
        )
        title_label.place(x=220, y=20)

        subtitle_label = tk.Label(
            header_frame,
            text="Aap ka Zarai Madadgar 🌿",
            font=("Arial", 18),
            fg="darkgreen",
            bg="#EAF5D7"
        )
        subtitle_label.place(x=220, y=70)

        # ===== Chat Area =====
        self.chat_area = ScrolledText(
            root,
            font=("Arial", 13),
            wrap=tk.WORD,
            bg="white"
        )

        self.chat_area.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        # ===== Bottom Frame =====
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(
            fill="x",
            padx=20,
            pady=15
        )

        self.entry = tk.Entry(
            bottom_frame,
            font=("Arial", 14),
            relief="solid",
            bd=1
        )

        self.entry.pack(
            side=tk.LEFT,
            fill="x",
            expand=True,
            ipady=12
        )

        self.send_button = tk.Button(
            bottom_frame,
            text="Send",
            font=("Arial", 13, "bold"),
            bg="#3E9E1A",
            fg="white",
            width=10,
            cursor="hand2"
        )

        self.send_button.pack(
            side=tk.RIGHT,
            padx=10
        )