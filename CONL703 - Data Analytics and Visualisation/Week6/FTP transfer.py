#import ftp library
#==========================================
#import ftplib

#set up fto session with tgftp.nws.noaa.gov
#==========================================
#ftp = ftplib.FTP('tgftp.nws.noaa.gov')

# login to FTP
#==========================================
#ftp.login()

# change directories in ftp
#==========================================
#ftp.cwd('data')

# list directories in ftp#
#===========================================
#print(ftp.nlst())


#Then you can fetch, for example, the latest METAR report for
#Chicago O’Hare International Airport:
#===========================================
#x = ftp.retrbinary('RETR observations/metar/decoded',open('KORD.TXT','wb').write)




#SFTP with paramiko
#===========================================
import paramiko as pk



