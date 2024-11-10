import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.Utils.config import get_scraper_config, setup_driver
from app.Utils.similarity_algorithm import calculate_tfidf_cosine_similarity


def wait_for_page_load(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "app-organic-search__main-body"))
        )
    except Exception as e:
        print("CAPTCHA detected. Pausing to retry later. " + str(e))
        time.sleep(120)


def extract_product_details(product, keyword):
    description_element = product.find_element(By.CSS_SELECTOR, "h2.search-card-e-title")
    description = description_element.text if description_element else "No description available"

    similarity_score = calculate_tfidf_cosine_similarity(keyword, description)

    link_element = product.find_element(By.CSS_SELECTOR, "a")
    link = link_element.get_attribute("href") if link_element else "No link available"
    if link and link.startswith("//"):
        link = "https:" + link

    try:
        price_element = product.find_element(By.CSS_SELECTOR, "div.search-card-e-price-main")
        price = price_element.text if price_element else "No price available"
    except ValueError:
        price = "No price available"

    try:
        issuer_element = product.find_element(By.CSS_SELECTOR, "a.search-card-e-company")
        issuer = issuer_element.text if issuer_element else "No issuer available"
    except ValueError:
        issuer = "No issuer available"

    return {
        "Product Title": keyword,
        "Product Description": description,
        "Product Link": link,
        "Price": price,
        "Issuer": issuer,
        "Similarity Score": similarity_score,
    }


def fetch_alibaba_products(keyword, max_results=10):
    driver = setup_driver()
    config = get_scraper_config()
    product_data = []

    try:
        search_url = f"{config['base_url']}{keyword.replace(' ', '+')}"
        print(f"Fetching data from: {search_url}")
        driver.get(search_url)

        wait_for_page_load(driver)

        products = driver.find_elements(By.CSS_SELECTOR, "div[class*='gallery-card-layout-info']")
        print(f"Found {len(products)} products on the page.")

        for product in products:
            if len(product_data) >= max_results:
                break

            product_details = extract_product_details(product, keyword)

            if product_details["Similarity Score"] < 0.1:
                print("Skipping product due to low similarity score.")
                continue

            product_data.append(product_details)

    except Exception as main_error:
        print(f"Error during fetch operation: {main_error}")

    finally:
        driver.quit()

    return product_data
