from selenium import webdriver
import os
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

urls = [
    "https://www.getcalley.com/",
    "https://www.getcalley.com/calley-call-from-browser/",
    "https://www.getcalley.com/calley-pro-features/",
    "https://www.getcalley.com/best-auto-dialer-app/",
    "https://www.getcalley.com/how-calley-auto-dialer-app-works/"
]
resolutions = {
    "Desktop": [
        {"width": 1920, "height": 1080},
        {"width": 1366, "height": 768},
        {"width": 1536, "height": 864}
    ],
    "Mobile": [
        {"width": 360, "height": 640},
        {"width": 414, "height": 896},
        {"width": 375, "height": 667}
    ]
}

# browsers = ["Chrome", "Firefox", "Safari"]
browsers = ["Chrome","Firefox"]
os.makedirs("screenshots", exist_ok=True)


for browser in browsers:
    for device, device_resolutions in resolutions.items():
        for resolution in device_resolutions:
          
            if browser == "Chrome":
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("--headless")
                driver = webdriver.Chrome(options=chrome_options)
            elif browser == "Firefox":
                firefox_options = webdriver.FirefoxOptions()
                firefox_options.add_argument("--headless")
                driver = webdriver.Firefox(options=firefox_options)
                
            else:
                print("Unsupported browser:", browser)
                continue
            
   
            driver.set_window_size(resolution["width"], resolution["height"])
            
            for url in urls:

                print(f"-------Taking Screenshot for {url} in {browser} for {device} at {resolution} -------")
                driver.get(url)
              
                # wait = WebDriverWait(driver, 10)
                # wait.until(EC.url_to_be(url))
                screenshot_name = f"screenshots/{browser}/{device}/{resolution['width']}x{resolution['height']}/{url.replace('https://', '').replace('/', '-')}"
                os.makedirs(os.path.dirname(screenshot_name), exist_ok=True)
                # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                height = driver.execute_script("return document.body.scrollHeight")
                driver.set_window_size(resolution["width"], height)

                date_time = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                driver.save_screenshot(f"{screenshot_name}-{date_time}.png")
            
            driver.quit()
