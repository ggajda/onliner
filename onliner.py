from gui_main import App
import os
import atexit


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()

atexit.register(os._exit(0))
