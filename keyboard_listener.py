"""
The code creates a keyboard listener that runs in the background and waits for the user to press a key.
When a key is pressed, the on_press function is called with the key that was pressed as an argument.
The function simply prints the key to the console.
By default, the listener runs until the program is terminated, but you can also return False from the on_press function to stop the listener.
"""

# Import the keyboard module from the pynput package
from pynput import keyboard


# Define a callback function to handle the key press event
def on_press(key):
    # Print the key that was pressed
    print(key)

    # Optionally, return False to stop the listener
    # return False


# Create a new keyboard listener object with the on_press callback
listener = keyboard.Listener(on_press=on_press)

# Start the listener in a separate thread
listener.start()

# Wait for the listener to stop (in this case, forever)
listener.join()
