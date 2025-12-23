import customtkinter as ctk
from pynput import keyboard
import threading
import random
import time

key = keyboard.Controller()


class WriterThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.running = threading.Event()
        self.text = ""

    def start_writing(self, text):
        self.text = text
        self.running.set()
        if not self.is_alive():
            self.start()

    def stop_writing(self):
        self.running.clear()

    def run(self):
        counter = 1
        while True:
            self.running.wait()  # czeka aż checkbox = ON

            for char in self.text:
                if not self.running.is_set():
                    break

                key.tap(char)

                if char == " ":
                    time.sleep(random.randint(1, 5))
                else:
                    time.sleep(random.random())

            if counter % 2 == 0:
                time.sleep(random.randint(5, 60))

            counter += 1


class OnLiner(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        self.writer_thread = WriterThread()

        self.checkbox_var = ctk.StringVar(value="off")
        master.bind("<FocusIn>",  self.on_focus_in)
        master.bind("<FocusOut>",  self.on_focus_out)

        self.checkbox = ctk.CTkCheckBox(
            self,
            text="Start",
            variable=self.checkbox_var,
            onvalue="on",
            offvalue="off",
            command=self.checkbox_handler,
        )
        self.checkbox.pack(pady=20, padx=20, fill='x')

        self.label_reader = ctk.CTkLabel(self, text="Tekst wejściowy:")
        self.label_reader.pack()

        self.textBox_reader = ctk.CTkTextbox(self, width=600, height=100)
        self.textBox_reader.insert("0.0", "To jest przykładowy tekst")
        self.textBox_reader.pack(pady=10)

        self.label_writer = ctk.CTkLabel(self, text="Tekst wyjściowy:")
        self.label_writer.pack()

        self.textBox_writer = ctk.CTkTextbox(self, width=600, height=100)
        self.textBox_writer.pack(pady=10)

    def on_focus_in(self, event)->None:
        print('on_focus_in')
        self.checkbox_var = ctk.StringVar(value="on")
        self.checkbox_handler()

    def on_focus_out(self, event)->None:
        print('on_focus_out')
        self.checkbox_var = ctk.StringVar(value="off")
        self.checkbox_handler()

    def checkbox_handler(self)->None:
        if self.checkbox_var.get() == "on":
            text = self.textBox_reader.get("0.0", "end").strip()
            self.textBox_writer.delete("0.0", "end")
            self.textBox_writer.focus()
            self.writer_thread.start_writing(text)
        else:
            self.writer_thread.stop_writing()


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    app.title("OnLiner")
    app.geometry("700x500")

    OnLiner(app)

    app.mainloop()
