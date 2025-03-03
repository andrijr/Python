import pyautogui
import pyscreenshot
import time

class ScreenClicker:
    def __init__(self):
        self.regions_of_interest = []
        self.click_condition = lambda x: 1 <= x <= 100  # Condition for clicking
        self.stop_condition = lambda x: x == 100  # Condition for stopping clicking
        self.click_count = 0

    def set_regions(self, regions):
        """Define the regions of interest on the screen.

        Args:
            regions (list): List of tuples representing the coordinates of the regions.
        """
        self.regions_of_interest = regions

    def set_conditions(self, click_condition=None, stop_condition=None):
        """Set the conditions for clicking and stopping.

        Args:
            click_condition (function): Lambda function that determines when to click.
            stop_condition (function): Lambda function that determines when to stop clicking.
        """
        if click_condition:
            self.click_condition = click_condition
        if stop_condition:
            self.stop_condition = stop_condition

    def click(self):
        """Perform a mouse click if conditions are met."""
        try:
            screenshot = pyscreenshot.grab()
            if any(self.should_click(screenshot, region) for region in self.regions_of_interest):
                self.click_count += 1
                pyautogui.click()
                if self.should_stop_clicking(screenshot):
                    print("Stopping clicks. Total clicks: ", self.click_count)
                    self.click_count = 0  # Reset click count
        except Exception as e:
            print(f"Error occurred: {e}. Continuing anyway.")

    def should_click(self, screenshot, region):
        """Check if a region meets the click condition."""
        try:
            x1, y1, x2, y2 = region
            region_screenshot = screenshot.crop((x1, y1, x2 + 1, y2 + 1))
            pixel_value = self.get_average_pixel_value(region_screenshot)
            return self.click_condition(pixel_value)
        except Exception as e:
            print(f"Error processing region: {region}. Error: {e}")
            return False

    def should_stop_clicking(self, screenshot):
        """Check if any regions meet the stop condition."""
        for region in self.regions_of_interest:
            if self.stop_condition(self.get_pixel_value(screenshot, region)):
                return True
        return False

    def get_pixel_value(self, screenshot, region):
        """Get the pixel value for a specific region."""
        x1, y1, x2, y2 = region
        pixel = screenshot.getpixel((x1, y1))
        return pixel

    def get_average_pixel_value(self, screenshot):
        """Get the average pixel value of a screenshot."""
        pixel_values = screenshot.massgrabs()
        average_value = sum(pixel_values) / len(pixel_values)
        return average_value

if __name__ == "__main__":
    clicker = ScreenClicker()
    clicker.set_regions([(10, 20, 150, 50), (50, 50, 100, 100)])  # Sample regions

    try:
        while True:
            clicker.click()
            time.sleep(0.5)  # Adjust sleep time as needed
    except KeyboardInterrupt:
        print("Stopping the program.")