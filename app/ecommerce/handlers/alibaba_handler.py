from selenium.webdriver.common.by import By
from app.Utils.config import get_scraper_config, wait_for_page_load, setup_driver
from app.Utils.similarity_algorithm import calculate_tfidf_cosine_similarity
from app.models.ecommerce_product import EcommerceProduct


def extract_alibaba_product_metadata(product, keyword):
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

    return EcommerceProduct(
        title=keyword,
        description=description,
        link=link,
        price=price,
        website_source="Alibaba",
        similarity_score=similarity_score,
    )


def fetch_alibaba_products(keyword, max_results=10, max_pages=10):
    driver = setup_driver("alibaba")
    config = get_scraper_config("alibaba")
    product_data = []
    page_number = 0

    try:
        while len(product_data) < max_results and page_number < max_pages:
            page_number += 1
            print(f"Parsing page {page_number}")

            search_url = f"{config['base_url']}{keyword.replace(' ', '+')}&page={page_number}"
            print(f"Fetching data from: {search_url}")

            driver.get(search_url)
            wait_for_page_load(driver, By.CSS_SELECTOR, "app-organic-search__main-body")

            products = driver.find_elements(By.CSS_SELECTOR, "div[class*='gallery-card-layout-info']")
            print(f"Found {len(products)} products on the current page.")

            for product in products:
                if len(product_data) >= max_results:
                    break

                try:
                    product_details = extract_alibaba_product_metadata(product, keyword)
                    if product_details.similarity_score >= 0.25:
                        product_data.append(product_details)
                        print(f"Product details extracted: {product_details}")
                    else:
                        print(f"Product similarity score too low: {product_details.similarity_score}")
                except Exception as e:
                    print(f"Error extracting product details: {e}")

    except Exception as main_error:
        print(f"Error during fetch operation: {main_error}")

    finally:
        driver.quit()

    return product_data
