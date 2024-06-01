from pynput import keyboard
import time
import random
import sys


key = keyboard.Controller()
i = 0


def press_fn(stop):

    tekst = "To jest przkładowy tekst"
    global i

    while True:
        for t in tekst:
            key.tap(t)
            if t == " ":
                time.sleep(random.randint(1, 5))
            time.sleep(random.random())
            if stop:
                sys.exit()
        if i == 2:
            time.sleep(random.randint(20, 60))
        i += 1
        if stop:
            sys.exit()


def on_release(key):
    try:
        print("{0}".format(key))
    except AttributeError:
        print("special key {0} pressed".format(key))


def listener_fn():
    listener = keyboard.Listener(on_release=on_release)
    listener.start()
