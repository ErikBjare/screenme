import os
import subprocess
import time

IMAGE_DIR = os.path.expanduser("~/screenme")


def capture_screenshot(save_path=IMAGE_DIR):
    timestamp = time.strftime("%Y-%m-%d-%H%M%S")
    screenshot_path = os.path.join(IMAGE_DIR, f"{timestamp}_screenshot.png")
    subprocess.run(["escrotum", screenshot_path])
    return screenshot_path
