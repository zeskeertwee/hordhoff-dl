from posixpath import dirname
import requests
import sys
from tqdm import tqdm
import time
import os
import random

if len(sys.argv) < 2:
    print("USAGE: python3 " + sys.argv[0] + " [UUID] [PAGE COUNT END] [PAGE COUNT START]")
    exit(-1)

uuid = sys.argv[1]
base_url = "https://cdp.contentdelivery.nu/" + str(uuid) + "/extract/assets/img/layout"
page_count_end = int(sys.argv[2])

page_count_start = 1
try:
    page_count_start = int(sys.argv[3])
except IndexError:
    print("Using 1 as page start")

print("Using '" + base_url + "' as the base url")
print("Downloading page " + str(page_count_start) + " until " + str(page_count_end) + "\n")

dir_name = "./.nordhoff-downloader-tmp_" + str(random.randint(0, 0xEEEE))
os.mkdir(dir_name)
print("Creating temporary folder '" + dir_name + "'")

for i in tqdm (range(page_count_start, page_count_end+1), desc="Downloading..."):
    file = open(dir_name + "/" + str(i) + ".jpg", "wb")
    data = requests.get(base_url + "/" + str(i) + ".jpg")
    file.write(data.content)
    time.sleep(random.randrange(500, 2000)/1000.0)
    pass

os.system("python3 ./stitch.py " + dir_name + "/ " + str(page_count_end) + " " + str(page_count_start))