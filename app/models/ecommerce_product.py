class EcommerceProduct:
    def __init__(self, title, description, link, price, website_source, similarity_score):
        """
        Initialize an EcommerceProduct object.
        """
        self.title = title
        self.description = description
        self.link = link
        self.price = price
        self.website_source = website_source
        self.similarity_score = similarity_score

    def to_dict(self):
        """
        Convert the EcommerceProduct object to a dictionary.
        """
        return {
            "Product Title": self.title,
            "Product Description": self.description,
            "Product Link": self.link,
            "Price": self.price,
            "Website Source": self.website_source,
            "Similarity Score": self.similarity_score,
        }
