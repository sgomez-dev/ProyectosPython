from playwright.sync_api import sync_playwright
import time

timestamp = int(time.time())
email = f"{timestamp}@sgomez.dev"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://localhost:4200/auth/register")
    page.reload()
    time.sleep(3)

    # Completar campos
    page.fill("#name", "Santiago")
    page.fill("#lastName", "Gómez")
    page.fill("#email", email)
    page.fill("#pass", "abc1239900")
    page.fill("#confPass", "abc1239900")
    time.sleep(1)

    print(f"Correo utilizado para registro: {email}")

    # Click en Login
    page.click("text=Registrar")
    time.sleep(20)

    # Esperar un poco para ver qué pasa
    page.wait_for_timeout(5000)
    browser.close()

