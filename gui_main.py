import customtkinter
from gui_onliner import OnLiner


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600+10+10")
        self.title("onLiner")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.on_linter = OnLiner(self)
        self.on_linter.pack(padx=20, pady=20, fill="both", expand=True)
