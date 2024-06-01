import customtkinter
from pynput import keyboard
import threading, sys, random
import time
from key_emulator import press_fn

key = keyboard.Controller()
stop = True


def stop_loop(stop):
    if stop:
        sys.exit()


def run_loop(txt):
    global stop
    stop = not stop

    counter = 1

    while True:
        stop_loop(stop)

        for t in txt:
            key.tap(t)
            if t == " ":
                time.sleep(random.randint(1, 5))
            time.sleep(random.random())
            stop_loop(stop)

        if counter % 2 == 0:
            time.sleep(random.randint(5, 60))

        counter += 1


def thread_fn(txt):
    thread = threading.Thread(target=run_loop, args=(txt,))
    thread.start()


class OnLiner(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def checkbox_handler():
            self.textBox_writer.focus()
            self.textBox_writer.delete(index1="0.0", index2="end")
            thread_fn(self.textBox_reader.get(index1="0.0", index2="end"))

        self.checkbox_var = customtkinter.StringVar(value="off")
        self.checkbox = customtkinter.CTkCheckBox(
            self,
            text="Start",
            command=checkbox_handler,
            variable=self.checkbox_var,
            onvalue="on",
            offvalue="off",
        )
        self.checkbox.pack(pady=20, padx=20, fill="x")

        self.label_reader = customtkinter.CTkLabel(self, text="Tekst wejściowy:")
        self.label_reader.pack()

        self.textBox_reader = customtkinter.CTkTextbox(
            self, width=600, height=100, corner_radius=3
        )
        self.textBox_reader.insert(index="0.0", text="To jest przykładowy tekst")
        self.textBox_reader.pack(pady=20)

        self.label_writer = customtkinter.CTkLabel(self, text="Tekst wyjściowy:")
        self.label_writer.pack()

        self.textBox_writer = customtkinter.CTkTextbox(self, width=600, corner_radius=3)
        self.textBox_writer.pack(pady=20)
