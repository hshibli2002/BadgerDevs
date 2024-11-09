import requests
from app.Utils.config import get_aliexpress_api_config
from app.Utils.similarity_algorithm import calculate_similarity


def fetch_aliexpress_products(keyword, page=1, sort="default", threshold=0.5):
    try:
        base_url, headers = get_aliexpress_api_config()
        endpoint = f"{base_url}/item_search_2"
        params = {
            "q": keyword,
            "page": page,
            "sort": sort
        }

        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        products = data.get("result", {}).get("resultList", [])

        filtered_products = []
        for product in products:
            title = product["item"].get("title", "")
            similarity_score = calculate_similarity(keyword, title)
            product["similarity_score"] = similarity_score

            if similarity_score >= threshold:
                filtered_products.append(product)

        filtered_products = sorted(filtered_products, key=lambda x: x.get("similarity_score", 0), reverse=True)

        return filtered_products

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from AliExpress: {e}")
        return []
