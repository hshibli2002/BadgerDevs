from datetime import datetime

from app.models.ecommerce_product import EcommerceProduct
from app.models.youtube_video import YoutubeVideo


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

            formatted_data.append([
                name,
                description,
                link,
                price,
                website_source,
                similarity_score
            ])

        else:
            raise ValueError("The product must be an instance of EcommerceProduct.")

    return formatted_data


def format_youtube_data(videos):
    formatted_data = []
    for video in videos:
        if isinstance(video, YoutubeVideo):
            video_dict = video.to_dict()
            title = video_dict.get("video_title", "N/A")
            channel_name = video_dict.get("channel_name", "N/A")
            link = video_dict.get("video_link", "N/A")
            description = video_dict.get("description", "N/A")
            likes = video_dict.get("likes_count", 0)
            views = video_dict.get("views_count", 0)
            published_date_raw = video_dict.get("published_date", "N/A")

            try:
                if published_date_raw != "N/A":
                    published_date = datetime.strptime(published_date_raw,
                                                       "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
                else:
                    published_date = "N/A"
            except ValueError:
                published_date = "Invalid Date"

            formatted_data.append([
                title,
                channel_name,
                link,
                description,
                likes,
                views,
                published_date
            ])
        else:
            raise ValueError("The video must be an instance of YoutubeVideo.")

    return formatted_data
