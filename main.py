#!/usr/bin/env python
import time
import logging
import secrets
import tweepy
import settings
from settings import tags, client, me

logger = logging.getLogger(__name__)

def check_tags(text:str, tags:list[str])->bool:
    text = text.lower()
    for tag in tags:
        if text.find(tag) != -1:
            return True
    return False




def follow_friends():
    friend_ids = client.get_friend_ids(count=600)
    for friend_id in friend_ids:
        friend = client.get_user(user_id=friend_id)
        if check_tags(friend.description, tags):
            friend_friends = client.get_friends(user_id=friend.id, count=200)
            for friend_friend in friend_friends:
                if check_tags(friend_friend.description, tags):
                    if friend_friend.id != me.id:
                        try:
                            friend_friend.follow()
                        except tweepy.Forbidden as e:
                            logger.error(e)
                            time.sleep(60)
                        time.sleep(20 * secrets.randbits(4))
                time.sleep(5 * secrets.randbits(3))


if __name__ == "__main__":
    while True:
        follow_friends()
