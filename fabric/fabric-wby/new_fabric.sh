####手动部署fabric

#!/bin/bash
cat >> /etc/hosts << EOF
192.168.10.118 orderer.example.com
192.168.10.118 peer0.org1.example.com
192.168.10.121 peer1.org1.example.com
192.168.10.119 peer0.org2.example.com
EOF

yum -y install wget git expect epel-release
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
yum clean all
yum makecache

wget -P /opt/ https://dl.google.com/go/go1.12.2.linux-amd64.tar.gz
tar zxf /opt/go1.12.2.linux-amd64.tar.gz -C /usr/local/

mkdir -p /opt/fabric-deploy/GOPATH/src/github.com/

cat >> /etc/profile << EOF
export GOROOT=/usr/local/go
export GOPATH=/opt/fabric-deploy/GOPATH
export PATH=\$PATH:\$GOROOT/bin
EOF

source /etc/profile

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

##下载fabric二进制文件
git clone root@192.168.10.243:/opt/gitfile/fabric.git
##安装镜像
./get-docker-images.sh

##
cat >> /etc/profile << EOF
export PATH=\$PATH:\$GOPATH/src/github.com/hyperledger/fabric/bin
EOF

##启动相关docker镜像
docker run -d -t -i -p 5984:5984 hyperledger/fabric-couchdb:amd64-0.4.14
docker run -d -t -i -p 2181:2181 hyperledger/fabric-zookeeper:amd64-0.4.14
docker run -d --name kafka \
-p 9092:9092 \
-e KAFKA_BROKER_ID=0 \
-e KAFKA_ZOOKEEPER_CONNECT=192.168.10.118:2181 \
-e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.10.118:9092 \
-e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 \
-t hyperledger/fabric-kafka:amd64-0.4.14

##准备证书 cryptogen的方式
创建一个配置文件crypto-config.yaml，这里配置了两个组织，org1的Count是2，表示两个peer：

cat > crypto-config.yaml << EOF
OrdererOrgs:
  - Name: Orderer
    Domain: example.com
    Specs:
      - Hostname: orderer
PeerOrgs:
  - Name: Org1
    Domain: org1.example.com
    Template:
      Count: 2
    Users:
      Count: 1
  - Name: Org2
    Domain: org2.example.com
    Template:
      Count: 1
    Users:
      Count: 1
EOF
然后执行crypto，生成证书：
cryptogen generate --config=crypto-config.yaml --output ./certs




docker run -tid --name=zk-3 \
--restart=always \
--privileged=true \
--net=host \
-e ZOO_MY_ID=3 \
-e ZOO_SERVERS=server.1="192.168.10.118:2888:3888 server.2=192.168.10.119:2888:3888 server.3=192.168.10.121:2888:3888" \
-v /data/kafka_cluster/zookeeper/data:/data \
hyperledger/fabric-zookeeper:amd64-0.4.14



docker run -itd --name=kafka3 \
--restart=always \
--net=host \
--privileged=true \
-v /etc/hosts:/etc/hosts \
-v /data/kafka_cluster/kafka/data:/kafka/kafka-logs-data-3 \
-v /data/kafka_cluster/kafka/logs:/opt/kafka/logs \
-e KAFKA_ADVERTISED_HOST_NAME=192.168.10.121 \
-e HOST_IP=192.168.10.121 \
-e KAFKA_ADVERTISED_PORT=9092 \
-e KAFKA_ZOOKEEPER_CONNECT=192.168.10.118:2181,192.168.10.119:2181,192.168.10.121:2181 \
-e KAFKA_BROKER_ID=2 \
-e KAFKA_HEAP_OPTS="-Xmx1024M -Xms1024M" \
hyperledger/fabric-kafka:amd64-0.4.14

##创建topic test
#订阅
docker exec -it kafka1  bash /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server 192.168.10.118:9092,192.168.10.119:9092,192.168.10.121:9092 --topic test --from-beginning

#发送消息
docker exec -it kafka2  bash /opt/kafka/bin/kafka-console-producer.sh --broker-list 192.168.10.118:9092,192.168.10.119:9092,192.168.10.121:9092 --topic test