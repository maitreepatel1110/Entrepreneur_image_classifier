import os
import time
import hashlib
import requests
import io
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fetch_image_urls(query: str, max_links_to_fetch: int, wd: webdriver, sleep_between_interactions: int = 2):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)

    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
    wd.get(search_url.format(q=query))

    print(f"Searching for '{query}'...")
    image_urls = set()
    image_count = 0
    results_start = 0

    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # Use explicit wait for images to load
        try:
            WebDriverWait(wd, 15).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "img.Q4LuWd"))
            )
        except Exception as e:
            print(f"Error waiting for images: {e}")
            continue

        thumbnail_results = wd.find_elements(By.CSS_SELECTOR, "img.Q4LuWd")
        number_results = len(thumbnail_results)

        print(
            f"Found: {number_results} search results for '{query}'. Extracting links...")

        for img in thumbnail_results[results_start:number_results]:
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception as e:
                print(f"Could not click on thumbnail: {e}")
                continue

            # Use explicit wait for the larger image to load
            try:
                actual_images = WebDriverWait(wd, 10).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, 'img.n3VNCb'))
                )
            except Exception as e:
                print(f"Error waiting for actual image: {e}")
                continue

            for actual_image in actual_images:
                src = actual_image.get_attribute('src')
                if src and 'http' in src:
                    print(f"Found image URL: {src}")
                    image_urls.add(src)
                elif src.startswith("data:image"):
                    print(
                        "Found base64 image URL. Skipping as we can't download base64 data directly.")
                else:
                    print(f"Invalid image URL format: {src}")

            image_count = len(image_urls)
            if image_count >= max_links_to_fetch:
                print(
                    f"Found: {len(image_urls)} image links for '{query}', done!")
                break
        else:
            time.sleep(30)
            load_more_button = wd.find_elements(By.CSS_SELECTOR, ".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")
            else:
                break

        results_start = len(thumbnail_results)

    print(f"Returning {len(image_urls)} image URLs for '{query}'")
    return image_urls


def persist_image(folder_path: str, url: str):
    try:
        print(f"Attempting to download image from {url}...")

        # Check if it's base64-encoded image
        if url.startswith('data:image'):
            print("Base64 encoded image, skipping for download")
            return

        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            image_content = response.content
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file).convert('RGB')

            file_path = os.path.join(folder_path, hashlib.sha1(
                image_content).hexdigest()[:10] + '.jpg')
            with open(file_path, 'wb') as f:
                image.save(f, "JPEG", quality=85)
            print(f"SUCCESS - saved {url} as {file_path}")
        else:
            print(
                f"Failed to download {url} with status code {response.status_code}")
    except requests.exceptions.Timeout:
        print(f"Timeout error - could not download {url}")
    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")


def search_and_download(search_terms: list, driver_path: str, target_path='./images', number_images=50):
    for search_term in search_terms:
        target_folder = os.path.join(
            target_path, '_'.join(search_term.lower().split(' ')))

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            print(f"Created folder: {target_folder}")

        service = Service(driver_path)
        with webdriver.Chrome(service=service) as wd:
            res = fetch_image_urls(
                search_term, number_images, wd=wd, sleep_between_interactions=2)

        if res:
            print(
                f"Attempting to download {len(res)} images for {search_term}...")
        else:
            print(f"No image URLs found for {search_term}.")

        for elem in res:
            persist_image(target_folder, elem)


# List of entrepreneurs
entrepreneurs = [
    "Elon Musk", "Jeff Bezos", "Bill Gates", "Mark Zuckerberg",
    "Warren Buffett", "Mukesh Ambani", "Ratan Tata",
    "Gautam Adani", "Azim Premji", "Narayana Murthy"
]

# Call the function
search_and_download(
    entrepreneurs, driver_path="C://Users//maitr//OneDrive//Desktop//chromedriver.exe", number_images=5
)
