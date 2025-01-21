
# Digital Clock

## Description
This script creates a simple digital clock using Python's Tkinter library. The clock displays the current time and date in a user-friendly graphical interface.

## Features
- Displays the current time in **HH:MM:SS** format.
- Displays the current date in **MM/DD/YY** format.
- Updates the time every second dynamically.

## Prerequisites
- Python 3.x
- Tkinter library (comes pre-installed with Python on most systems).

## Installation
1. Clone this repository or download the script.
2. Ensure Python is installed on your system.
3. Run the script using:
   ```bash
   python digital_clock.py
   ```

## Usage
1. Launch the script.
2. The clock will display the current time and date, updating every second.
3. Close the application to exit.

## How It Works
- The `strftime` function from the `time` module fetches the current time and date.
- A `Label` widget displays the time and date in a graphical interface.
- The `after` method ensures the time updates every second.

## Customization
- **Font**: The font can be changed by modifying the `font` parameter in the `Label` widget.
- **Background and Foreground Colors**: Customize the `background` and `foreground` parameters to your preference.
- **Time Format**: Modify the `strftime` format string to change the display format.

## Example
The clock interface will display:
```
HH:MM:SS
MM/DD/YY
```


## Acknowledgements
- Built using Python's `tkinter` library.
- Real-time updates powered by the `time.strftime` function.
