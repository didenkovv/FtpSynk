from ftplib import FTP
ftpServerHQ = FTP('localhost')
ftpServerHQ.login(user = 'vdidenko', passwd = 'vdidenko123')
ftpLocalFobler = 'D:/TEMP'
directory = '/01'

print("")



#data = ftpServerHQ.retrlines('LIST')
#print(data)




