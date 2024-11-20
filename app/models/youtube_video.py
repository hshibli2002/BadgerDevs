class YoutubeVideo:
    def __init__(self, title, channel_name, link, description, likes, views, published_date):
        """
        Initialize a YoutubeVideo object.
        """
        self.title = title
        self.channel_name = channel_name
        self.link = link
        self.description = description
        self.likes = likes
        self.views = views
        self.published_date = published_date

    def to_dict(self):
        """
        Convert the YoutubeVideo object to a dictionary.
        """
        return {
            "video_title": self.title,
            "channel_name": self.channel_name,
            "video_link": self.link,
            "description": self.description,
            "likes_count": self.likes,
            "views_count": self.views,
            "published_date": self.published_date,
        }
