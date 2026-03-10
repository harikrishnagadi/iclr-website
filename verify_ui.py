import time
from playwright.sync_api import sync_playwright

def verify_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})

        # Abort external requests
        page.route("**/*", lambda route: route.abort() if not route.request.url.startswith("http://localhost:8000") else route.continue_())

        page.goto('http://localhost:8000')

        # Wait for everything to settle
        time.sleep(2)

        # Hide full screen video
        page.evaluate("""
            const overlay = document.querySelector('.video-fullscreen-overlay');
            if(overlay) overlay.style.display = 'none';
        """)

        # Take a screenshot of the top hero
        page.screenshot(path='screenshot_hero_modern.png')

        # Scroll down
        page.evaluate("window.scrollTo(0, 1000);")
        time.sleep(1)

        # Take a screenshot of the scrolled content
        page.screenshot(path='screenshot_scroll_modern.png')

        browser.close()

if __name__ == '__main__':
    verify_ui()
