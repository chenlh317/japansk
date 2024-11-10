"""

TS to mp4:
https://gist.github.com/nhtera/d2a78f607019570d48152ce72fccabd4

Merge mp4:
https://stackoverflow.com/questions/56920546/combine-mp4-files-by-order-based-on-number-from-filenames-in-python

"""

import os

from moviepy.editor import concatenate_videoclips, VideoFileClip
from natsort import natsorted


walk_dir = os.getcwd()
count = 0

L = []

for root, subdirs, files in os.walk(walk_dir):
    files = natsorted(files)

    for file in files:
        if os.path.splitext(file)[1] == ".ts":
            print("Processing: ", file)

            filePath = os.path.join(root, file)

            mp4FilePath = os.path.join(root, os.path.splitext(file)[0] + ".mp4")
            if not os.path.isfile(mp4FilePath):

                os.system("ffmpeg -i " + '"' + filePath + '"' + ' "' + mp4FilePath + '"' + " -loglevel error")

            video = VideoFileClip(mp4FilePath)
            L.append(video)

            count = count + 1

            print("    Done: ", file)

final_clip = concatenate_videoclips(L)
final_clip.to_videofile("output.mp4", fps=24, remove_temp=False)

print("Done the total number of file was be converted: ", count)
