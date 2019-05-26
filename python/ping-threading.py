import subprocess
import os
import threading

def ping(host):
    rc = subprocess.run('ping -c2 %s  &>/dev/null ' % host , shell=True)
    if rc.returncode == 0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)


if __name__ == '__main__':
    ip_all = ['176.52.8.%s' % i for i in range(1,255)]

    for ip in ip_all:
        t = threading.Thread(target=ping , args=(ip,))
        t.start()
