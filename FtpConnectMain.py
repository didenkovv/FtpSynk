from ftplib import FTP
import os
ftpServerHQ = FTP('localhost')
ftpServerHQ.login(user = 'vdidenko', passwd = 'vdidenko123')
ftpLocalFobler = 'D:/TEMP'

### copy file ftom ftp ###
ftpFilenameFromServer = "1.exe"

#### name filename local file ###
ftpFilenameLocal_ = "11111.exe"
#
local_filename = os.path.join("D:/" , ftpFilenameLocal_)
### copy ftp file ###
ftpServerHQ.retrbinary("RETR " + ftpFilenameFromServer, open(local_filename, 'wb').write)
ftpServerHQ.close()





