import customtkinter
from gui_onliner import OnLiner


def on_focus_in(event):
    
    #stop_loop(stop)
    print('on focus in')

def on_focus_out(event):
    print('on focus out')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.event_bind = self.bind()

        self.geometry("700x500+10+10")
        #self.iconbitmap("icon.ico")
        self.title("onLiner")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)


        self.on_linter = OnLiner(self)
        self.on_linter.pack(padx=20, pady=20, fill="both", expand=True)
