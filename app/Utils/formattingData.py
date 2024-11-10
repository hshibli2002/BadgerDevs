def format_product_data(products):
    formatted_data = []
    for product in products:
        name = product.get("Product Title", "N/A")
        description = product.get("Product Description", "N/A")
        link = product.get("Product Link", "N/A")
        price = product.get("Price", "N/A")
        website_source = "Alibaba"
        similarity_score = product.get("Similarity Score", 0.0)

        formatted_data.append([name, description, link, price, website_source, similarity_score])
    return formatted_data
