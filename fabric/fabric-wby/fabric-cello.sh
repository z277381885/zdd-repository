yum install git epel-release -y
yum install python-pip -y
pip install --upgrade pip
pip install docker-compose
pip install tox

git clone http://gerrit.hyperledger.org/r/cello
cd cello
SERVER_PUBLIC_IP=192.168.10.107 make start