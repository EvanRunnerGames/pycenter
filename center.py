import os
import time

global refresh_rate

def center_text(text):
    while True:
        refresh_rate = 1
        time.sleep(refresh_rate)
        # Get terminal dimensions
        terminal_width = os.get_terminal_size().columns
        
        # Calculate padding for centering the text
        padding = (terminal_width - len(text)) // 2
        
        # Create the centered text
        centered_text = ' ' * padding + text
        
        return centered_text
