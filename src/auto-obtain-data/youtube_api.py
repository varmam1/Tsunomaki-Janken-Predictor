import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

watame_channel_id = "UCqm3BQLlJfvkTsX_hvm0UmA"
uploads_playlist = "UUqm3BQLlJfvkTsX_hvm0UmA"
api_service_name = "youtube"
api_version = "v3"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=os.environ["API_KEY"])


def getAllUploadsFromWatame():
    """
    Returns the videos that Watame Ch. has on her channel

    Returns:
        videos: A dictionary which has a list of all of the videos. The keys of this dictionary are ['kind', 'etag', 'nextPageToken', 'items', 'pageInfo']. 

    """
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=50,
        playlistId=uploads_playlist
    )
    return request.execute()

def getWatameNoUta(videos):
    """
    Given a response from the youtube API which is a list of videos, returns all of the videos that were Watame no Uta.

    Keyword Arguments:
        videos: A dictionary which has a list of all of the videos. The keys of this dictionary are ['kind', 'etag', 'nextPageToken', 'items', 'pageInfo']. 

    Returns:
        List of videos that had Watame no Uta in the title. The keys of this dictionary will be ['kind', 'etag', 'id', 'snippet', 'contentDetails']
    """
    
    wataUtas = []

    for video in videos['items']:
        if "わためのうた" in video['snippet']['title']:
            wataUtas.append(video)

    return wataUtas
