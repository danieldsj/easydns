#!/usr/bin/env python
import urllib2
import sys
import base64

# This is a test comment

try:
    username = sys.argv[1]
    password = sys.argv[2]
    hostname = sys.argv[3]
    url = "http://members.easydns.com" + \
       "/dyn/dyndns.php?" + \
       "hostname=%s&" % hostname + \
       "myip=1.1.1.1"
except:
    print 'Usage: %s <username> <password> \
        <dynamic dns hostname>' % sys.argv[0] 
    sys.exit()

try:
    request = urllib2.Request(url)
    base64string = base64.encodestring('%s:%s' %
        (username, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    result = urllib2.urlopen(request)
    for i in result:
        print i
except:
    print 'Usage: %s <username> <password> \
        <dynamic dns hostname>' % sys.argv[0] 
    sys.exit()
