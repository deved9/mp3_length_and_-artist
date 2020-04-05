from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import os
from stat import *

path = input("path to directory with mp3: ")
path = os.path.abspath(path)

def iterate_in_folder(path):
    ln = 0
    num = 0
    for item in os.listdir(path):
        if S_ISDIR(os.stat(os.path.join(path,item))[ST_MODE]):
            iterate_in_folder(os.path.join(path,item))
        elif item.endswith("mp3"):
            audio = MP3(os.path.join(path,item))
            print(str(item) + "  " + str(audio.info.length))
            try:
                audio = EasyID3(os.path.join(path,item))
                if audio["artist"] != item[:item.index("-")-1]:
                    audio["artist"] = item[:item.index("-")-1]
                    audio.save(v2_version=3)
            except ValueError:
                pass

iterate_in_folder(path)