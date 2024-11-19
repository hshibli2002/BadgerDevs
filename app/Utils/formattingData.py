from app.models.ecommerce_product import EcommerceProduct


def format_product_data(products):
    formatted_data = []
    for product in products:
        if isinstance(product, EcommerceProduct):
            product_dict = product.to_dict()
            name = product_dict.get("Product Title", "N/A")
            description = product_dict.get("Product Description", "N/A")
            link = product_dict.get("Product Link", "N/A")
            price = product_dict.get("Price", "N/A")
            website_source = product_dict.get("Website Source", "N/A")
            similarity_score = product_dict.get("Similarity Score", 0.0)

            formatted_data.append([name, description, link, price, website_source, similarity_score])
        else:
            raise ValueError("The product must be an instance of EcommerceProduct.")

    return formatted_data
