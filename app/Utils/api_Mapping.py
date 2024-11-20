"""Summary:
In this snippet, we are defining a mapping of website names to their corresponding API functions.
This mapping is used to dynamically call the correct API function based on the website name provided.
"""
from app.ecommerce.controllers.alibaba_controller import search_and_store_products as alibaba_function
from app.ecommerce.controllers.asos_controller import search_and_store_products as asos_function
from app.streaming.controllers.youtube_api_controller import search_youtube as youtube_function

WEBSITE_APIS = {
    "asos": asos_function,
    "alibaba": alibaba_function,
    "youtube": youtube_function,
}
