from ftplib import FTP
import os
ftpServerHQ = FTP('localhost')
ftpServerHQ.login(user = 'vdidenko', passwd = 'vdidenko123')
ftpLocalFobler = 'D:/TEMP'

ftpServerHQ.retrlines("LIST")

##################################################################
### copy name file ftom ftp ###
ftpFilenameFromServer = "1.exe"

#### name filename local file ###
ftpFilenameLocal = "11111.exe"

### local fobler from ftp ###
ftpResultFromFtp = "D:/ftplocal"

#def copyFile():
listing = []
ftpServerHQ.retrlines("LIST", listing.append)
words = listing[0].split(None, 8)
filename = words[-1].lstrip()

local_filename = os.path.join(ftpResultFromFtp, filename)

### copy ftp file ###
ftpServerHQ.retrbinary("RETR " + filename,  open(local_filename, 'wb').write, 8*1024)
print(ftpServerHQ.retrlines('LIST'))
#print(ftpServerHQ.nlst())
ftpServerHQ.close()

##################################################################
#copyFile()
#ftpServerHQ.cwd("")
#ftpServerHQ.retrlines("LIST")
#for files in os.walk("/"):
#    for file in files:
#        ftpServerHQ.retrbinary("RETR " + ftpFilenameFromServer, open(local_filename, 'wb').write)

#import os
import sys
#import fnmatch
#root = 'D:/TEMP'
#pattern = '*.*'
#for folder, subdirs, files in os.walk(root):
   # print(folder)
#    for filename in fnmatch.filter(files, pattern):
#        fullname = os.path.join(folder, filename)
#        print(fullname)