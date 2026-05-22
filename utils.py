

# Import os, time format change, clean the screen
# Author: Chen Hu
# When: May 22, 2026


import os

def time_to_seconds(time_str):
    """
    Input: string in "hh:mm:ss" time format
    Returns: total seconds in the time string
    Working: converts the time string into total seconds
    """
    parts = time_str.split(":")

    if len(parts) == 3:
        hours, minutes, seconds = int(parts[0]), int(parts[1]), int(parts[2])
    elif len(parts) == 2:
        minutes, seconds = int(parts[0]), int(parts[1])
        hours = 0
    else:
        raise ValueError("Invalid time format")

    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Invalid time format")
    if minutes >= 60 or seconds >= 60:
        raise ValueError("Invalid time format")

    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def seconds_to_time_format(seconds):
    """
    Input: total seconds in the time string
    Returns: string in "hh:mm:ss" time format
    Working: converts the total seconds into a time string
    """
    if seconds < 0:
        raise ValueError("Seconds cannot be negative")

    hours = seconds//3600
    remainder = seconds%3600
    minutes = remainder//60
    seconds = remainder%60

    if hours > 0:
        return f"{hours}:{minutes:02}:{seconds:02}"
    else:
        return f"{minutes}:{seconds:02}"

def clear():
    """
    Input: None
    Returns: None
    Working:
    This function clears terminal screen
    """
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')