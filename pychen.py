#!/usr/bin/env python
#http://wiki.shellium.org/w/Writing_an_IRC_bot_in_Python

import socket
import pyscrape
import tldrwiki

server = "irc.drwilco.net"
port = 6667
channel = "#bottest"
botnick = "pychen"
breakit = "\r\n"

def ping():
    ircsock.send("PONG :Pong\n")
def sendmsg(chan, msg):
    ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")
def joinchan(chan):
    ircsock.send("JOIN "+ chan + breakit)
def hello():
    ircsock.send("PRIVMSG "+ channel +" :Hello!\n")
def latesttldrwiki():
    linkD = pyscrape.pyScrape()
    pyscrape.resizeImg(linkD['pImage'])
    txt = tldrwiki.outputOCR()
    tldrmsg = txt +" |Date: "+ linkD['pDate'] + " |Link: " + linkD['pImage']
    ircsock.send("PRIVMSG "+ channel +" :"+ tldrmsg + "\n")
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, port))
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :pychen by danielim"+ breakit)
ircsock.send("NICK "+ botnick + breakit)

joinchan(channel)

while 1:
    ircmsg = ircsock.recv(2048)
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)

    if ircmsg.find(":#Hello "+ botnick) != -1:
        hello()

    if ircmsg.find("PING :") != -1:
        ping()

    if ircmsg.find(":#tldrwiki") != -1:
        latesttldrwiki()
