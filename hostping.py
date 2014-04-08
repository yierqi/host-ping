__author__ = 'chenyongjie'
import os
import time
import subprocess

def ping(host):
    re = subprocess.call('ping -n 1 %s' % host,stdout=open('file','w'))
    if re == 0:
        return 0
    else:
        return 1

def main_app():
    hosts=['211.88.28.35','211.88.22.79','211.88.22.222']
    sum_ok=[]
    sum_bad=[]

    for host in hosts:
        if ping(host)==0:
            sum_ok.append(host)
            print host+' is ok'
        else:
            sum_bad.append(host)
            print host+' is bad'

    print "the ok host is"
    print [i for i in sum_ok]
    print "the bad host is"
    print [i for i in sum_bad]
    time.sleep(10)

while 1:
    main_app()