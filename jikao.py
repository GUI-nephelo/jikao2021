from urllib.request import *
from urllib.error import *
import socket
import os,time

Burl = "http://222.249.128.24:8088/01-jikao/jikao_gz/photo/100161/%s.jpg"
pingUrl = "http://222.249.128.24:8088/01-jikao/jikao_gz/photo/%s/"

districtCode = "110101"

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def ping(id):
    url = pingUrl %(str(id))
    try:
        r = urlopen(url, timeout=5).read()
        print(r)
    except HTTPError as e:
        if e.code==403:
            print(url,e)
    except socket.timeout as e:
        print(url,e)
        ping(id)
    except URLError as e:
        print(url,e)
        ping(id)

def _getTimeF():
    return "[%s]"%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

def download(xkid,dc,c=0):
    global Burl
    url= Burl %(xkid)
    print(url)
    try:
        r = urlopen(url, timeout=5).read()
        open("%s\\%s.JPG" % ("JIKAO"+dc, xkid), "wb").write(r)
        return True
    except HTTPError as e:
        print(e)
        open("log.txt","a").write("%s error %s %s\n"%(_getTimeF(),xkid,str(e)))
        return False
    except socket.timeout as e:
        print(url,e)
        download(xkid,dc)
    except URLError as e:
        print(url,e)
        download(xkid,dc)
    

def fix(i,c=4):
    r = i
    while len(r)<c:
        r="0"+r
    return r

def main(dc):
    mkdir("JIKAO"+dc)
    c=0
    for i in range(1609,10000):
        if c>=100:
            print(dc,"ok")
            return 
        bid = "21"+dc+"10"+fix(str(i))
        s = download(bid,dc)
        if not s:
            c+=1
        else: 
            c=0
if __name__ == "__main__":
    #open("log.txt","w").close()
    a=["1101"+fix(str(i),c=2) for i in range(6,20)]
    a.remove("110110")
    a.remove("110112")
    print(a)
    for i in a:
        main(i)
    """
    for i in range(100141,100500):
        ping(i)
    """
