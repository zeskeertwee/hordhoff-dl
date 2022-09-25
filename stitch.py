import sys
import os
import random

if len(sys.argv) < 2:
    print("USAGE: python3 " + sys.argv[0] + "[FOLDER PATH] [PAGE END] [PAGE START]")
    exit(-1)

folder_path = sys.argv[1]
page_count_end = int(sys.argv[2])

page_count_start = 1
try:
    page_count_start = int(sys.argv[3])
except IndexError:
    print("Using 1 as page start")

print("Using images from '" + folder_path + "'")
print("Stitching pdf from pages " + str(page_count_start) + " until " + str(page_count_end))

command = "img2pdf --output ./stiched-book-" + str(random.randint(0, 0xEEEE)) + ".pdf "

for i in range(page_count_start, page_count_end+1):
    command += folder_path + str(i) + ".jpg "

print("Invoking img2pdf command")
exitcode = os.system(command)
print("img2pdf finished with code " + str(exitcode))