#!/usr/bin/env python3
"""
essential constants for our app
"""
import json
import os
import logging
import tweepy

logging.basicConfig(
        filename="debug.log",
        filemode="a",
        level="CRITICAL"
    )

tags = []
try:
    with open("tags.json", "r") as fp:
        try:
            tags = json.load(fp)
        except json.JSONDecodeError as e:
            print(e)
            exit()
except FileNotFoundError as e:
    print(e)
    exit()
except PermissionError as e:
    print(e)
    exit()

auth = tweepy.OAuth1UserHandler(
        os.getenv("CONSUMER_KEY"),
        os.getenv("CONSUMER_KEY_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )

client = tweepy.API(auth)
me = client.verify_credentials()

