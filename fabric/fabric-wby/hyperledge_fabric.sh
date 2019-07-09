环境配置
Git client
Go - 及1.6 以上
Vagrant - 1.7.4 及以上
VirtualBox - 5.0 及以上
BIOS中设置Virtualization为Enabled
提示: BIOS的Virtualization选项应该在CPU或者Security设置中

#!/bin/bash
sed "s/#UseDNS yes/UseDNS no/g" /etc/ssh/sshd_config
systemctl restart sshd
##go语言环境搭建
yum -y install wget git expect epel-release
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
yum clean all
yum makecache
wget -P /opt/ https://dl.google.com/go/go1.12.2.linux-amd64.tar.gz
tar zxf /opt/go1.12.2.linux-amd64.tar.gz -C /usr/local/

mkdir -p /opt/fabric-deploy/GOPATH/src/github.com/

##安装docker
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum install docker-ce docker-ce-cli containerd.io -y

systemctl start docker
cat > /etc/docker/daemon.json << EOF
{
  "registry-mirrors": ["https://registry.docker-cn.com"]
}
EOF
systemctl restart docker

##Docker-Compose安装
yum install python-pip -y
pip install docker-compose

##NODE.JS安装
wget -P /opt/ https://nodejs.org/dist/latest-v8.x/node-v8.16.0-linux-x64.tar.gz 
tar zxf /opt/node-v8.15.1-linux-x64.tar.gz -C /usr/local/
cd /usr/local/
mv node-v8.15.1-linux-x64 nodejs

##下载二进制文件
cd $GOPATH
/usr/bin/expect << EOF
set timeout -1
spawn git clone root@192.168.10.243:/opt/gitfile/fabric.git
expect {
	"yes/no?" { send "yes\n";exp_continue }
	"password:" { send "97hEYpmZKN\n"}
}
expect "password:" { send "97hEYpmZKN\n"}
EOF

tar zxf fabric/hyperledger-fabric-linux-amd64-1.4.0.tar.gz -C ./
cd $GOPATH/src/github.com/
git clone -b release-1.4 https://github.com/hyperledger/fabric-samples.git


cat >> /etc/profile << EOF
export GOROOT=/usr/local/go
export GOPATH=/opt/fabric-deploy/GOPATH
export NODE=/usr/local/nodejs
export PATH=\$PATH:\$GOROOT/bin:\$GOPATH/bin:\$NODE/bin
EOF

source /etc/profile

npm install npm@5.6.0 -g

systemctl stop firewalld
setenforce 0
systemctl restart docker



./get-docker-images.sh
cd ../first-network
##生成网络工件
/usr/bin/expect << EOF
spawn ./byfn.sh generate
expect "n]"
send "y\n"
EOF
##打造网络
/usr/bin/expect << EOF
spawn ./byfn.sh up
expect "n]"
send "y\n"
EOF





##选择订购服务
#要使用Raft订购服务启动网络，请发出：
./byfn.sh up -o etcdraft
#要使用Kafka订购服务启动网络，请发出：
./byfn.sh up -o kafka

yum -y install gcc+ gcc-c++
npm install --unsafe-perm

##服务器配置之初安装docker时就指定其在额外挂载磁盘中
vim /etc/docker/daemon.json
{
     "graph": "/data/docker/docker"
}
##执行docker重新加载当前配置信息
systemctl daemon-reload
systemctl restart docker.service
docker info

fabric实例
https://github.com/aberic/fabric-net-server
https://www.cnblogs.com/aberic/p/9161532.html





