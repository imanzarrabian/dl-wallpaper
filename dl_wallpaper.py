import requests
from random import randint
import urllib
import time
import sys


wallpaper_source = " https://api.desktoppr.co/1/users/"

#replace by your auth_token
auth_token = ""

#replace by users you like on desktoppr.co
user_worth_looking = ["sutto", "vertis", "gotmug"]

def get_random_wallpaper_from_user(username):
    url = wallpaper_source + str(username)+ "/wallpapers/random"
    r = requests.get(url = url)
    params = {"auth_token": str(auth_token)}

    if r.status_code == 200:
        return r.json()["response"]["image"]["url"]
    else:
        print r.text
        sys.exit("GET /wallpaper/random response not parsed")


if auth_token == "":
    print "Need auth_token from Desktoppr"
    sys.exit()

# get a random user
index = randint(0, 1)
username = user_worth_looking[index]

#download and write to file
wallpaper_url = get_random_wallpaper_from_user(username)
print "Downloading: " + wallpaper_url
ts = time.time()
urllib.urlretrieve(wallpaper_url, username + str(int(ts)) +  ".jpg")
