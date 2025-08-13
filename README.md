# Folder Size Analyzer

This is a desktop application built with Python and PyQt6 that helps you visualize the size of folders and their contents on your file system. It provides a tree-like view of a selected directory, displaying the total size of each subfolder in a human-readable format.

# Installation and Setup
## Step 1: Install Python

Ensure you have a recent version of Python (3.6 or higher) installed on your system. You can check your version by running ```python3 --version``` in your terminal.

### Step 2: Set Up a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
ource venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```

### Step 3: Install PyQt6

Once your virtual environment is active, install PyQt6 using pip.

``pip install PyQt6``

### Step 4: Platform-Specific Requirements

- Windows / macOS: No additional steps are usually required.

- Linux: If you encounter the "Could not load the Qt platform plugin 'xcb'" error, install the missing system libraries for your distribution.

    - Debian/Ubuntu: sudo apt-get install libxcb-cursor0

    - Fedora/CentOS: sudo dnf install qt6-qtbase-devel

    - Arch Linux: sudo pacman -S qt6-base

# How to Run the Application

With your virtual environment activated, navigate to the project directory and run the main script.

`python3 main.py`
