import argparse
import sys
import os 
import bcrypt
import csv
import random
import shutil
import datetime
import string 
import cv2
import re

sys.path.insert(0, os.path.join(os.getcwd(),"vireo-backend/src"))

from database.client import DbClient
from manager.upload import UploadManager


START_DATE = datetime.datetime(2000,1,1)
END_DATE = datetime.datetime.now()


# default
VIDEO_DB = "testdb/videos"
THUMBNAILS_DB = "testdb/thumbnails"
VIDEO_SRC = "tmp"
USER_INFO = ""

TMP_SECRET = "1dcd2fbc17612a8ef4b5c860ed951942989b76f612e952551f9f9865c8344c71"



def random_date():
  return START_DATE + datetime.timedelta(
      seconds=random.randint(0, int((END_DATE - START_DATE).total_seconds())))

def upload(src,cid,title,description,udate,db_client):

    possibility = string.ascii_lowercase + string.ascii_lowercase + string.digits
    path = "".join(random.choice(possibility) for c in range(7))


    query = f"""

            INSERT INTO Videos(
                PathHash,
                ChannelID,
                Title,
                Description,
                Upload
            )
            VALUE (
                '{path}',
                '{cid}',
                '{title}',
                '{description}',
                Date('{udate}')
            );"""
    
    print(query)

    db_client.insert(query)


    shutil.copyfile(src,os.path.join(VIDEO_DB,f"{path}.mp4"))

    setThumbnail(path)

        
def setThumbnail(name):
    #TODO: make sure that the video exist
    video = cv2.VideoCapture(os.path.join(VIDEO_DB,f"{name}.mp4"))
  
    
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)    
    frame_id = random.randint(0, frames)
    

    video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)

    success,frame = video.read()

    cv2.imwrite(os.path.join(THUMBNAILS_DB,f"{name}.png"),frame)
    

# cmdline arg setup
parser = argparse.ArgumentParser()
parser.add_argument("-v","--videos", nargs='?',help="directory where videos to upload should be",type=str)
parser.add_argument("-d","--video-db", nargs='?', help="directory where the video should be store",type=str)
parser.add_argument("-t","--thumbnails", nargs='?', help="where thumbnails should be store",type=str)

args = parser.parse_args()


client = DbClient()
client.initiate_connection(True)
uploader = UploadManager()


# init increment
client.alter("""ALTER TABLE Channels AUTO_INCREMENT = 1""")
client.alter("""ALTER TABLE Videos AUTO_INCREMENT = 1""")

# create channels
x = 0

users = []

with open("data/dbtest/userinfo.csv") as f:

    csv_reader = csv.reader(f,delimiter=",")

    for user in csv_reader:

        if x != 0:

            salt = bcrypt.gensalt(rounds=14)
            passwd = bcrypt.hashpw(user[5].encode('utf-8'), salt).decode('utf-8')

            mname = ""


            if user[1] == '':
                mname = "NULL"
            else:
                mname = f"""'{user[1]}'"""
            print(mname)


            client.insert(f"""
                INSERT INTO Channels ( 
	                Username,
                    Password
                )

                VALUES ('{user[3]}','{passwd}');

                """)

            client.insert(f"""

                INSERT INTO ChannelDetails (
                        ChannelID,
	                    Fname,
                        Mname,
                        Lname,
                        Email,
                        Birth
                    )   
                    VALUES
                    (
                        {x},
                        '{user[0]}',
                        {mname},
                        '{user[2]}',
                        '{user[4]}',
                        Date('{user[6]}')
                    );""")

            users.append(user[3])

        x += 1

      

for video in os.listdir(VIDEO_SRC):

    fp = os.path.join(VIDEO_SRC,video)

    rid = random.randint(0, len(users) -1) + 1

    name = video.split(".")[0]
    
    print(name)

    fapostroph = [ m.start() for m in re.finditer("'", name)]

    add = 0

    if len(fapostroph) != 0:

        for index in fapostroph:

            name = name[:index + add] + "'" + name[index + add:]
            add += 1 

   


    description = f"""a video about {name}"""

    rdate = random_date()

    upload(fp,rid, name, description, rdate, client)




































