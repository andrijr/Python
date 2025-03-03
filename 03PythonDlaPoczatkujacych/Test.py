import pyautogui
import pyscreenshot
import time

# Define the regions of the screen to monitor
regions_of_interest = [(x1, y1, x2, y2), (x3, y3, x4, y4)]  # replace with your coordinates

# Define the conditions for clicking
def should_click(screenshot):
    for region in regions_of_interest:
        pixel = screenshot.getpixel((region[0], region[1]))
        if 1 <= pixel <= 100:  # replace with your condition
            return True
        elif pixel == 100:  # replace with your condition
            return False
    return False

# Main loop
while True:
    screenshot = pyscreenshot.grab()
    if should_click(screenshot):
        pyautogui.click()
    time.sleep(1)  # adjust the sleep time as needed