import sys
from urllib import request



def download(url,fname):

    r = request.urlopen(url)
    with open(fname,'wb') as fobj:
        while True:
            data=r.read(1024)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    download(sys.argv[1] , sys.argv[2])











