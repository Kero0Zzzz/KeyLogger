# Cross-Platform Keyboard Logger

A Python project demonstrating keyboard-event logging on Windows and Linux, with local log storage and email.

## Features

- Cross-platform: Supports Windows and Linux.
- Local logging: Stores keyboard events generated inside the application's own input window.
- Timestamps: Records the date and time of each event.
- Special keys: Displays key names such as Enter, Space, Shift, and Ctrl when pressed inside the application.
- Lightweight: Uses Python's standard library for the core functionality.
- Standalone builds: Can be packaged separately for Windows and Linux.

## Prerequisites

- Python 3.10 or newer.
- Tkinter for the graphical interface.
- PyInstaller if you want to build a standalone executable.
- A Gmail account and an App Password if testing Gmail SMTP.

### Check your Python installation

# Windows:

```powershell
py --version
```

# Linux:

```bash
python3 --version
```

## Project Structure

```text
CrossPlatformKeylogger/
├── keylogger.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone or download the project

If the project is hosted on GitHub:

```bash
git clone YOUR_REPOSITORY_URL
cd CrossPlatformKeylogger
```

Alternatively, download and extract the repository ZIP file.

### 2. Create a virtual environment

# Windows:

```powershell
py -m venv .venv
.venv\Scripts\activate
```

# Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

The dependencies listed in `requirements.txt` should match the libraries actually imported by the project.

### 4. Install Tkinter if needed

On Ubuntu or Debian:

```bash
sudo apt update
sudo apt install python3-tk
```

On Windows, Tkinter is generally included with the standard Python installer.

## Configuration

Review `config.py` before running the application.

Recommended configuration options include:

- `LOG_FILE`: The local path used for log storage.
- `EMAIL_ADDRESS`: The sender's email address.
- `RECEIVER_EMAIL`: The destination for test reports.

### Gmail SMTP

For Gmail accounts using two-step verification, create an App Password through your Google Account security settings.

Do not commit passwords, tokens, or other secrets to GitHub. Prefer environment variables for credentials and keep them out of source control.

## Usage

Start the application from the project directory.

# Windows:

```powershell
py main.py
```

# Linux:

```bash
python3 main.py
```

The application records keyboard events only while its own input field is focused. Use the application's controls to save the local log or send a predefined email test message.

The exact stop procedure depends on the implementation in `main.py`; document the actual keyboard shortcut or close-window behavior used by your version.

## Build a Windows Executable

### 1. Install PyInstaller

```powershell
py -m pip install pyinstaller
```

### 2. Build

```powershell
py -m PyInstaller --onefile --windowed --name KeyboardLogger main.py
```

The executable should be created at:

```text
dist/KeyboardLogger.exe
```

Build and test the executable on Windows.

## Build a Linux Executable

### 1. Install PyInstaller

```bash
python3 -m pip install pyinstaller
```

### 2. Build

```bash
python3 -m PyInstaller --onefile --windowed --name keyboard-logger main.py
```

The executable should be created at:

```text
dist/keyboard-logger
```

Build and test the Linux executable on Linux. PyInstaller does not normally cross-compile a Windows executable from Linux or a Linux executable from Windows.

## Email Testing

Before using email reporting, test SMTP connectivity with a predefined message that contains no captured keyboard data.

Verify:

1. The sender address is correct.
2. The App Password is valid.
3. Network access to the SMTP server is available.
4. Authentication and connection errors are handled appropriately.

## Troubleshooting

### `ModuleNotFoundError`

Install the missing dependency in the active virtual environment:

```bash
python -m pip install -r requirements.txt
```

### Tkinter is unavailable

On Ubuntu or Debian:

```bash
sudo apt install python3-tk
```

### Gmail authentication fails

- Verify the sender address.
- Use an App Password where required.
- Check that credentials are not expired or mistyped.
- Never publish credentials in the repository.

### The executable does not run on another operating system

Build a separate executable on each target operating system and test it on that platform.

### The application does not respond to keyboard input

Ensure the application's input field has focus and check that the GUI event handler is connected correctly.

## Security and Privacy

- The application should clearly indicate when it is running.
- Keyboard events should be collected only within the application's own input field.
- Do not collect passwords or other sensitive information.
- Do not commit logs or credentials to source control.
- Obtain appropriate authorization before testing email or distributing the application.

