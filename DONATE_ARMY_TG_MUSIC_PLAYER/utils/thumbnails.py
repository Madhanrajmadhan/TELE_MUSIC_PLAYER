#
# Copyright (C) 2024 by DONATE_ARMY™@Github, < https://github.com/DONATE-ARMY-BOTS >.
#
# This file is part of < https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER > project,
# and is released under the MIT License.
# Please see < https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER/blob/master/LICENSE >
#
# All rights reserved.
#

from youtubesearchpython.__future__ import VideosSearch

from config import YOUTUBE_IMG_URL


async def gen_thumb(videoid):
    try:
        query = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        return thumbnail
    except Exception as e:
        return YOUTUBE_IMG_URL


async def gen_qthumb(vidid):
    try:
        query = f"https://www.youtube.com/watch?v={vidid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        return thumbnail
    except Exception as e:
        return YOUTUBE_IMG_URL


from youtubesearchpython.__future__ import VideosSearch


async def get_thumb(videoid):
    try:
        # Search for the video using video ID
        query = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        return thumbnail
    except Exception as e:
        return config.YOUTUBE_IMG_URL


async def get_thumb(vidid):
    try:
        # Search for the video using video ID
        query = f"https://www.youtube.com/watch?v={vidid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        return thumbnail
    except Exception as e:
        return config.YOUTUBE_IMG_URL
