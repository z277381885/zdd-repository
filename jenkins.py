import requests
import wget
import os
import hashlib
import tarfile

def has_new_ver(ver_fname,ver_url):
    if not os.path.isfile(ver_fname):       #判断本地有没有版本文件
        return True

    with open(ver_fname) as fobj:           #如果存在则打开
        local_ver = fobj.read()             #读取版本文件内容赋值给local_ver

    r = requests.get(ver_url)               #get远程jenkins的版本文件
    remote_ver = r.text                     #读取内容.文本格式,读取赋值给remote_ver

    if local_ver != remote_ver:             #本地和远程版本信息对比
        return True
    return False


def has_error(fname,md5_url):
    m = hashlib.md5()                   #创建md5文件
    with open(fname,'rb') as fobj:      #打开
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    r = requests.get(md5_url)
    if m.hexdigest() == r.text.strip():
        return False
    return True


def deploy(app_fname):
    ##此时app_fname为/var/www/download/myweb-1.0.tar.gz
    #先解压缩
    deploy_dir = '/var/www/deploy/'
    tar = tarfile.open(app_fname,'r:gz')
    tar.extractall(path=deploy_dir)
    tar.close()

    #拼出解压目录的绝对路径
    app_path = os.path.basename(app_fname)        #只取myweb-1.0.tar.gz
    app_path = app_path.replace('.tar.gz','')      #只取myweb-1.0
    app_path = os.path.join(deploy_dir,app_path)   #合并网页实际路径/var/www/deploy/myweb-1.0
    # print(app_path)       #测试用
    #创建连接,如果连接已存在,先删除它
    link = '/var/www/html/nsd1811'   #创建连接指向网页/var/www/deploy/myweb-1.0
    if os.path.exists(link):        #判断删除原链接
        os.remove(link)
    os.symlink(app_path,link)

if __name__ == '__main__':
    app_dir = '/var/www/download'
    ver_fname = '/var/www/deploy/live_ver'
    ver_url = 'http://192.168.4.4/deploy/live_ver'
    if not has_new_ver(ver_fname,ver_url):      #使用has_new_ver函数判断有没有新版本
        print('没有新版本')
        exit(1)

    #如果有新版本,则下载
    r = requests.get(ver_url)
    ver = r.text.strip()                 #获取服务器上的版本号
    app_url = 'http://192.168.4.4/deploy/packages/myweb-%s.tar.gz' % ver #最新版本包的地址
    wget.download(app_url, app_dir)      #下载最新版本的包

    #校验下载的压缩包是否损坏
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(app_dir , app_fname)   #拼接压缩包的绝对路径

    md5_url = app_url + '.md5'  #拼出md5值的网址

    if has_error(app_fname, md5_url):
        print('文件已损坏')
        os.remove(app_fname) #如果文件损坏,则删除它
        exit(2)
    print('文件未损坏')
    #如果下载的文件是完好的,则部署
    deploy(app_fname)
    #更新本地版本文件
    with open(ver_fname,'w') as fobj:
        fobj.write(r.text)      #r在下载版本那requests.get(ver_url)








