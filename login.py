from playwright.sync_api import sync_playwright
import json

file_path="json/cookies.json"

def save_cookies(cookies, file_path):
    with open(file_path, "w") as f:
        json.dump(cookies, f, indent=4)
    print(f"Cookies sauvegardés dans {file_path}")

def login_and_save_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        )

        page = context.new_page()
        page.goto("https://x.com/login")

        page.wait_for_selector("input[name='text']") 
        page.wait_for_timeout(100000)  

        cookies = context.cookies()
        save_cookies(cookies)

        browser.close()

if __name__ == "__main__":
    login_and_save_cookies()
