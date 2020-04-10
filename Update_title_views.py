# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import time
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube"]
if 2>1:


    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_970683916447-6vcgljur35tai67a47bom561mnemoie1.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    while 2>1:
        request = youtube.videos().list(
        part="statistics",
        id="7LN6b3OOLt8"
        )
        response = request.execute()
        viewcount = str(response)
        viewcount = viewcount[316:318]
        print(response)
        print(viewcount)
        lastviews = 0
        if lastviews != viewcount:
                lastviews = viewcount
                request = youtube.videos().update(
                part="snippet,status,localizations",
                body={
                    "id": "7LN6b3OOLt8",
                    "localizations": {
                        "es": {
                            "title": "no hay nada a ver aqui",
                            "description": "Esta descripcion es en español."
                        }
                    },
                    "snippet": {
                        "categoryId": "22",
                        "defaultLanguage": "en",
                        "description": "This is the video that i saw: https://www.youtube.com/watch?v=BxV14h0kFs0&t=7s\n this is the code: https://throwbin.io/pmnOpPp",
                        "tags": [
                            "new tags"
                        ],
                        "title": "This video currently has " + viewcount + " views."
                    },
                    "status": {
                        "privacyStatus": "public"
                    }
                }
            )
        response = request.execute()

        print(response)


