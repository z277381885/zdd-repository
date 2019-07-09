yum install -y epel-release npm postgresql postgresql-server gcc-c++
wget https://nodejs.org/dist/v8.11.3/node-v8.11.3-linux-x64.tar.xz
tar -xvf node-v8.11.3-linux-x64.tar.xz

postgresql-setup initdb
chown -R postgres:postgres /var/run/postgresql/
systemctl start postgresql
git clone https://github.com/hyperledger/blockchain-explorer.git
cp blockchain-explorer/app/persistence/fabric/postgreSQL/db/updatepg.sql /tmp/
cp blockchain-explorer/app/persistence/fabric/postgreSQL/db/explorerpg.sql /tmp/