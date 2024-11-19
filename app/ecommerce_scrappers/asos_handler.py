from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from app.Utils.config import setup_driver, get_scraper_config, wait_for_page_load
from app.Utils.similarity_algorithm import calculate_tfidf_cosine_similarity
from app.models.ecommerce_product import EcommerceProduct


def extract_asos_product_metadata(product, keyword):
    description_element = product.find_element(By.CSS_SELECTOR, "div.productInfo_rwyH5 > p.productDescription_sryaw")
    description = description_element.text if description_element else "No description available"

    similarity_score = calculate_tfidf_cosine_similarity(keyword, description)

    link_element = product.find_element(By.CSS_SELECTOR, "a.productLink_KM4PI")
    link = link_element.get_attribute("href") if link_element else "No link available"

    price = 0.0

    try:
        original_price_element = product.find_element(By.CSS_SELECTOR, "span.originalPrice_jEWt1 span.price__B9LP")
        price = original_price_element.text if original_price_element else "No original price available"
        print(f"Original Price: {price}")
    except Exception as e:
        print(f"Error fetching original price: {e}")

    try:
        reduced_price_element = product.find_element(By.CSS_SELECTOR, "span.reducedPrice_lsM0L")
        price = reduced_price_element.text if reduced_price_element else "No reduced price available"
        print(f"Reduced Price: {price}")
    except NoSuchElementException:
        print("No reduced price available")

    return EcommerceProduct(
        title=keyword,
        description=description,
        link=link,
        price=price,
        website_source="ASOS",
        similarity_score=similarity_score,
    )


def fetch_asos_products(keyword, max_results=10):
    driver = setup_driver("asos")
    config = get_scraper_config("asos")
    product_data = []
    page_number = 0

    try:
        while len(product_data) < max_results:
            page_number += 1
            print(f"Parsing page {page_number}")

            search_url = f"{config['base_url']}{keyword.replace(' ', '+')}&page={page_number}"
            print(f"Fetching data from: {search_url}")

            driver.get(search_url)

            wait_for_page_load(driver, By.CSS_SELECTOR, "div.container_yiEoY.wrapper_UjNAa")

            products = driver.find_elements(By.CSS_SELECTOR, "section.listingPage_HfNlp article")
            print(f"Found {len(products)} products on the current page.")

            for product in products:
                if len(product_data) >= max_results:
                    break
                try:
                    product_details = extract_asos_product_metadata(product, keyword)
                    if product_details.similarity_score >= 0.25:
                        product_data.append(product_details)
                        print(f"Product details extracted: {product_details}")
                    else:
                        print(f"Cosine similarity score is below threshold: {product_details.similarity_score}"
                              f" Skipping product.")
                except Exception as e:
                    print(f"Error extracting product details: {e}")

    except Exception as e:
        print(f"Error fetching data: {e}")

    finally:
        driver.quit()

    return product_data
