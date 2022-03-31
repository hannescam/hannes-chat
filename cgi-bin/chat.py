#!/usr/bin/env python
import cgi
import cgitb
from time import sleep
import Cookie
import os
cgitb.enable()
form = cgi.FieldStorage()
if "text" not in form:
   f = open('/usr/lib/cgi-bin/chat.txt', 'r')
else:
   if "name" not in form:
      nam = os.environ["HTTP_COOKIE"].replace(";", "").replace("UserID=", "")
   else:
      nam = form["name"].value
      cook = Cookie.SimpleCookie()
      cook["UserID"] = nam
      cook["UserID"]["expires"] = 2147483647 #60 * 60 * 24 * 365
      print cook
   f = open('/usr/lib/cgi-bin/chat.txt', 'a')
   f.write(nam+': '+form["text"].value+"\n")
   f.close()
   f = open('/usr/lib/cgi-bin/chat.txt', 'r')
print "Content-type:text/html\r\n\r\n"
#print 'Content-type: text/html\r\n\r'
print '<link rel="stylesheet" type="text/css" href="/chatstyle.css">'
print '<link rel="shortcut icon" href="/chat.ico">'
print '<html>'
print '<title>Hannes Chat</title>'
print '<h1>Hannes Chat</h1>'
print f.read().replace('\n', '<p></p>')
print '<p>&nbsp;</p>'
print '<p><a title="Eine neue Nachricht schreiben, bitte niemand beleidigen! danke" href="/new.html">Neue Nachricht</a></p>'
print '<p><a title="Neue Posts anzeigen" href="/cgi-bin/chat.py">Neu Laden</a></p>'
#sleep(3)
#print '<meta http-equiv=\"refresh\" content=\"0; url = /cgi-bin/chat.py" />'
print '</form>'
print '</html>'
