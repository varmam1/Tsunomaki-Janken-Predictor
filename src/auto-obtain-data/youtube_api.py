import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=os.environ["API_KEY"])

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id="UCqm3BQLlJfvkTsX_hvm0UmA" # Static channel ID for Watame Ch. 
    )
    response = request.execute()

    print(response['contentDetails']['subscriberCount'])

if __name__ == "__main__":
    main()
