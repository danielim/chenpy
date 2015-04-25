#!/usr/bin/env python
'''
pyChen. IRC bot created in python for the entertainment of IRC users.
Author: Daniel Chen
Version: 0.0.1-Alpha
Inspiration from: http://wiki.shelliu.org/w/Writing_an_IRC_bot_in_Python
'''

import socket
import re
from chatfunc import chatFunc

# Connect to server and join channel
class connect:
    def __init__(self, server, port, channel, botnick):
        self.server = server
        self.port = port
        self.channel = channel
        self.botnick = botnick
        self.br = "\r\n"
        self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.ircsock.connect((self.server, self.port))
        self.ircsock.send("USER "+ self.botnick +" "+ self.botnick +" "+ self.botnick +" :pychen by danielim"+ self.br)
        self.ircsock.send("NICK "+ self.botnick + self.br)
        self.ircsock.send("JOIN "+ self.channel + self.br)
    def loopy(self):
        while 1:
            ircmsg = self.ircsock.recv(2048)
            ircmsg = ircmsg.strip('\n\r')
            print(ircmsg)
            cf = chatFunc() 

            if ircmsg.find("PING :") != -1:
                self.ircsock.send("PONG :Pong\n")

            # split ircmsg
            # ircarg[0] = User
            # ircarg[1] = IRC command (PRIVMSG, NICK, etc)
            # ircarg[2] = Channel
            # ircarg[3] = Message
            else:
                try:
                    ircarg = ircmsg.split(" ", 3)
                    if ircarg[3][1:2] == "|":
                        cmd = ircarg[3][2:]
                        usr = re.search("(?<=:)(.*)(?=\!)", ircarg[0]).group(1)
                        cf.handshaker(usr, self.channel, self.ircsock, cmd) 
                        
                # This exception mostly only handles nickname change, this is because /nick only has 3 parts, can't be split 3 times.
                except Exception as e:
                    print e 

#            if ircmsg.find(":|Hello "+ self.botnick) != -1:
#                cf.hello(self.channel, self.ircsock)
#        
#            if ircmsg.find(":|tldrwiki") != -1:
#                cf.latesttldrwiki(self.ircsock)

if __name__ == "__main__":
    irc = connect("anarchy.tamu.edu", 6667, "#bottest", "pychen")
    irc.loopy()
