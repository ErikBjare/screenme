import os
import time

import click
from .screenshot import capture_screenshot
from .webcam import capture_webcam_image


@click.command()
@click.option(
    "--interval",
    default=60,
    help="Interval in seconds between captures. Default is 60 seconds.",
)
def main(interval):
    """Capture webcam and screen images at regular intervals."""
    while True:
        # Define the directory structure
        date_dir = time.strftime("%Y-%m-%d")
        time_dir = time.strftime("%H-%M")
        base_dir = os.path.expanduser("~/screenme/shots")
        full_dir = os.path.join(base_dir, date_dir, time_dir)

        # Create directories if they don't exist
        os.makedirs(full_dir, exist_ok=True)

        # Capture and save screenshot
        screenshot_path = os.path.join(full_dir, "screenshot.png")
        capture_screenshot(screenshot_path)

        # Capture and save webcam image
        webcam_path = os.path.join(full_dir, "webcam.png")
        capture_webcam_image(webcam_path)

        # Wait for the specified interval
        time.sleep(interval)


if __name__ == "__main__":
    main()
