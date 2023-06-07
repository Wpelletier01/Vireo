
import shutil
import os




VIDEO_DB = "testdb/videos"
THUMBNAILS_DB = "testdb/thumbnails"



for video in os.listdir(VIDEO_DB):

    p = os.path.join(VIDEO_DB,video)

    os.remove(p)

for thumb in os.listdir(THUMBNAILS_DB):

    p = os.path.join(THUMBNAILS_DB,thumb)

    os.remove(p)