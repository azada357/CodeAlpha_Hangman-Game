#✅ TASK 3: Task Automation with Python Scripts 
# Goal: Automate a small, real-life repetitive task. 
# Pick One of These Ideas: 
# ● Move all .jpg files from a folder to a new folder. 
# ● Extract all email addresses from a .txt file and save them to another file. 
# ● Scrape the title of a fixed webpage and save it. 
# Key Concepts Used: os, shutil, re, requests, file handling.
import os
import shutil
import re
x = os.getcwd()
import os
import shutil
import re



import os
import shutil
import re
x = os.getcwd()
files = os.listdir()

print(files)

if not os.path.exists("Images"):
    os.mkdir("Images")

for file in files:
    print("Checking:", file)

    if re.search(r"\.(jpg|jpeg|png)$", file, re.IGNORECASE):
        print("Moving:", file)

        shutil.move(file, f"Images/{file}")

with open("log.txt", "a") as log:
    log.write("Images organized\n")
