class EcommerceProduct:
    def __init__(self, title, description, link, price, website_source, similarity_score):
        self.title = title
        self.description = description
        self.link = link
        self.price = price
        self.website_source = website_source
        self.similarity_score = similarity_score

    def to_dict(self):
        return {
            "Product Title": self.title,
            "Product Description": self.description,
            "Product Link": self.link,
            "Price": self.price,
            "Website Source": self.website_source,
            "Similarity Score": self.similarity_score,
        }

    def __str__(self):
        return (f"EcommerceProduct(title={self.title}, "
                f"description={self.description}, "
                f"price={self.price})")
