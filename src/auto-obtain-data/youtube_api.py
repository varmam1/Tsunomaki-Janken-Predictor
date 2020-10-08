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
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=25,
        playlistId=uploads_playlist
    )
    return request.execute()
