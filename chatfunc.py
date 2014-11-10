
class chatFunc:
    def ping(self, ircsock):
        ircsock.send("PONG :Pong\n")
    def sendmsg(channel, msg):
        ircsock.send("PRIVMSG "+ channel +" :"+ msg +"\n")
    def hello(self, channel, ircsock):
        import pychen
        ircsock.send("PRIVMSG "+ channel +" :Hello!\n")
    def latesttldrwiki(self, ircsock):
        linkD = pyscrape.pyScrape()
        pyscrape.resizeImg(linkD['pImage'])
        txt = tldrwiki.outputOCR()
        tldrmsg = txt +" |Date: "+ linkD['pDate'] + " |Link: " + linkD['pImage']
        ircsock.send("PRIVMSG "+ channel +" :"+ tldrmsg + "\n")
