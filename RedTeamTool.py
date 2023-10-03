# Name: Abdullah Sakayl
# Email: aks4803

import time
import keyboard

def press_caps_lock():
    while True:

        # Presses the caps lock 
        keyboard.press('caps lock') # Presses a key on the keyboard
        keyboard.release('caps lock') # Releases the action of pressing a key on the keyboard

        # Repeat a "HAHAHAHA" message on the machine whenever the code is excuted
        keyboard.press('H') 
        keyboard.release('H') 
        time.sleep(.01) 
        keyboard.press('A')
        keyboard.release('A')
        time.sleep(.01)
        keyboard.press('H') 
        keyboard.release('H')
        time.sleep(.01)  
        keyboard.press('A')
        keyboard.release('A')
        time.sleep(.01)
        keyboard.press('H') 
        keyboard.release('H')
        time.sleep(.01)  
        keyboard.press('A')
        keyboard.release('A')
       
        time.sleep(1)  # Adjust the delay as needed for how often the previous events occur

# Main function that runs the code until the user use Ctrl + C to stop the tool 
if __name__ == "__main__":
    try:
        press_caps_lock()
    except KeyboardInterrupt:
        print("\nTool stopped.")


