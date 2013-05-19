#!/usr/bin/env python
import urllib2
import sys
import base64

class EasyDNS:
    username = None
    password = None
    hostnames = []

    def set_username(self,username):
	'''sets username'''
	self.username = username

    def set_password(self,password):
	'''sets password'''
        self.password = password

    def set_hostname(self,hostname):
	'''sets hostname'''
        self.hostname = hostname 

    def print_usage(self):
	'''generates usage output'''
        print('Usage: %s ' % sys.argv[0] + \
            '<username> <password> <dynamic dns hostname>')

    def parse_arguments(self, arguments=sys.argv[1:]):
	'''parses command line arguments if running as a script'''
	self.set_username(arguments[0])
	self.set_password(arguments[1])
        self.set_hostname(arguments[2])

    def run(self):
	'''runs the class as an application'''
        base64string = base64.encodestring('%s:%s' %
            (self.username, self.password)).replace('\n', '')
       
	url = "http://members.easydns.com" + \
           "/dyn/dyndns.php?" + \
           "hostname=%s&" % self.hostname + \
           "myip=1.1.1.1"
        request = urllib2.Request(url)
        request.add_header("Authorization", "Basic %s" % base64string)
        result = urllib2.urlopen(request)
        for i in result:
            print i

if __name__ == "__main__":
    app = EasyDNS()
    try:
        app.parse_arguments()
	app.run()
    except Exception, e:
	app.print_usage()
	print e
