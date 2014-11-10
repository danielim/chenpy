import re
s = ':daniel!~daniel@75-1-51-146.lightspeed.snantx.sbcglobal.net PRIVMSG #bottest :ok added test against | not being the first character'
si = ':daniel!~daniel@75-1-51-146.lightspeed.snantx.sbcglobal.net PRIVMSG #bottest :|test'
arr = ["this", "that", 123]
print arr + s
if '|' in s:
    try:
        cmd1 = s.split(' ', 3)
        if cmd1[3][1:2] == '|':
            print "success 1"
        else:
            print "fail 1"
    except:
        print "bhe" 
if '|' in si:
        cmd2 = si.split(' ', 3)
        usr = re.search("(?<=:)(.*)(?=\!)", cmd1[0]).group(1)
        if cmd2[3][1:2] == '|':
            print usr
            print "success 2"
        else:
            print cmd 
            print "fail 2"
