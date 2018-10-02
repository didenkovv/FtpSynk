import os
from ftplib import FTP

ftp = FTP('10.30.24.104')
ftp.login("vdidenko", "vdidenko")
ftp.retrlines("LIST")

#ftp.cwd("D:\TEMP\---Q2-2018")
#ftp.cwd("D:\TEMP\---Q2-2018")  # or ftp.cwd("folderOne/subFolder")

listing = []
ftp.retrlines("LIST", listing.append)
words = listing[0].split(None, 8)
filename = words[-1].lstrip()
filenames = ftp.nlst()
print(filenames)

for filename in filenames:
        local_filename = os.path.join(r"D:/ftplocal", filename)
        lf = open(local_filename, "wb")
        ftp.retrbinary("RETR " + filename, lf.write, 8 * 1024)
        lf.close()