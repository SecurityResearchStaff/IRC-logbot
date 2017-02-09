import string
import socket
import sys
import os
server = "127.0.0.1"      
channel = "#BOT"
botnick = "DAVID" 
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print "connecting to:"+server
irc.connect((server, 6667))                                             
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :DAVID\n") 
irc.send("NICK "+ botnick +"\n")                
irc.send("PRIVMSG nickserv :DAVID\r\n")    
irc.send("JOIN "+ channel +"\n")       
while 1:   
   text=irc.recv(2040) 
   print text
