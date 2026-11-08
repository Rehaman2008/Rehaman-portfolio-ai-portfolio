import os
import sys
import time
from playwright.sync_api import sync_playwright

BASE_DIR = r"C:\Users\shaik\.gemini\antigravity\scratch\ai-portfolio"
HTML_PATH = os.path.join(BASE_DIR, "index.html")
OUTPUT_PDF = os.path.join(BASE_DIR, "2026BTAI076_Shaik_Rehaman_Shareef_AI_Portfolio.pdf")

def capture_screenshots():
    print("[1/3] Launching browser to capture website screenshots...")
    sections = [
        ("home", "screenshot_1_home.png", "#home"),
        ("about", "screenshot_2_about.png", "#about"),
        ("skills", "screenshot_3_skills.png", "#skills"),
        ("projects", "screenshot_4_projects.png", "#projects"),
        ("achievements", "screenshot_5_achievements.png", "#achievements"),
        ("contact", "screenshot_6_contact.png", "#contact"),
    ]
    
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=2)
        page.goto(f"file:///{HTML_PATH.replace(os.sep, '/')}")
        page.wait_for_load_state("networkidle")
        time.sleep(2) # Allow fonts and animations to settle

        # Capture individual sections
        for name, filename, selector in sections:
            el = page.query_selector(selector)
            out_file = os.path.join(BASE_DIR, filename)
            if el:
                el.scroll_into_view_if_needed()
                time.sleep(0.6)
                el.screenshot(path=out_file)
                print(f"Captured: {filename}")
            else:
                print(f"Selector {selector} not found")

        # Full page overview screenshot
        full_path = os.path.join(BASE_DIR, "screenshot_full_page.png")
        page.screenshot(path=full_path, full_page=True)
        print("Captured full page screenshot")

        browser.close()

if __name__ == "__main__":
    capture_screenshots()
