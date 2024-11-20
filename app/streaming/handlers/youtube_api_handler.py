import os

from app.Utils.config import youtube_build
from app.models.youtube_video import YoutubeVideo


def youtube_metadata_search(query, max_results=25):
    """
    Fetches video metadata from YouTube based on the provided query.

    :param query: The query to search for on YouTube.
    :param max_results: The maximum number of results to return.

    :return: List of YoutubeVideo objects containing the extracted metadata.
    """
    youtube = youtube_build()

    search_query = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=max_results,
        type='video',
        order='relevance',
        safeSearch='strict',
    ).execute()

    video_metadata = []

    for item in search_query['items']:
        video_title = item['snippet']['title']
        video_id = item['id']['videoId']
        channel_title = item['snippet']['channelTitle']
        published_at = item['snippet']['publishedAt']
        description = item['snippet']['description']

        video_statistics = youtube.videos().list(
            part='statistics',
            id=video_id
        ).execute()

        view_count = video_statistics['items'][0]['statistics'].get('viewCount', 0)
        like_count = video_statistics['items'][0]['statistics'].get('likeCount', 0)

        video = YoutubeVideo(
            video_title,
            channel_title,
            f'{os.getenv("YOUTUBE_BASE_URL")}{video_id}',
            description,
            like_count,
            view_count,
            published_at)

        video_metadata.append(video)

    return video_metadata
