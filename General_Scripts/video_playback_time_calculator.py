import os
import subprocess
from ffprobe import FFProbe
def get_length(filename):
    timing = FFProbe(filename).streams[0].duration
    return timing


path = r"E:\Tutorial_videos\corey_s_full_tutorial\Django_Tutorial_Corey_S"

os.chdir(path)
print(os.listdir())
print("stepping towards success.")
videos = os.listdir()
res = get_length(os.path.join(path + videos[1]))