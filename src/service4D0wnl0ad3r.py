'''
Created on 25 Jul 2015

@author: akrv
'''
#!/usr/bin/env python

import sys, time
from daemonizer import Daemon
import pag3F0110w3r

class MyDaemon(Daemon):
        def run(self):
            pag3F0110w3r.run()

if __name__ == "__main__":
        daemon = MyDaemon('/tmp/d0wnl0ad3r.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)