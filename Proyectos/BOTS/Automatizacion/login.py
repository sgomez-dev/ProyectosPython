from playwright.sync_api import sync_playwright
import time

timestamp = int(time.time())
email = "santiago@sgomez.dev"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://localhost:4200/auth/login" \
    "")
    time.sleep(3)

    # Completar campos
    page.fill("#email", email)
    page.fill("#pass", "........")
    time.sleep(1)

    # Click en Login
    page.click("text=Iniciar sesión")
    time.sleep(20)

    # Esperar un poco para ver qué pasa
    page.wait_for_timeout(5000)
    browser.close()