from playwright.sync_api import sync_playwright
import os
import time
import subprocess

def verify():
    # Start local server
    server_process = subprocess.Popen(["python3", "-m", "http.server", "8000"])
    time.sleep(2)  # Wait for server to start

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            # Create verification directory
            os.makedirs("/home/jules/verification", exist_ok=True)

            # Check contato page for asterisks
            page.goto("http://localhost:8000/contato.html")
            page.screenshot(path="/home/jules/verification/contato_final.png")

            browser.close()
    finally:
        server_process.terminate()

if __name__ == "__main__":
    verify()
