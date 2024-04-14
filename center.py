import os
def center_text(text):
    # Get terminal dimensions
    terminal_width = os.get_terminal_size().columns
    
    # Calculate padding for centering the text
    padding = (terminal_width - len(text)) // 2
    
    # Create the centered text
    centered_text = ' ' * padding + text
    
    return centered_text