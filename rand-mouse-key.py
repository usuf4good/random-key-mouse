import pyautogui
import time
import random
import string

def generate_random_string(length):
    """Generate a random string of a given length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def move_mouse_randomly():
    """Move the mouse to a random position on the screen."""
    screen_width, screen_height = pyautogui.size()
    random_x = random.randint(0, screen_width - 1)
    random_y = random.randint(0, screen_height - 1)
    pyautogui.moveTo(random_x, random_y, duration=0.5)  # Adjust the duration if needed

def main():
    print("Hello Python.")
    while True:
        time.sleep(13)  # Sleep for 13 seconds

        # Generate a random string of a given length
        random_string = generate_random_string(5)  # Adjust the length as needed
        print(random_string)  # Print the random string to the console

        # Simulate typing the random string
        for char in random_string:
            pyautogui.keyDown(char)
            time.sleep(0.1)  # Adjust the delay between key presses if needed
            pyautogui.keyUp(char)
            time.sleep(0.1)  # Adjust the delay between key presses if needed

        # Move the mouse to a random position on the screen
        move_mouse_randomly()

if __name__ == "__main__":
    main()
